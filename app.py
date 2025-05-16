from weasyprint import HTML
import pyodbc
from flask import Flask, send_file
import io

# Configuración de conexión a SQL Server
# db_config = {
#     'server': '35.237.126.12:1433',
#     'database': 'workflowbsp',
#     'username': 'bsp-inspector',
#     'password': 'BSPwfkNew',
#     'driver': '{ODBC Driver 17 for SQL Server}'
# }

# Función para obtener HTML desde SQL Server
# def get_html_from_db(id):
#     conn_str = f"DRIVER={db_config['driver']};SERVER={db_config['server']};DATABASE={db_config['database']};UID={db_config['username']};PWD={db_config['password']}"
#     conn = pyodbc.connect(conn_str)
#     cursor = conn.cursor()
#     cursor.execute("select contenido from WKF_GestorDocumental where id = ?;", id)
#     html_content = cursor.fetchone()[0]
#     conn.close()
#     return html_content

html_content = """
<!DOCTYPE html>
    <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name='viewport' content='width=device-width, initial-scale=1.0'>
            <title>Documento</title>
            <link rel='stylesheet' href='https://wkfclient.bsp-inspector.cl/assets/styles/editor.css'>
        </head>
        <style>
        /* Basic styles to maintain layout; can be expanded */
        .acta { width: 1024px; margin: 0 auto; font-family: Arial, sans-serif; }
    </style>
        <body>
<div class="acta">
    <h3>I. Antecedentes Generales:</h3>
    <div class="lista-campos">
        <div class="titulo_lista">Compañía:</div>
        <div class="result">&nbsp;</div>
        <div class="titulo_lista">Corredor:</div>
        <div class="result">&nbsp;</div>
        <div class="titulo_lista">Rut Asegurado:</div>
        <div class="result">&nbsp;</div>
        <div class="titulo_lista">Nombre Asegurado:</div>
        <div class="result">&nbsp;</div>
        <div class="titulo_lista">Dirección:</div>
        <div class="result">&nbsp;</div>
        <div class="titulo_lista">Fecha de inspección:</div>
        <div class="result">&nbsp;</div>
        <div class="titulo_lista">Dirección de inspección:</div>
        <div class="result">&nbsp;</div>
    </div>
    <h3>II. Antecedentes de Vehículo</h3>
    <div class="lista-campos">
        <div class="titulo_lista">Marca:</div>
        <div class="result">&nbsp;</div>
        <div class="titulo_lista">Modelo:</div>
        <div class="result">&nbsp;</div>
        <div class="titulo_lista">Patente:</div>
        <div class="result">&nbsp;</div>
        <div class="titulo_lista">Año:</div>
        <div class="result">&nbsp;</div>
        <div class="titulo_lista">Color:</div>
        <div class="result">&nbsp;</div>
        <div class="titulo_lista">Vin (Código Chasis):</div>
        <div class="result">&nbsp;</div>
        <div class="titulo_lista">Código motor:</div>
        <div class="result">&nbsp;</div>
        <div class="titulo_lista">Kilometraje:</div>
        <div class="result">&nbsp;</div>
        <div class="titulo_lista">Puertas:</div>
        <div class="result">&nbsp;</div>
        <div class="titulo_lista">Uso:</div>
        <div class="result">&nbsp;</div>
        <div class="titulo_lista">Cantidad de pasajeros:</div>
        <div class="result">&nbsp;</div>
        <div class="titulo_lista">Combustión:</div>
        <div class="result">&nbsp;</div>
        <div class="titulo_lista">Tracción:</div>
        <div class="result">&nbsp;</div>
        <div class="titulo_lista">Transmisión:</div>
        <div class="result">&nbsp;</div>
        <div class="titulo_lista">Tipo Mercado:</div>
        <div class="result">&nbsp;</div>
    </div>
        <h3>III. Inspección de Daños</h3>
        <table border="1">
            <tbody>
                <tr>
                    <td><strong>Parte o Pieza</strong></td>
                    <td colspan="2"><strong>Delantero Derecho</strong></td>
                    <td colspan="2"><strong>Delantero Izquierdo</strong></td>
                    <td colspan="2"><strong>Trasero Derecho</strong></td>
                    <td colspan="2"><strong>Trasero Izquierdo</strong></td>
                </tr>
                <tr>
                    <td>Tapabarro</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td>Puerta</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td>Pilares</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td>Costados</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td>Molduras</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td>Zocalo</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td>Parachoques</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td>Vidrios</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td>Parabrisas</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td>Espejos</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td>Neblineros</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td>Ópticos</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td>Focos</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td>Bisel</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td>Manillas exteriores</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td>Manillas interiores</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                </tr>
            </tbody>
        </table>
    <table style="width: 100%; page-break-inside: avoid;" border="1">
        <tbody>
            <tr>
                <td><strong>Parte o Pieza</strong></td>
                <td><strong>Tipo Daño</strong></td>
                <td><strong>Deducible</strong></td>
            </tr>
            <tr>
                <td>Techo</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>Capot</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>Maleta o Portalón</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>Mascara</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>Frontal</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>Pintura en General</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>Tapiz</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>Tablero</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>Cubre equipajes</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>Descuadre</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
        </tbody>
    </table>
    <table style="width: 100%; page-break-inside: avoid;" border="1">
        <tbody>
            <tr>
                <td>Observaciones adicionales para daños</td>
                <td>&nbsp;</td>
            </tr>
        </tbody>
    </table>
    <h3>IV. Accesorios Interiores:</h3>
    <table style="width: 100%; page-break-inside: avoid;" border="1">
        <tbody>
            <tr>
                <td>Radio</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>Parlantes</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>Airbag</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>Aire acondicionado</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>Climatizador</td>
                <td>&nbsp;</td>
            </tr>
        </tbody>
    </table>
    <table style="width: 100%; page-break-inside: avoid;" border="1">
        <tbody>
            <tr>
                <td>Espejos</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>Alzavidrios</td>
                <td>&nbsp;</td>
            </tr>
        </tbody>
    </table>
    <hr>
    <table style="width: 100%; page-break-inside: avoid;" border="1">
        <tbody>
            <tr>
                <td>Alarma - Cierre centralizado</td>
                <td>Grabado patente</td>
                <td>Corta corriente</td>
                <td>Cámara retroceso</td>
                <td>Vidrios polarizados</td>
                <td>Láminas seguridad</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
        </tbody>
    </table>
    <div style="width: 100%; page-break-inside: avoid;">
        <h3>V. Accesorios exteriores:</h3>
        <table border="1">
            <tbody>
                <tr>
                    <td>Sunroof</td>
                    <td>Techo panorámico</td>
                    <td>Limpia parabrisas</td>
                    <td>Limpia lunetas</td>
                    <td>Tubo escape</td>
                    <td>Coco arrastre</td>
                    <td>Muela enganche</td>
                </tr>
                <tr>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                </tr>
            </tbody>
        </table>
    </div>
    <h3>VI. Notas importantes a considerar:</h3>
    <div class="lista-campos">
        <ul>
            <li>El Artículo 556 Nº 4 del Código de Comercio, al igual que el contrato de Seguros suscrito manifiesta que: el asegurado está obligado a tomar todas las providencias necesarias para salvar o recobrar la cosa asegurada, o para conservar sus restos, por lo tanto deberán conservar bajo su custodia los objetos dañados hasta su retiro por parte de la Compañía Aseguradora o de quien esta designe para estos efectos.</li>
            <li>Los bienes que el Asegurado y/o los Informes Técnicos determinen como irrecuperables y/o su pérdida total, serán retirados para su venta en calidad de Salvataje “Por cuenta de quien corresponda”, cuya orden emanará del Liquidador Oficial de Seguros o los Aseguradores involucrados.</li>
            <li>El Presupuesto de reparación deberá ser elaborado considerando unidad, Cantidad, valor unitario y total para cada partida afectada, más gastos generales y utilidad.</li>
            <li>El listado de contenidos dañados o afectados, deben indicar, marca, modelo, año de adquisición y valor actual de los bienes, respaldando por cotizaciones de mercado.</li>
            <li>Los documentos y/o antecedentes solicitados tienen carácter de preliminares y de su análisis dependerá si existirá una nueva solicitud de antecedentes.</li>
            <li>La presente Acta, representa las gestiones u acciones iniciales del siniestro denunciado, cuyo contenido será evaluado y analizado en base a los documentos aportados, reservándonos el derecho de inspeccionar los bienes afectados las veces que sea necesario para establecer la real causa de los daños y/o pérdidas.</li>
            <li>
                La función del inspector se acota a tomar registro de los daños que denuncia y/o reclama el asegurado, producto del evento denunciado y levantar un acta de catastro de daños exhibidos por quien atiende al profesional.<br>
                La visita del inspector no confirma cobertura del evento ni valorización de los daños y/o pérdidas, labor que compete a otro funcionario de la empresa liquidadora.
            </li>
        </ul>
    </div>
    <div class="row firmas">
        <div class="col">
            <h3>Firma</h3>
            <p>Nombre:</p>
            <p>Cargo:</p>
        </div>
        <div class="col">
            <h3>Firma Inspector</h3>
            <p>Nombre:</p>
            <p>CONSULTAS AL FONO: 223784300</p>
        </div>
    </div>
    <p>El Asegurado firma en señal de haber leído en todas sus partes este documento, certifica que fue realizada la inspección de los daños producto del siniestro denunciado y recibe copia de la presente acta.</p>
</div>
</body>
    </html>
"""

