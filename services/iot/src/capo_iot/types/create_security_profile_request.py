"""Generated from Smithy shape ``com.amazonaws.iot#CreateSecurityProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.additional_metrics_to_retain_list
    import capo_iot.types.additional_metrics_to_retain_v2_list
    import capo_iot.types.alert_targets
    import capo_iot.types.behaviors
    import capo_iot.types.metrics_export_config
    import capo_iot.types.security_profile_description
    import capo_iot.types.security_profile_name
    import capo_iot.types.tag_list


class CreateSecurityProfileRequest(TypedDict, closed=True):
    security_profile_name: "capo_iot.types.security_profile_name.SecurityProfileName"
    """<p>The name you are giving to the security profile.</p>"""
    security_profile_description: NotRequired[
        "capo_iot.types.security_profile_description.SecurityProfileDescription"
    ]
    """<p>A description of the security profile.</p>"""
    behaviors: NotRequired["capo_iot.types.behaviors.Behaviors"]
    """<p>Specifies the behaviors that, when violated by a device (thing), cause an alert.</p>"""
    alert_targets: NotRequired["capo_iot.types.alert_targets.AlertTargets"]
    """<p>Specifies the destinations to which alerts are sent. (Alerts are always sent to the console.) Alerts are generated when a device (thing) violates a behavior.</p>"""
    additional_metrics_to_retain: NotRequired[
        "capo_iot.types.additional_metrics_to_retain_list.AdditionalMetricsToRetainList"
    ]
    """<p> <i>Please use <a>CreateSecurityProfileRequest$additionalMetricsToRetainV2</a> instead.</i> </p> <p>A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's <code>behaviors</code>, but it is also retained for any metric specified here. Can be used with custom metrics; cannot be used with dimensions.</p>"""
    additional_metrics_to_retain_v2: NotRequired[
        "capo_iot.types.additional_metrics_to_retain_v2_list.AdditionalMetricsToRetainV2List"
    ]
    """<p>A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's <code>behaviors</code>, but it is also retained for any metric specified here. Can be used with custom metrics; cannot be used with dimensions.</p>"""
    tags: NotRequired["capo_iot.types.tag_list.TagList"]
    """<p>Metadata that can be used to manage the security profile.</p>"""
    metrics_export_config: NotRequired[
        "capo_iot.types.metrics_export_config.MetricsExportConfig"
    ]
    """<p>Specifies the MQTT topic and role ARN required for metric export.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSecurityProfileRequest) -> dict:
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
    if "tags" in value:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.serialize_json(value["tags"])
    if "metrics_export_config" in value:
        import capo_iot.types.metrics_export_config

        out["metricsExportConfig"] = (
            capo_iot.types.metrics_export_config.serialize_json(
                value["metrics_export_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSecurityProfileRequest:
    out: CreateSecurityProfileRequest = {}  # type: ignore[typeddict-item]
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
    if "tags" in data:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.deserialize_json(data["tags"])
    if "metricsExportConfig" in data:
        import capo_iot.types.metrics_export_config

        out["metrics_export_config"] = (
            capo_iot.types.metrics_export_config.deserialize_json(
                data["metricsExportConfig"]
            )
        )
    return out
