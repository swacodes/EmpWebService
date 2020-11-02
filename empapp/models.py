from django.db import models


class Employee(models.Model):

    use_in_migrations = True
    employee_id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=100)
    salary = models.IntegerField()
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    manager_emp_id = models.IntegerField()


def __str__(self):
    return '{},{},{},{},{},{}'.format(self.employee_id,
                                      self.city_name,
                                      self.salary,
                                      self.first_name,
                                      self.second_name,
                                      self.manager_emp_id)


class Meta:
        db_table = 'employee'
