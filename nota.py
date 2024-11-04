agenda_notas = {}

while True:
    print("\n-----📚 Registro de Notas 📝-----")
    print("1. Adicionar notas de aluno ➕")
    print("2. Visualizar médias dos alunos 📊")
    print("3. Sair 🔸")

    opcao = input("Escolha uma opção: ")
    print(50 * '-')

    if opcao == "1":
        aluno = input("Digite o nome do aluno: ")
        if aluno not in agenda_notas:
            agenda_notas[aluno] = {}
        disciplina = input("Digite o nome da disciplina: ")
        nota = float(input("Digite a nota do aluno na disciplina: "))
        if disciplina not in agenda_notas[aluno]:
            agenda_notas[aluno][disciplina] = [nota]
        else:
            agenda_notas[aluno][disciplina].append(nota)
        print("Nota adicionada com sucesso!✅")
    elif opcao == "2":
        print("Médias dos alunos:")
        for aluno, disciplinas in agenda_notas.items():
            print("Aluno:", aluno)
            total_nota = 0
            total_disciplinas = 0
            for disciplina, notas in disciplinas.items():
                media = sum(notas) / len(notas)
                total_nota += sum(notas)
                total_disciplinas += len(notas)
                print("- Disciplina:", disciplina, "| Média:", round(media, 2))
            if total_disciplinas > 0:
                media_geral = total_nota / total_disciplinas
                print("- Média Geral:", round(media_geral, 2))
            else:
                print("- Nenhuma nota registrada.")
    elif opcao == "3":
        print("Encerrando... Até mais👋")
        break
    else:
        print("Opção inválida. Tente novamente.")
