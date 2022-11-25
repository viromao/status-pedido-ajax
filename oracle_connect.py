from multiprocessing import connection
from sqlite3 import connect
import cx_Oracle as cx_Oracle
import sys


cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_21_7")

uid = "RAMTEC"
pwd = "RAMTEC01INFO"
dsn_tns = cx_Oracle.makedsn(
    '192.168.200.250', '1521', service_name='WINT')

connection = cx_Oracle.connect(user="RAMTEC", password="RAMTEC01INFO",
                               dsn=dsn_tns, encoding="UTF-8")


def Pedidos():
    cursor = connection.cursor()
    sql = ("""
                                           SELECT
      PCPEDC.NUMPED,
      PCPEDC.CODCLI,
      round(PCPEDC.VLATEND,2) as valor,
      PCPEDC.DTLIBERA,
      PCPEDC.DTEMISSAOMAPA,
      PCPEDC.DATAPEDCLI,
      PCPEDC.CODFUNCCONF,
      PCPEDC.CODFUNCSEP,
      PCPEDC.CODFILIAL,
      PCPEDC.DTINICIALCHECKOUT,
      PCPEDC.DTFINALCHECKOUT,
      PCPEDC.DTFAT,
      PCPEDC.NUMVIASMAPASEP,
      PCCLIENT.CLIENTE
FROM
    PCPEDC,
    PCCLIENT

WHERE
PCPEDC.CODCLI = PCCLIENT.CODCLI
AND PCPEDC.DTFAT IS NULL
AND PCPEDC.DATAPEDCLI = trunc(sysdate)
AND PCPEDC.CODSUPERVISOR = 1
order By PCPEDC.DATAPEDCLI DESC
    """)

    cursor.execute(sql)
    return(cursor)

def consultaEmitido():
    cursor = connection.cursor()
    sql = """
    SELECT * FROM(
 SELECT
      PCPEDC.NUMPED
FROM
    PCPEDC
WHERE
PCPEDC.DATAPEDCLI = trunc(sysdate)
AND PCPEDC.DTEMISSAOMAPA IS  NULL
AND PCPEDC.DTINICIALCHECKOUT IS NULL
AND PCPEDC.DTFINALCHECKOUT IS NULL
AND PCPEDC.CODSUPERVISOR = 1

order By PCPEDC.DTEMISSAOMAPA DESC
) WHERE ROWNUM=1



    """
    cursor.execute(sql)
    return(cursor)


def consultaEmSeparacao():
    cursor = connection.cursor()
    sql = """
    SELECT * FROM(
 SELECT
      PCPEDC.NUMPED
FROM
    PCPEDC
WHERE
PCPEDC.DATAPEDCLI = trunc(sysdate)
AND PCPEDC.DTEMISSAOMAPA IS NOT NULL
AND PCPEDC.DTINICIALCHECKOUT IS NULL
AND PCPEDC.DTFINALCHECKOUT IS NULL
AND PCPEDC.CODSUPERVISOR = 1

order By PCPEDC.DTEMISSAOMAPA DESC
) WHERE ROWNUM=1



    """
    cursor.execute(sql)
    return(cursor)





def consultaConferido():
    cursor = connection.cursor()
    sql = ("""
    SELECT * FROM(
    SELECT
      PCPEDC.NUMPED
FROM
    PCPEDC
WHERE
PCPEDC.DATAPEDCLI = trunc(sysdate)
AND PCPEDC.DTEMISSAOMAPA IS NOT NULL
AND PCPEDC.DTINICIALCHECKOUT IS NOT NULL
AND PCPEDC.DTFINALCHECKOUT IS NOT NULL
AND PCPEDC.CODSUPERVISOR = 1

order By PCPEDC.DTFINALCHECKOUT DESC
) WHERE ROWNUM=1




    """)
    cursor.execute(sql)
    return(cursor)






def consultaQtdeEmitido():
    cursor = connection.cursor()
    sql = ("""
    SELECT
COUNT(PCPEDC.NUMPED) as "Em Aberto"
FROM
PCPEDC
WHERE
PCPEDC.DATAPEDCLI = trunc(sysdate)
AND PCPEDC.DTEMISSAOMAPA IS NULL
AND PCPEDC.DTINICIALCHECKOUT IS NULL
AND PCPEDC.DTFAT IS NULL
AND PCPEDC.CODSUPERVISOR = 1

order By PCPEDC.DTEMISSAOMAPA DESC
    """)
    cursor.execute(sql)
    return(cursor)


def consultaQtdEmSeparacao():
    cursor = connection.cursor()
    sql = ("""
    SELECT
COUNT(PCPEDC.NUMPED) as "Em Aberto"
FROM
PCPEDC
WHERE
PCPEDC.DATAPEDCLI = trunc(sysdate)
AND PCPEDC.DTEMISSAOMAPA IS NOT NULL
AND PCPEDC.DTINICIALCHECKOUT IS NULL
AND PCPEDC.DTFAT IS NULL
AND PCPEDC.CODSUPERVISOR = 1

order By PCPEDC.DTEMISSAOMAPA DESC
    """)
    cursor.execute(sql)
    return(cursor)


def consultaQtdeEmConferencia():
    cursor = connection.cursor()
    sql = ("""
SELECT
COUNT(PCPEDC.NUMPED) as "Em Separação"
FROM
PCPEDC
WHERE
PCPEDC.DATAPEDCLI = trunc(sysdate)
AND PCPEDC.DTEMISSAOMAPA IS NOT NULL
AND PCPEDC.DTINICIALCHECKOUT IS NOT NULL
AND PCPEDC.DTFINALCHECKOUT IS NULL
AND PCPEDC.DTFAT IS NULL
AND PCPEDC.CODSUPERVISOR = 1

order By PCPEDC.DTEMISSAOMAPA DESC
    """)
    cursor.execute(sql)
    return(cursor)


def consultaQtdeConferido():
    cursor = connection.cursor()
    sql = ("""
SELECT
COUNT(PCPEDC.NUMPED) as "Conferido"
FROM
PCPEDC
WHERE
PCPEDC.DATAPEDCLI = trunc(sysdate)
AND PCPEDC.DTEMISSAOMAPA IS NOT NULL
AND PCPEDC.DTINICIALCHECKOUT IS NOT NULL
AND PCPEDC.DTFINALCHECKOUT IS NOT NULL
AND PCPEDC.DTFAT IS NULL
AND PCPEDC.CODSUPERVISOR = 1

order By PCPEDC.DTEMISSAOMAPA DESC
    """)
    cursor.execute(sql)
    return(cursor)


