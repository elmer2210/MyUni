from django.db import models


# Create your models here.

class Speciality(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50)
    duration = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt = "{0}, (Duration: {1} year(s))"
        return txt.format(self.name, self.duration)


class Student(models.Model):
    dni = models.CharField(max_length=10, primary_key=True)
    fatherLastName = models.CharField(max_length=35)
    motherLastName = models.CharField(max_length=35)
    names = models.CharField(max_length=35)
    dateBorn = models.DateField()
    sexes = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    sex = models.CharField(max_length=1, choices=sexes, default='M')
    speciality = models.ForeignKey(Speciality, null=False, blank=False, on_delete=models.CASCADE)
    isStudying = models.BooleanField(default=True)

    def full_name(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.fatherLastName, self.motherLastName, self.names)

    def __str__(self):
        txt = "{0} /speciality: {1} / {2}"
        if self.isStudying:
            student_state = "VIGENTE"
        else:
            student_state = "DE BAJA"
        return txt.format(self.full_name(), self.speciality, student_state)


class Curse(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=30)
    credits = models.PositiveSmallIntegerField()
    teacher = models.CharField(max_length=100)

    def __str__(self):
        txt = "{0} ({1}) / Docente: {2}"
        return txt.format(self.name, self.code, self.teacher)


class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, null=False, blank=False, on_delete=models.CASCADE)
    curse = models.ForeignKey(Curse, null=False, blank=False, on_delete=models.CASCADE)
    registrationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt = "{0} matriculad{1} en el curso {2} / Fecha: {3}"
        if self.student.sex == "F":
            sex_leter = "a"
        else:
            sex_leter = "o"
        registration_date = self.registrationDate.strftime("%A %d/%m/%Y %H:%M:%S")
        return txt.format(self.student.full_name(), sex_leter, self.curse, registration_date)
