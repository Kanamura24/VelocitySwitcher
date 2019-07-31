#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file VelocitySwitcherTest.py
 @brief Filter for TimedVelocity2D, changes output according to Game State and Camera Recognition Result.
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import VelocitySwitcher_idl

# Import Service implementation class
# <rtc-template block="service_impl">
from VelocitySwitcher_idl_example import *

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
velocityswitchertest_spec = ["implementation_id", "VelocitySwitcherTest", 
		 "type_name",         "VelocitySwitcherTest", 
		 "description",       "Filter for TimedVelocity2D, changes output according to Game State and Camera Recognition Result.", 
		 "version",           "1.0.0", 
		 "vendor",            "KanamuraRobotics", 
		 "category",          "Controller", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class VelocitySwitcherTest
# @brief Filter for TimedVelocity2D, changes output according to Game State and Camera Recognition Result.
# 
# 
class VelocitySwitcherTest(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_vel_out = OpenRTM_aist.instantiateDataType(RTC.TimedVelocity2D)
		"""
		"""
		self._vel_outIn = OpenRTM_aist.InPort("vel_out", self._d_vel_out)
		self._d_vel_in = OpenRTM_aist.instantiateDataType(RTC.TimedVelocity2D)
		"""
		"""
		self._vel_inOut = OpenRTM_aist.OutPort("vel_in", self._d_vel_in)

		"""
		"""
		self._gameStateSwitcherPort = OpenRTM_aist.CorbaPort("gameStateSwitcher")
		"""
		"""
		self._colorSwitcherPort = OpenRTM_aist.CorbaPort("colorSwitcher")

		

		"""
		"""
		self._gameStateSwitcherService = OpenRTM_aist.CorbaConsumer(interfaceType=KanamuraRobotics.VelocitySwitcherService)
		"""
		"""
		self._colorSwitcherService = OpenRTM_aist.CorbaConsumer(interfaceType=KanamuraRobotics.VelocitySwitcherService)

		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		
		# Set InPort buffers
		self.addInPort("vel_out",self._vel_outIn)
		
		# Set OutPort buffers
		self.addOutPort("vel_in",self._vel_inOut)
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		self._gameStateSwitcherPort.registerConsumer("KanamuraRobotics::VelocitySwitcherService", "KanamuraRobotics::VelocitySwitcherService", self._gameStateSwitcherService)
		self._colorSwitcherPort.registerConsumer("KanamuraRobotics::VelocitySwitcherService", "KanamuraRobotics::VelocitySwitcherService", self._colorSwitcherService)
		
		# Set CORBA Service Ports
		self.addPort(self._gameStateSwitcherPort)
		self.addPort(self._colorSwitcherPort)
		
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	# 
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The activated action (Active state entry action)
	#	# former rtc_active_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	# 
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onActivated(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The deactivated action (Active state exit action)
	#	# former rtc_active_exit()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onDeactivated(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The execution action that is invoked periodically
	#	# former rtc_active_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onExecute(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	



def VelocitySwitcherTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=velocityswitchertest_spec)
    manager.registerFactory(profile,
                            VelocitySwitcherTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    VelocitySwitcherTestInit(manager)

    # Create a component
    comp = manager.createComponent("VelocitySwitcherTest")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

