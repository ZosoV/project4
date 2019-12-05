from projects.models import School

school = School(name="School of Mathematical and Computational Sciences", code="MATH") 
school.save()
school = School(name="School of Biological Sciences and Engineering", code="BIO")
school.save()
school = School(name="School of Geological Sciences and Engineering", code="GEO")
school.save()
school = School(name="School of Chemical Sciences and Engineering", code="CHEM")
school.save()
school = School(name="School of Physical Sciences and Nanotechnology", code="PHYS")
school.save()