entire_html = """
<!DOCTYPE html>
    <html lang='es'>
        <head>
            <meta charset='UTF-8'>
            <meta name='viewport' content='width=device-width, initial-scale=1.0'>
            <title>Documento</title>
            <link rel='stylesheet' href='https://wkfclient.bsp-inspector.cl/assets/styles/editor.css'>
        </head>
        <body>
            {html_content}
        </body>
    </html>
"""
# def convert_html_to_pdf(html_content):
#     pdf_file = io.BytesIO()
#     HTML(string=html_content).write_pdf(pdf_file)
#     pdf_file.seek(0)
#     return pdf_file
def convert_html_to_pdf(html_content):
    css = """
    @page {
        size: 800 auto; /* O usa 'Letter', 'Legal', etc. */
        margin: 1cm; /* Ajusta el margen a tu gusto */
    }
    """
    pdf_file = io.BytesIO()
    HTML(string=html_content).write_pdf(pdf_file, stylesheets=[io.BytesIO(css.encode("utf-8"))])
    pdf_file.seek(0)
    return pdf_file
# Servicio con Flask
app = Flask(__name__)

@app.route('/generate-pdf/<int:id>')
def generate_pdf(id):
    try:
        # html_string = get_html_from_db(id)
        pdf_file = convert_html_to_pdf(html_content)
        return send_file(
            pdf_file,
            mimetype='application/pdf',
            as_attachment=True,
            download_name='output.pdf'
        )
    except Exception as e:
        return f"Error generando el PDF: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)