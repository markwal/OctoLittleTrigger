/*
 * View model for OctoLittleTrigger
 *
 * Author: Mark Walker
 * License: AGPLv3
 */
$(function() {
    function LittletriggerViewModel(parameters) {
        var self = this;

        // assign the injected parameters, e.g.:
        // self.loginStateViewModel = parameters[0];
        // self.settingsViewModel = parameters[1];

        // TODO: Implement your plugin's view model here.
    }

    // view model class, parameters for constructor, container to bind to
    OCTOPRINT_VIEWMODELS.push([
        LittletriggerViewModel,

        // e.g. loginStateViewModel, settingsViewModel, ...
        [ /* "loginStateViewModel", "settingsViewModel" */ ],

        // e.g. #settings_plugin_littletrigger, #tab_plugin_littletrigger, ...
        [ /* ... */ ]
    ]);
});
