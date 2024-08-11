from django.shortcuts import render, redirect
from .models import Special, Chef
from .forms import SpecialForm, ChefForm, FeedBackForm
from django.contrib import messages
from aiogram import Bot, asyncio
from django.contrib.auth.decorators import permission_required
from django.conf.urls import handler404


from config import TOKEN, TELEGRAM_ID

def index(request):
    all_special = Special.objects.all()
    all_chef = Chef.objects.all()
    
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.save()
            
            first_name = request.POST.get('first_name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            async def send_telegram_message():
                bot = Bot(token=TOKEN)
                
                await bot.send_message((TELEGRAM_ID),
                           f'*{first_name}*\n'
                           f'*{email}*\n'
                           f'{message}',
                           parse_mode='MARKDOWN')
            asyncio.run(send_telegram_message())
        
        messages.success(request, 'Ваше сообщение отправлено! Спасибо!')
        return redirect('index')
    else:
        form = FeedBackForm()
    
    return render(request, 'index.html', {'all_special': all_special, 'all_chef': all_chef, 'form': form})

@permission_required('coffee_shop.can_access_admin_menu')
def add_special(request):
    if request.method == 'POST':
        form = SpecialForm(request.POST, request.FILES)
        if form.is_valid():
            special = form.save(commit=False)
            special.save()
            
        messages.success(request, 'Блюдо успешно добавлено!')
    else:
        form = SpecialForm()
    return render(request, 'add_special.html', {'form': form})

@permission_required('coffee_shop.can_access_admin_menu')
def add_chef(request):
    if request.method == 'POST':
        form = ChefForm(request.POST, request.FILES)
        if form.is_valid():
            chef = form.save(commit=False)
            chef.save()
        messages.success(request, 'Шеф-повар успешно добавлен!')
    else:
        form = ChefForm()
        
        return render(request, 'add_chef.html', {'form': form})
    
@permission_required('coffee_shop.can_access_admin_menu')
def admin_menu(request):
    return render(request, 'admin_menu.html')


