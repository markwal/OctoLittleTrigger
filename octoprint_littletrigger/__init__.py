# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import octoprint.printer


class LittletriggerCallback(octoprint.printer.PrinterCallback):
	def __init__(self, settings, event_bus, logger):
		self._settings = settings
		self._event_bus = event_bus
		self._logger = logger

	def on_printer_add_message(self, data):
		if self._settings.get(["comm_message"]) in data:
			event_to_trigger = self._settings.get(["event_to_trigger"])
			self._logger.warn("found message, firing event %s" % event_to_trigger)
			self._event_bus.fire(event_to_trigger)


class LittletriggerPlugin(octoprint.plugin.StartupPlugin,
		                  octoprint.plugin.SettingsPlugin,
                          octoprint.plugin.TemplatePlugin):

	##~~ StartupPlugin mixin

	def on_after_startup(self):
		self._printer.register_callback(LittletriggerCallback(self._settings, self._event_bus, self._logger))

	##~~ SettingsPlugin mixin

	def get_settings_defaults(self):
		return dict(
			# put your plugin's default settings here
			comm_message='enqueueing "M81',
			event_to_trigger='PowerOff'
		)

	##~~ TemplatePlugin mixin

	def get_template_configs(self):
		return [
			dict(type="settings", custom_bindings=False)
		]

	##~~ Softwareupdate hook

	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			littletrigger=dict(
				displayName="Littletrigger Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="markwal",
				repo="OctoLittleTrigger",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/markwal/OctoLittleTrigger/archive/{target_version}.zip"
			)
		)


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "LittleTrigger"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = LittletriggerPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

