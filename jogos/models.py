from django.db import models

class Modalidade(models.Model):
    tipo_choices = [
        ('Coletiva', 'COLETIVA'),
        ('Individual', 'INDIVIDUAL'),
    ]

    nome = models.CharField(max_length=50, unique=True)
    tipo = models.CharField(max_length=10, choices=tipo_choices)
    max_atletas = models.PositiveIntegerField()

    class Meta:
        verbose_name="Modalidade"
        verbose_name_plural = "Modalidades"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Tecnico(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)

    class Meta:
        verbose_name="Técnico"
        verbose_name_plural = "Técnicos"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Equipe(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    curso = models.CharField(max_length=50)
    cor = models.CharField(max_length=8)
    criada_em = models.DateTimeField(auto_now_add=True)
    tecnico = models.OneToOneField(Tecnico, on_delete=models.CASCADE, related_name='equipe', null=True, blank=True)

    class Meta:
        verbose_name="Equipe"
        verbose_name_plural = "Equipes"
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def atletas_count(self):
        return self.atletas.count()


class Atleta(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField()
    equipe = models.ForeignKey(Equipe, on_delete=models.PROTECT, related_name='atletas')
    modalidade = models.ManyToManyField(Modalidade, related_name='atletas', blank=True)

    class Meta:
        verbose_name="Atleta"
        verbose_name_plural = "Atletas"
        ordering = ['nome']

    def __str__(self):
        return self.nome