"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#RealTimeAlertConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.boolean
    import aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_rule_list


class RealTimeAlertConfiguration(TypedDict, closed=True):
    disabled: "aws_sdk_chime_sdk_media_pipelines.types.boolean.Boolean"
    """<p>Turns off real-time alerts.</p>"""
    rules: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_rule_list.RealTimeAlertRuleList"
    ]
    """<p>The rules in the alert. Rules specify the words or phrases that you want to be notified about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeAlertConfiguration) -> dict:
    out: dict = {}
    out["Disabled"] = value.get("disabled", False)
    if "rules" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_rule_list

        out["Rules"] = (
            aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_rule_list.serialize_json(
                value["rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> RealTimeAlertConfiguration:
    out: RealTimeAlertConfiguration = {}  # type: ignore[typeddict-item]
    if "Disabled" in data:
        out["disabled"] = data["Disabled"]
    else:
        out["disabled"] = False
    if "Rules" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_rule_list

        out["rules"] = (
            aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_rule_list.deserialize_json(
                data["Rules"]
            )
        )
    return out
