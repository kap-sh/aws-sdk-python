"""Generated from Smithy shape ``com.amazonaws.iot#UpdateSecurityProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.additional_metrics_to_retain_list
    import capo_iot.types.additional_metrics_to_retain_v2_list
    import capo_iot.types.alert_targets
    import capo_iot.types.behaviors
    import capo_iot.types.delete_additional_metrics_to_retain
    import capo_iot.types.delete_alert_targets
    import capo_iot.types.delete_behaviors
    import capo_iot.types.delete_metrics_export_config
    import capo_iot.types.metrics_export_config
    import capo_iot.types.optional_version
    import capo_iot.types.security_profile_description
    import capo_iot.types.security_profile_name


class UpdateSecurityProfileRequest(TypedDict, closed=True):
    security_profile_name: "capo_iot.types.security_profile_name.SecurityProfileName"
    """<p>The name of the security profile you want to update.</p>"""
    security_profile_description: NotRequired[
        "capo_iot.types.security_profile_description.SecurityProfileDescription"
    ]
    """<p>A description of the security profile.</p>"""
    behaviors: NotRequired["capo_iot.types.behaviors.Behaviors"]
    """<p>Specifies the behaviors that, when violated by a device (thing), cause an alert.</p>"""
    alert_targets: NotRequired["capo_iot.types.alert_targets.AlertTargets"]
    """<p>Where the alerts are sent. (Alerts are always sent to the console.)</p>"""
    additional_metrics_to_retain: NotRequired[
        "capo_iot.types.additional_metrics_to_retain_list.AdditionalMetricsToRetainList"
    ]
    """<p> <i>Please use <a>UpdateSecurityProfileRequest$additionalMetricsToRetainV2</a> instead.</i> </p> <p>A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's <code>behaviors</code>, but it is also retained for any metric specified here. Can be used with custom metrics; cannot be used with dimensions.</p>"""
    additional_metrics_to_retain_v2: NotRequired[
        "capo_iot.types.additional_metrics_to_retain_v2_list.AdditionalMetricsToRetainV2List"
    ]
    """<p>A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's behaviors, but it is also retained for any metric specified here. Can be used with custom metrics; cannot be used with dimensions.</p>"""
    delete_behaviors: "capo_iot.types.delete_behaviors.DeleteBehaviors"
    """<p>If true, delete all <code>behaviors</code> defined for this security profile. If any <code>behaviors</code> are defined in the current invocation, an exception occurs.</p>"""
    delete_alert_targets: "capo_iot.types.delete_alert_targets.DeleteAlertTargets"
    """<p>If true, delete all <code>alertTargets</code> defined for this security profile. If any <code>alertTargets</code> are defined in the current invocation, an exception occurs.</p>"""
    delete_additional_metrics_to_retain: "capo_iot.types.delete_additional_metrics_to_retain.DeleteAdditionalMetricsToRetain"
    """<p>If true, delete all <code>additionalMetricsToRetain</code> defined for this security profile. If any <code>additionalMetricsToRetain</code> are defined in the current invocation, an exception occurs.</p>"""
    expected_version: NotRequired["capo_iot.types.optional_version.OptionalVersion"]
    """<p>The expected version of the security profile. A new version is generated whenever the security profile is updated. If you specify a value that is different from the actual version, a <code>VersionConflictException</code> is thrown.</p>"""
    metrics_export_config: NotRequired[
        "capo_iot.types.metrics_export_config.MetricsExportConfig"
    ]
    """<p>Specifies the MQTT topic and role ARN required for metric export.</p>"""
    delete_metrics_export_config: (
        "capo_iot.types.delete_metrics_export_config.DeleteMetricsExportConfig"
    )
    """<p>Set the value as true to delete metrics export related configurations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSecurityProfileRequest) -> dict:
    out: dict = {}
    if "security_profile_description" in value:
        out["securityProfileDescription"] = value["security_profile_description"]
    if "behaviors" in value:
        import capo_iot.types.behaviors

        out["behaviors"] = capo_iot.types.behaviors.serialize_json(value["behaviors"])
    if "alert_targets" in value:
        import capo_iot.types.alert_targets

        out["alertTargets"] = capo_iot.types.alert_targets.serialize_json(
            value["alert_targets"]
        )
    if "additional_metrics_to_retain" in value:
        import capo_iot.types.additional_metrics_to_retain_list

        out["additionalMetricsToRetain"] = (
            capo_iot.types.additional_metrics_to_retain_list.serialize_json(
                value["additional_metrics_to_retain"]
            )
        )
    if "additional_metrics_to_retain_v2" in value:
        import capo_iot.types.additional_metrics_to_retain_v2_list

        out["additionalMetricsToRetainV2"] = (
            capo_iot.types.additional_metrics_to_retain_v2_list.serialize_json(
                value["additional_metrics_to_retain_v2"]
            )
        )
    out["deleteBehaviors"] = value.get("delete_behaviors", False)
    out["deleteAlertTargets"] = value.get("delete_alert_targets", False)
    out["deleteAdditionalMetricsToRetain"] = value.get(
        "delete_additional_metrics_to_retain", False
    )
    if "metrics_export_config" in value:
        import capo_iot.types.metrics_export_config

        out["metricsExportConfig"] = (
            capo_iot.types.metrics_export_config.serialize_json(
                value["metrics_export_config"]
            )
        )
    out["deleteMetricsExportConfig"] = value.get("delete_metrics_export_config", False)
    return out


def deserialize_json(data: dict) -> UpdateSecurityProfileRequest:
    out: UpdateSecurityProfileRequest = {}  # type: ignore[typeddict-item]
    if "securityProfileDescription" in data:
        out["security_profile_description"] = data["securityProfileDescription"]
    if "behaviors" in data:
        import capo_iot.types.behaviors

        out["behaviors"] = capo_iot.types.behaviors.deserialize_json(data["behaviors"])
    if "alertTargets" in data:
        import capo_iot.types.alert_targets

        out["alert_targets"] = capo_iot.types.alert_targets.deserialize_json(
            data["alertTargets"]
        )
    if "additionalMetricsToRetain" in data:
        import capo_iot.types.additional_metrics_to_retain_list

        out["additional_metrics_to_retain"] = (
            capo_iot.types.additional_metrics_to_retain_list.deserialize_json(
                data["additionalMetricsToRetain"]
            )
        )
    if "additionalMetricsToRetainV2" in data:
        import capo_iot.types.additional_metrics_to_retain_v2_list

        out["additional_metrics_to_retain_v2"] = (
            capo_iot.types.additional_metrics_to_retain_v2_list.deserialize_json(
                data["additionalMetricsToRetainV2"]
            )
        )
    if "deleteBehaviors" in data:
        out["delete_behaviors"] = data["deleteBehaviors"]
    else:
        out["delete_behaviors"] = False
    if "deleteAlertTargets" in data:
        out["delete_alert_targets"] = data["deleteAlertTargets"]
    else:
        out["delete_alert_targets"] = False
    if "deleteAdditionalMetricsToRetain" in data:
        out["delete_additional_metrics_to_retain"] = data[
            "deleteAdditionalMetricsToRetain"
        ]
    else:
        out["delete_additional_metrics_to_retain"] = False
    if "metricsExportConfig" in data:
        import capo_iot.types.metrics_export_config

        out["metrics_export_config"] = (
            capo_iot.types.metrics_export_config.deserialize_json(
                data["metricsExportConfig"]
            )
        )
    if "deleteMetricsExportConfig" in data:
        out["delete_metrics_export_config"] = data["deleteMetricsExportConfig"]
    else:
        out["delete_metrics_export_config"] = False
    return out
