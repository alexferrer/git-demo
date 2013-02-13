import sys
print "*** Script para construir el projecto demo **************"
print "*********************************************************"
print "Compilando El codigo"
for i in range(10): 
   print " compilando archivo ",i
print "Compilacion termino exitosamente"
print
print "Ejecutando de unidad (Unit Tests)"
for i in range(5): 
   print " *------"
   for x in range(4):
       print " Testeando metodo ",x,"en archivo ",i
print
print "Test de unidad terminado exitosamente"
print
print "Iniciando deploy al servidor web"
print " moviendo ejecutables al servidor"
print " 1,2,3,4,5" 
print " moviendo graficos y archivos estaticos"
print

#destino = "/var/www/ngnix-default/demo.html"
destino = "demo.html"
with open(destino,"a") as myfile:
     myfile.write("nueva linea <br>")
     myfile.close()

print "Deploy al servidor terminado exitosamente"


print
print "El build y deploy termino exitosamente "
#cambio trifial para gatillar un build en jenkings
status = 0 #0 indica que el build fue exitoso
#status = 1 #0 indica que el build fallo

sys.exit(status)  

