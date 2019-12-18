from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from agendar import Agendar
import time

class CazaCupo():

    def tryIt(self) :
        base_url = "http://consulta.siiau.udg.mx/wco/sspseca.forma_consulta"
        driver = webdriver.Chrome('LA_RUTA_DE_TU_COMPU_AL_DRIVER_DE_SELENIUM') # Ejemplo: /home/jacobnuno/chromedriver (en mi caso usé el driver para chrome)
        driver.implicitly_wait(3)
        bandera = False

        while bandera == False:
            driver.maximize_window()
            driver.get(base_url)
            ciclo = driver.find_element_by_id('cicloID')
            select = Select(ciclo)
            select.select_by_value('ID_DEL_CICLO_A_AGENDAR') # Ejemplo: 202010

            centro = driver.find_element_by_css_selector('[name="cup"]')
            select = Select(centro)
            select.select_by_value('ID_DE_TU_CENTRO') # Ejemplo: D      (el de CUCEI)

            carrera = driver.find_element_by_name('majrp')
            carrera.send_keys('CLAVE_DE_TU_CARRERA') # Ejemplo: INCO      (en mi caso la carrera de ingeniería en computación)

            claveMateria = driver.find_element_by_name('crsep')
            claveMateria.send_keys('CLAVE_DE_TU_MATERIA') # Ejemplo: I7041

            consultar = driver.find_element_by_id('idConsultar')
            consultar.click()

            time.sleep(3)

            cupos = driver.find_element_by_xpath('//td[text()="NRC_DE_TU_MATERIA"]/parent::tr/td[7]') # Ejemplo: 140934

            if(cupos.text > '0'):
                print('I got you... cupos disponibles: ' + cupos.text)
                agendar = Agendar()
                agendar.test()
                bandera = True
            else:
                print('I failed you... cupos disponibles: ' + cupos.text)
                time.sleep(5)

chro = CazaCupo()
chro.tryIt()
