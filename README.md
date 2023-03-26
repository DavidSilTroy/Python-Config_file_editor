# Program to Edit INI files, known as configuration file for computer software

More about [*.ini files](https://es.wikipedia.org/wiki/INI_(extensi%C3%B3n_de_archivo)).
This program is made using python and works in base to a dictionary, to define how to show the information.

## Example of the *.ini file
``` ini
[Default]
NAME = Default
DESC = 
LOOP = 13
MARKSPEED = 1000.000000
POWERRATIO = 50.000000
FREQF = 20000.000000
STARTTC = 0
LASEROFFTC = 100
ENDTC = 0
POLYTC = 100
JUMPSPEED = 2000.000000
JUMPPOSTC = 0
JUMPDISTTC = 0
m_nMinJumpDelayTCUs = 10
m_nMaxJumpDelayTCUs = 85
m_dJumpLengthLimit = 10.000000
ENACCMODE = 0
BreakAngle = 89.000000
ENDCOMP = 0.000000
ACCDIST = 0.000000
SCANNERMOVEDELAY = 0
ScanberBiDirOffset = 0.000000
m_dScanberBiDirCompLen = 0.000000
POINTTIME = 0.100000
CURRENT = 1.000000
PULSEMODE = 0
PULSENUM = 1
YAGMODE = 48
QPULSEWIDTH = 10.000000
m_nLaserParamIndex = 0
SPIWAVE = 0
SPICONTMODE = 0
WOBBLEMODE = 0
HWWOBBLEMODE = 0
WOBBLETYPE = 0
WOBBLEDIAMETER = 1.000000
WOBBLEDIAMETERB = 0.500000
WOBBLEDIST = 0.500000
WOBBLEFREQ = 1000.000000
m_bEndAddPt = 0
m_nEndPointNum = 1
m_dEndPointDist = 0.010000
m_dEndPointTime = 1.000000
m_nEndPointCyc = 1
m_dPointDist = 0.500000
.... etc
```
## Example of dictionary
``` python
toShowPropertyList = 
{
    'Current pen parameter' : #Group of properties to show together
    {
        'NAME' : # This is the property name to search in the *.ini file
        {
            'name' : 'Param name' # 'name' is how it will be showed to the user
        },
        'DESC' : # This is the property name to search in the *.ini file
        {
            'name' : 'DESC' # 'name' is how it will be showed to the user
            },
    },
    'Marking parameter': #Group of properties to show together
    { 
        'LOOP' :  # This is the property name to search in the *.ini file
        {
            'name' : 'Loop Count' # 'name' is how it will be showed to the user
        },
        'MARKSPEED' : 
        {
            'name' : 'Speed(MM/Second)' # 'name' is how it will be showed to the user
        },
    },
    'Laser param[FIBER]': #Group of properties to show together
    {
        'FREQF' : 
        {
            'name' : 'Frequency(KHz)' # 'name' is how it will be showed to the user
            },
        'POWERRATIO' : 
        {
            'name' : 'Power(%)' # 'name' is how it will be showed to the user
            }, 
        'QPULSEWIDTH' : 
        {
            'name' : 'Pulse Width', # 'name' is how it will be showed to the user
            'prefix': 'ns', # 'prefix' in this case to show nano seconds, to add in the numer like 15ns or 100ns
            'saveWith': '.000000', #'saveWhit' to add at the end of the number because of the *.ini file
            'options': #'options' because in this case the user only can select one of the options to save
            (
                2,4,6,9,13,20,30,45,60,80,100,150,200,250,350,500 #different options
            )
        }
    },
    #To understand how it works
    'Another group':
    {
        'PropertyNameInFile':
        {
            'name': 'Name User See',
            'prefix': 'Can be nano, micro, pico, etc',
            'options' :  #'options' because in this case the user only can select one of the options to save
            (
                'when', 'it', 'is', 'a', 'limited', 'input','to','show','like','list', #different options
            )
            'anotherOption' : {
                'SomethinNew' : 'A new option maybe?'
            }
        }
    }
    #to every property that does not have a group yet
    'Undentified':{
            'JUMPPOSTC' : 
            {
                'name' : 'JUMPPOSTC'
                },
            'JUMPDISTTC' : 
            {
                'name' : 'JUMPDISTTC'
                },
            .... etc
    
    }
}
```

---
## Possible libraries to create this program:

- pyQT5
- PySide2
- Tkinter
- wxPython
- Kivy

## Selected
[ &#9989; pyQT5](https://www.riverbankcomputing.com/static/Docs/PyQt5/introduction.html)

---
<strong> Remember to use a VIRTUAL ENVIRONMENT! </strong>

## Install libraries
Go to the main folder and:
```python  
pip install -r ./requirements.txt
```
It can be `pip3` or also `python3 pip`
## Run with python
To run the program it is necessary to install the library `pyqt5` and then run the `main.py` file:
```python  
python ./main.py
```

## Create Executable
It is necessary to install the library `pyinstaller` and then use:
```python
pyinstaller -F main.py --noconsole
```
## UI to be develop
![User Interface](/assets/images/example/ui_to_develop.png)

### List of roperties from parameters
![User Interface](/assets/images/example/parameter_property_list_1.png)
![User Interface](/assets/images/example/parameter_property_list_2.png)
![User Interface](/assets/images/example/parameter_property_list_3.png)


## Result
![...](/assets/something.png)

## TODO
- ....

