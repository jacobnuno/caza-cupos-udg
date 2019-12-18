from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
import time

class Agendar():

    def test(self) :
        base_url = "http://siiauescolar.siiau.udg.mx/wus/gupprincipal.inicio"
        driver = webdriver.Chrome('LA_RUTA_DE_TU_COMPU_AL_DRIVER_DE_SELENIUM') # Ejemplo: /home/jacobnuno/chromedriver (en mi caso uso el driver para chrome)
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        frame_modal = driver.find_element_by_name("mainFrame")
        driver.switch_to_frame(frame_modal)

        code = driver.find_element_by_name('p_codigo_c')
        code.send_keys(TU_CODIGO) # Ejemplo: 212543192           (no es mi código)

        nip = driver.find_element_by_name('p_clave_c')
        nip.send_keys(TU_NIP) # Ejemplo: secret01

        submit = driver.find_element_by_css_selector('[type="submit"]')
        submit.click()

        menu = driver.find_element_by_name("Menu")
        driver.switch_to_frame(menu)
        time.sleep(1)

        menuAlumno = driver.find_element_by_link_text('ALUMNOS')
        menuAlumno.click()
        time.sleep(1)

        menuRegistro = driver.find_element_by_link_text('REGISTRO')
        menuRegistro.click()
        time.sleep(1)

        calendario = driver.find_element_by_id('carreraID')
        select = Select(calendario)
        select.select_by_value('ID_DE_TU_CARRERA_QUE_APARECE_EN_SIIAU') # Ejemplo: INCO-201520
        time.sleep(1)

        registro = driver.find_element_by_link_text('Registro')
        registro.click()
        time.sleep(1)

        driver.switch_to.default_content()
        menu = driver.find_element_by_name("mainFrame")
        driver.switch_to_frame(menu)
        time.sleep(1)

        menu = driver.find_element_by_name("Contenido")
        driver.switch_to_frame(menu)
        time.sleep(1)

        input = driver.find_element_by_xpath('//form/table/tbody/tr[2]/td[1]/input')
        input.send_keys('NRC_DE_TU_MATERIA') # Ejemplo: 140934

        submit = driver.find_element_by_css_selector('[action] [type="submit"]')
        submit.click()

        time.sleep(15)
