"""Generated from Smithy shape ``com.amazonaws.iot#UpdateSecurityProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.additional_metrics_to_retain_list
    import capo_iot.types.additional_metrics_to_retain_v2_list
    import capo_iot.types.alert_targets
    import capo_iot.types.behaviors
    import capo_iot.types.metrics_export_config
    import capo_iot.types.security_profile_arn
    import capo_iot.types.security_profile_description
    import capo_iot.types.security_profile_name
    import capo_iot.types.timestamp
    import capo_iot.types.version


class UpdateSecurityProfileResponse(TypedDict, closed=True):
    security_profile_name: NotRequired[
        "capo_iot.types.security_profile_name.SecurityProfileName"
    ]
    """<p>The name of the security profile that was updated.</p>"""
    security_profile_arn: NotRequired[
        "capo_iot.types.security_profile_arn.SecurityProfileArn"
    ]
    """<p>The ARN of the security profile that was updated.</p>"""
    security_profile_description: NotRequired[
        "capo_iot.types.security_profile_description.SecurityProfileDescription"
    ]
    """<p>The description of the security profile.</p>"""
    behaviors: NotRequired["capo_iot.types.behaviors.Behaviors"]
    """<p>Specifies the behaviors that, when violated by a device (thing), cause an alert.</p>"""
    alert_targets: NotRequired["capo_iot.types.alert_targets.AlertTargets"]
    """<p>Where the alerts are sent. (Alerts are always sent to the console.)</p>"""
    additional_metrics_to_retain: NotRequired[
        "capo_iot.types.additional_metrics_to_retain_list.AdditionalMetricsToRetainList"
    ]
    """<p> <i>Please use <a>UpdateSecurityProfileResponse$additionalMetricsToRetainV2</a> instead.</i> </p> <p>A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the security profile's <code>behaviors</code>, but it is also retained for any metric specified here.</p>"""
    additional_metrics_to_retain_v2: NotRequired[
        "capo_iot.types.additional_metrics_to_retain_v2_list.AdditionalMetricsToRetainV2List"
    ]
    """<p>A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's behaviors, but it is also retained for any metric specified here. Can be used with custom metrics; cannot be used with dimensions.</p>"""
    version: "capo_iot.types.version.Version"
    """<p>The updated version of the security profile.</p>"""
    creation_date: NotRequired["capo_iot.types.timestamp.Timestamp"]
    """<p>The time the security profile was created.</p>"""
    last_modified_date: NotRequired["capo_iot.types.timestamp.Timestamp"]
    """<p>The time the security profile was last modified.</p>"""
    metrics_export_config: NotRequired[
        "capo_iot.types.metrics_export_config.MetricsExportConfig"
    ]
    """<p>Specifies the MQTT topic and role ARN required for metric export.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSecurityProfileResponse) -> dict:
    out: dict = {}
    if "security_profile_name" in value:
        out["securityProfileName"] = value["security_profile_name"]
    if "security_profile_arn" in value:
        out["securityProfileArn"] = value["security_profile_arn"]
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
    out["version"] = value.get("version", 0)
    if "creation_date" in value:
        import capo_iot.types.timestamp

        out["creationDate"] = capo_iot.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "last_modified_date" in value:
        import capo_iot.types.timestamp

        out["lastModifiedDate"] = capo_iot.types.timestamp.serialize_json(
            value["last_modified_date"]
        )
    if "metrics_export_config" in value:
        import capo_iot.types.metrics_export_config

        out["metricsExportConfig"] = (
            capo_iot.types.metrics_export_config.serialize_json(
                value["metrics_export_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSecurityProfileResponse:
    out: UpdateSecurityProfileResponse = {}  # type: ignore[typeddict-item]
    if "securityProfileName" in data:
        out["security_profile_name"] = data["securityProfileName"]
    if "securityProfileArn" in data:
        out["security_profile_arn"] = data["securityProfileArn"]
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
    if "version" in data:
        out["version"] = data["version"]
    else:
        out["version"] = 0
    if "creationDate" in data:
        import capo_iot.types.timestamp

        out["creation_date"] = capo_iot.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    if "lastModifiedDate" in data:
        import capo_iot.types.timestamp

        out["last_modified_date"] = capo_iot.types.timestamp.deserialize_json(
            data["lastModifiedDate"]
        )
    if "metricsExportConfig" in data:
        import capo_iot.types.metrics_export_config

        out["metrics_export_config"] = (
            capo_iot.types.metrics_export_config.deserialize_json(
                data["metricsExportConfig"]
            )
        )
    return out
