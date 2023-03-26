

def get_property_list():
        return {
            'Current pen parameter' :
            {
                'NAME' : 
                {
                    'name' : 'Param name'
                },
                'DESC' : 
                {
                    'name' : 'DESC'
                    },
            },
            'Marking parameter':{
                'LOOP' : 
                {
                    'name' : 'Loop Count'
                    },
                'MARKSPEED' : 
                {
                    'name' : 'Speed(MM/Second)'
                    },
            },
            'Laser param[FIBER]':{
                'FREQF' : 
                {
                    'name' : 'Frequency(KHz)'
                    },
                'POWERRATIO' : 
                {
                    'name' : 'Power(%)'
                    },
                'QPULSEWIDTH' : 
                {
                    'name' : 'Pulse Width',
                    'prefix': 'ns',
                    'saveWith': '.000000',
                    'options':
                    (
                        2,4,6,9,13,20,30,45,60,80,100,150,200,250,350,500
                     )
                     }
            },
            'Delay param':{
                'STARTTC' : 
                {
                    'name' : 'Start TC(US)'
                    },
                'LASEROFFTC' : 
                {
                    'name' : 'Laser Off TC(UC)'
                    },
                'ENDTC' : 
                {
                    'name' : 'End TC(US)'
                    },
                'POLYTC' : 
                {
                    'name' : 'Polygon TC(US)'
                    },
            },
            'Other':{
            'POINTTIME' : 
            {
                'name' : 'Time per point(ms)'
                },
            'm_bEnableSelfCurveTol' : 
            {
                'name' : 'Enable curve scatter error'
                },
            'm_dSelfCurveTol' : 
            {
                'name' : 'Curve scatter tolerance(MM)'
                },
            'm_bEnableLaserOnLagTime' : 
            {
                'name' : 'Laser on lag time'
                },
            'm_nLaserOnLagTimeUs' : 
            {
                'name' : 'Laser on lag time(us)'
                },
            },
            'Jump param' : {
                'JUMPSPEED' : 
                {
                    'name' : 'Jump Speed(MM/Second)'
                    },
                'm_nMinJumpDelayTCUs' : 
                {
                    'name' : 'Min jump TC(US)'
                    },
                'm_nMaxJumpDelayTCUs' : 
                {
                    'name' : 'Max jump TC(US)'
                    },
                'm_dJumpLengthLimit' : 
                {
                    'name' : 'Jump limit(MM)'
                    },
            },
            # 'SKY optimization':{
                
            # },
            # 'Power linear transformation':{
                
            # },
            # 'Velocity linear transformation':{
                
            # },
            # 'Frecuency ramping':{
                
            # },
            # 'Optimized parameter':{
                
            # },
            'Wobble':{
                'WOBBLEMODE' : 
                {
                    'name' : 'Enable'
                    },
                'HWWOBBLEMODE' : 
                {
                    'name' : 'HWWOBBLEMODE'
                    },
                'WOBBLETYPE' : 
                {
                    'name' : 'Type'
                    },
                'WOBBLEDIAMETER' : 
                {
                    'name' : 'Diameter(MM)'
                    },
                'WOBBLEDIST' : 
                {
                    'name' : 'distance(MM)'
                    },
                'WOBBLEDIAMETERB' : 
                {
                    'name' : 'Diameter2(MM)'
                    },
                'WOBBLEFREQ' : 
                {
                    'name' : 'Relative speed(MM/Second)'
                    },
                
            },
            'Undentified':{
                'JUMPPOSTC' : 
                {
                    'name' : 'JUMPPOSTC'
                    },
                'JUMPDISTTC' : 
                {
                    'name' : 'JUMPDISTTC'
                    },
                'ENACCMODE' : 
                {
                    'name' : 'ENACCMODE'
                    },
                'BreakAngle' : 
                {
                    'name' : 'BreakAngle'
                    },
                'ENDCOMP' : 
                {
                    'name' : 'ENDCOMP'
                    },
                'ACCDIST' : 
                {
                    'name' : 'ACCDIST'
                    },
                'SCANNERMOVEDELAY' : 
                {
                    'name' : 'SCANNERMOVEDELAY'
                    },
                'ScanberBiDirOffset' : 
                {
                    'name' : 'ScanberBiDirOffset'
                    },
                'm_dScanberBiDirCompLen' : 
                {
                    'name' : 'm_dScanberBiDirCompLen'
                    },
                'CURRENT' : 
                {
                    'name' : 'CURRENT'
                    },
                'PULSEMODE' : 
                {
                    'name' : 'PULSEMODE'
                    },
                'PULSENUM' : 
                {
                    'name' : 'PULSENUM'
                    },
                'YAGMODE' : 
                {
                    'name' : 'YAGMODE'
                    },
                'm_nLaserParamIndex' : 
                {
                    'name' : 'm_nLaserParamIndex'
                    },
                'SPIWAVE' : 
                {
                    'name' : 'SPIWAVE'
                    },
                'SPICONTMODE' : 
                {
                    'name' : 'SPICONTMODE'
                    },
                'm_bEndAddPt' : 
                {
                    'name' : 'm_bEndAddPt'
                    },
                'm_nEndPointNum' : 
                {
                    'name' : 'm_nEndPointNum'
                    },
                'm_dEndPointDist' : 
                {
                    'name' : 'm_dEndPointDist'
                    },
                'm_dEndPointTime' : 
                {
                    'name' : 'm_dEndPointTime'
                    },
                'm_nEndPointCyc' : 
                {
                    'name' : 'm_nEndPointCyc'
                    },
                'm_dPointDist' : 
                {
                    'name' : 'm_dPointDist'
                    },
                'm_bEnableWeldWave' : 
                {
                    'name' : 'm_bEnableWeldWave'
                    },
                'm_dWeldWavePower0' : 
                {
                    'name' : 'm_dWeldWavePower0'
                    },
                'm_dWeldWavePower1' : 
                {
                    'name' : 'm_dWeldWavePower1'
                    },
                'm_dWeldWavePower2' : 
                {
                    'name' : 'm_dWeldWavePower2'
                    },
                'm_dWeldWavePower3' : 
                {
                    'name' : 'm_dWeldWavePower3'
                    },
                'm_dWeldWavePower4' : 
                {
                    'name' : 'm_dWeldWavePower4'
                    },
                'm_dWeldWavePower5' : 
                {
                    'name' : 'm_dWeldWavePower5'
                    },
                'm_dWeldWavePower6' : 
                {
                    'name' : 'm_dWeldWavePower6'
                    },
                'm_dWeldWavePower7' : 
                {
                    'name' : 'm_dWeldWavePower7'
                    },
                'm_dWeldWaveWidthMs0' : 
                {
                    'name' : 'm_dWeldWaveWidthMs0'
                    },
                'm_dWeldWaveWidthMs1' : 
                {
                    'name' : 'm_dWeldWaveWidthMs1'
                    },
                'm_dWeldWaveWidthMs2' : 
                {
                    'name' : 'm_dWeldWaveWidthMs2'
                    },
                'm_dWeldWaveWidthMs3' : 
                {
                    'name' : 'm_dWeldWaveWidthMs3'
                    },
                'm_dWeldWaveWidthMs4' : 
                {
                    'name' : 'm_dWeldWaveWidthMs4'
                    },
                'm_dWeldWaveWidthMs5' : 
                {
                    'name' : 'm_dWeldWaveWidthMs5'
                    },
                'm_dWeldWaveWidthMs6' : 
                {
                    'name' : 'm_dWeldWaveWidthMs6'
                    },
                'm_dWeldWaveWidthMs7' : 
                {
                    'name' : 'm_dWeldWaveWidthMs7'
                    },
                'm_dFocusDelta' : 
                {
                    'name' : 'm_dFocusDelta'
                    },
                'm_nFocusCount' : 
                {
                    'name' : 'm_nFocusCount'
                    },
                'm_dFocusOffset' : 
                {
                    'name' : 'm_dFocusOffset'
                    },
                'm_bEnableArcSeg' : 
                {
                    'name' : 'm_bEnableArcSeg'
                    },
                'm_nArcSeg' : 
                {
                    'name' : 'm_nArcSeg'
                    },
                'm_dArcCountCoef0' : 
                {
                    'name' : 'm_dArcCountCoef0'
                    },
                'm_dArcCountCoef1' : 
                {
                    'name' : 'm_dArcCountCoef1'
                    },
                'm_dArcCountCoef2' : 
                {
                    'name' : 'm_dArcCountCoef2'
                    },
                'm_dArcCountCoef3' : 
                {
                    'name' : 'm_dArcCountCoef3'
                    },
                'm_dArcCountCoef4' : 
                {
                    'name' : 'm_dArcCountCoef4'
                    },
                'm_dArcSpeedCoef0' : 
                {
                    'name' : 'm_dArcSpeedCoef0'
                    },
                'm_dArcSpeedCoeff1' : 
                {
                    'name' : 'm_dArcSpeedCoeff1'
                    },
                'm_dArcSpeedCoef2' : 
                {
                    'name' : 'm_dArcSpeedCoef2'
                    },
                'm_dArcSpeedCoef3' : 
                {
                    'name' : 'm_dArcSpeedCoef3'
                    },
                'm_dArcSpeedCoef4' : 
                {
                    'name' : 'm_dArcSpeedCoef4'
                    },
                'm_dArcFreqCoef0' : 
                {
                    'name' : 'm_dArcFreqCoef0'
                    },
                'm_dArcFreqCoef1' : 
                {
                    'name' : 'm_dArcFreqCoef1'
                    },
                'm_dArcFreqCoef2' : 
                {
                    'name' : 'm_dArcFreqCoef2'
                    },
                'm_dArcFreqCoef3' : 
                {
                    'name' : 'm_dArcFreqCoef3'
                    },
                'm_dArcFreqCoef4' : 
                {
                    'name' : 'm_dArcFreqCoef4'
                    },
                'm_bAccSegEnablePower' : 
                {
                    'name' : 'm_bAccSegEnablePower'
                    },
                'm_dAccSegStartPowerRatio' : 
                {
                    'name' : 'm_dAccSegStartPowerRatio'
                    },
                'm_dAccSegPowerLen' : 
                {
                    'name' : 'm_dAccSegPowerLen'
                    },
                'm_bAccSegEnableSpeed' : 
                {
                    'name' : 'm_bAccSegEnableSpeed'
                    },
                'm_dAccSegStartSpeedRatio' : 
                {
                    'name' : 'm_dAccSegStartSpeedRatio'
                    },
                'm_dAccSegSpeedLen' : 
                {
                    'name' : 'm_dAccSegSpeedLen'
                    },
                'm_bDecSegEnablePower' : 
                {
                    'name' : 'm_bDecSegEnablePower'
                    },
                'm_dDecSegStartPowerRatio' : 
                {
                    'name' : 'm_dDecSegStartPowerRatio'
                    },
                'm_dDecSegPowerLen' : 
                {
                    'name' : 'm_dDecSegPowerLen'
                    },
                'm_bDecSegEnableSpeed' : 
                {
                    'name' : 'm_bDecSegEnableSpeed'
                    },
                'm_dDecSegStartSpeedRatio' : 
                {
                    'name' : 'm_dDecSegStartSpeedRatio'
                    },
                'm_dDecSegSpeedLen' : 
                {
                    'name' : 'm_dDecSegSpeedLen'
                    },
                'm_bSkyWrite' : 
                {
                    'name' : 'm_bSkyWrite'
                    },
                'm_nSkyWriteMode' : 
                {
                    'name' : 'm_nSkyWriteMode'
                    },
                'm_dSkyWriteLimitAngle' : 
                {
                    'name' : 'm_dSkyWriteLimitAngle'
                    },
                'm_nSkyWriteNprev' : 
                {
                    'name' : 'm_nSkyWriteNprev'
                    },
                'm_nSkyWriteNpost' : 
                {
                    'name' : 'm_nSkyWriteNpost'
                    },
                'm_dSkyWriteTimelag' : 
                {
                    'name' : 'm_dSkyWriteTimelag'
                    },
                'm_dSkyWriteLaserOnShift' : 
                {
                    'name' : 'm_dSkyWriteLaserOnShift'
                    },
                'm_bEnablePso' : 
                {
                    'name' : 'm_bEnablePso'
                    },
                'm_nPsoMode' : 
                {
                    'name' : 'm_nPsoMode'
                    },
                'm_nPsoPulseWidthNs' : 
                {
                    'name' : 'm_nPsoPulseWidthNs'
                    },
                'm_dPsoDistance' : 
                {
                    'name' : 'm_dPsoDistance'
                    },
                'm_bEnableMarkStep' : 
                {
                    'name' : 'm_bEnableMarkStep'
                    },
                'm_dMarkStep' : 
                {
                    'name' : 'm_dMarkStep'
                    },
                'm_bRasterPointMode' : 
                {
                    'name' : 'm_bRasterPointMode'
                    },
                'm_nRasterPointCountOfOnce' : 
                {
                    'name' : 'm_nRasterPointCountOfOnce'
                    },
                'm_nLasetExtOutputIndex' : 
                {
                    'name' : 'm_nLasetExtOutputIndex'
                    },
                'm_nAccSegSpeedCustomNum' : 
                {
                    'name' : 'm_nAccSegSpeedCustomNum'
                    },
                'm_dAccSegSpeedCustomRatio0' : 
                {
                    'name' : 'm_dAccSegSpeedCustomRatio0'
                    },
                'm_dAccSegSpeedCustomLen0' : 
                {
                    'name' : 'm_dAccSegSpeedCustomLen0'
                    },
                'm_dAccSegSpeedCustomRatio1' : 
                {
                    'name' : 'm_dAccSegSpeedCustomRatio1'
                    },
                'm_dAccSegSpeedCustomLen1' : 
                {
                    'name' : 'm_dAccSegSpeedCustomLen1'
                    },
                'm_dAccSegSpeedCustomRatio2' : 
                {
                    'name' : 'm_dAccSegSpeedCustomRatio2'
                    },
                'm_dAccSegSpeedCustomLen2' : 
                {
                    'name' : 'm_dAccSegSpeedCustomLen2'
                    },
                'm_dAccSegSpeedCustomRatio3' : 
                {
                    'name' : 'm_dAccSegSpeedCustomRatio3'
                    },
                'm_dAccSegSpeedCustomLen3' : 
                {
                    'name' : 'm_dAccSegSpeedCustomLen3'
                    },
                'm_dAccSegSpeedCustomRatio4' : 
                {
                    'name' : 'm_dAccSegSpeedCustomRatio4'
                    },
                'm_dAccSegSpeedCustomLen4' : 
                {
                    'name' : 'm_dAccSegSpeedCustomLen4'
                    },
                'm_dAccSegSpeedCustomRatio5' : 
                {
                    'name' : 'm_dAccSegSpeedCustomRatio5'
                    },
                'm_dAccSegSpeedCustomLen5' : 
                {
                    'name' : 'm_dAccSegSpeedCustomLen5'
                    },
                'm_dAccSegSpeedCustomRatio6' : 
                {
                    'name' : 'm_dAccSegSpeedCustomRatio6'
                    },
                'm_dAccSegSpeedCustomLen6' : 
                {
                    'name' : 'm_dAccSegSpeedCustomLen6'
                    },
                'm_dAccSegSpeedCustomRatio7' : 
                {
                    'name' : 'm_dAccSegSpeedCustomRatio7'
                    },
                'm_dAccSegSpeedCustomLen7' : 
                {
                    'name' : 'm_dAccSegSpeedCustomLen7'
                    },
                'm_dAccSegSpeedCustomRatio8' : 
                {
                    'name' : 'm_dAccSegSpeedCustomRatio8'
                    },
                'm_dAccSegSpeedCustomLen8' : 
                {
                    'name' : 'm_dAccSegSpeedCustomLen8'
                    },
                'm_dAccSegSpeedCustomRatio9' : 
                {
                    'name' : 'm_dAccSegSpeedCustomRatio9'
                    },
                'm_dAccSegSpeedCustomLen9' : 
                {
                    'name' : 'm_dAccSegSpeedCustomLen9'
                    },
                'm_dAccSegSpeedCustomRatio10' : 
                {
                    'name' : 'm_dAccSegSpeedCustomRatio10'
                    },
                'm_dAccSegSpeedCustomLen10' : 
                {
                    'name' : 'm_dAccSegSpeedCustomLen10'
                    },
                'm_dAccSegSpeedCustomRatio11' : 
                {
                    'name' : 'm_dAccSegSpeedCustomRatio11'
                    },
                'm_dAccSegSpeedCustomLen11' : 
                {
                    'name' : 'm_dAccSegSpeedCustomLen11'
                    },
                'm_dAccSegSpeedCustomRatio12' : 
                {
                    'name' : 'm_dAccSegSpeedCustomRatio12'
                    },
                'm_dAccSegSpeedCustomLen12' : 
                {
                    'name' : 'm_dAccSegSpeedCustomLen12'
                    },
                'm_dAccSegSpeedCustomRatio13' : 
                {
                    'name' : 'm_dAccSegSpeedCustomRatio13'
                    },
                'm_dAccSegSpeedCustomLen13' : 
                {
                    'name' : 'm_dAccSegSpeedCustomLen13'
                    },
                'm_dAccSegSpeedCustomRatio14' : 
                {
                    'name' : 'm_dAccSegSpeedCustomRatio14'
                    },
                'm_dAccSegSpeedCustomLen14' : 
                {
                    'name' : 'm_dAccSegSpeedCustomLen14'
                    },
                'm_dAccSegSpeedCustomRatio15' : 
                {
                    'name' : 'm_dAccSegSpeedCustomRatio15'
                    },
                'm_dAccSegSpeedCustomLen15' : 
                {
                    'name' : 'm_dAccSegSpeedCustomLen15'
                    }
            },
        }





        #TODO: Show the names with section based in a dictionary
        # name_of_properties = get_property_list()
        # for header in name_of_properties:
        #     print(f'1.   {header}')
        #     item = QListWidgetItem()
        #     item_widget = QWidget()

        #     line_text = QLabel(header)

        #     self.tableWidget = QTableWidget()
        #     number_of_rows = len(name_of_properties[header])

        #     self.tableWidget.setFixedHeight(31*number_of_rows) #30xrow <---- check it
        #     # set row count 
        #     self.tableWidget.setRowCount(number_of_rows)
        #     # set column count
        #     self.tableWidget.setColumnCount(1)
        #     counter = 0
        #     for property in name_of_properties[header]:
        #         print(f'2.    {property}')
        #         print(f'3.    {name_of_properties[header][property]}')
        #         self.tableWidget.setItem(counter,0, QTableWidgetItem(self.config.get(section,property)))
        #         self.tableWidget.setVerticalHeaderItem(counter,QTableWidgetItem(name_of_properties[header][property]))
        #         self.tableWidget.horizontalHeader().setStretchLastSection(True)
        #         self.tableWidget.horizontalHeader().hide()
        #         self.tableWidget.verticalHeader().setFixedWidth(220)
        #         counter+=1

        #     item_layout = QVBoxLayout()
        #     item_layout.addWidget(line_text)
        #     item_layout.addWidget(self.tableWidget)
        #     item_widget.setLayout(item_layout)
        #     item.setSizeHint(item_widget.sizeHint())

        #     self.property_param_listWidget.addItem(item)
        #     self.property_param_listWidget.setItemWidget(item, item_widget)