from django.shortcuts import render, redirect
from .models import Task, Musician

#Essa função renderiza a página principal. Ela atualiza a página para que todas as informações recentes apareçam na página principal
def home(request): 
  tasks = Task.objects.all() 
  artistas = Musician.objects.all()
  return render(request, 'home.html', context={"tasks": tasks,"artistas": artistas})

#Essa função atribui a lista de todas as tarefas do banco de dados à variável "tasks"
def list_tasks(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "list_tasks.html", context=context)

#Essa função nos permite criar as tarefas dentro da classe Task. Dentro da função, nós escolhemos quais informações sobre a tarefa serão pedidas, por exemplo: título, descrição e prazo
def create_task(request):
  if request.method == 'POST':
    print(request.POST)
    Task.objects.create(
      title=request.POST["title"],
      description=request.POST["description"],
      due_date=request.POST["due_date"],
    )
    return redirect("home")
 
  return  render(request, "tasks_forms.html")

#Essa função permite que as informações sobre a tarefa sejam editadas através da página principal. Após as edições serem realizadas, essa função garante que a tarefa seja atualizada
def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    # É necessário converter o objeto datetime para uma string para que ele apareça corretamente como valor do input do meu template
    task.due_date = task.due_date.strftime('%Y-%m-%d')

    if request.method == "POST":
        task.title = request.POST["title"]
        task.description = request.POST["description"]
        task.due_date = request.POST["due_date"]
        task.save()
        return redirect("home")

    return render(request, "tasks_forms.html", context={"task": task})

#Essa função nos permite deletar qualquer tarefa que já tenha sido cadastrada na lista
def delete_task(request, task_id):
    task = Task.objects.get(id = task_id)
    if request.method == "POST":
      if "confirm" in request.POST:
        task.delete()

      return redirect("home")

    return render(request, "delete_form.html", context={"task": task})

#Essa função atribui a lista de todas as tarefas do banco de dados à variável "artist"
def list_musician(request):
    artist = Musician.objects.all()
    context = {"artists": artist}
    return render(request, "list_musicians.html", context=context)

#Essa função nos permite criar os artistas dentro da classe Musician. Dentro da função, nós escolhemos quais informações sobre os artistas deverão ser inseridas, por exemplo: nome, sobrenome e instrumento
def create_musician(request):
  if request.method == 'POST':
    print(request.POST)
    Musician.objects.create(
      nome=request.POST["nome"],
      sobrenome=request.POST["sobrenome"],
      instrumento=request.POST["instrumento"]
    )
    return redirect("home")
 
  return  render(request, "musicians_forms.html")

#Essa função permite que as informações sobre o artista sejam editadas através da página principal. Após as edições serem realizadas, essa função garante que as informações sobre o artista sejam atualizadas
def update_musician(request, musician_id):
    artist = Musician.objects.get(id=musician_id)
    if request.method == "POST":
        artist.nome = request.POST["nome"]
        artist.sobrenome = request.POST["sobrenome"]
        artist.instrumento = request.POST["instrumento"]
        artist.save()
        return redirect ("home")
    return render(request, "musicians_forms.html", context={"artist": artist})


#Essa função nos permite deletar qualquer artista que já tenha sido cadastrado na lista
def delete_musician(request, musician_id):
    artist = Musician.objects.get(id=musician_id)
    if request.method == "POST":
      if "confirm" in request.POST:
        artist.delete()

      return redirect("home")

    return render(request, "delete_form.html", context={"artist": artist})
