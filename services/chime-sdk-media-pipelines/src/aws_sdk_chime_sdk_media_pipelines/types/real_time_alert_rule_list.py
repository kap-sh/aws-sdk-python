"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#RealTimeAlertRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_rule

RealTimeAlertRuleList: TypeAlias = list[
    "aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_rule.RealTimeAlertRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeAlertRuleList) -> list:
    import aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_rule.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RealTimeAlertRuleList:
    import aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_rule

    out: RealTimeAlertRuleList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_rule.deserialize_json(
                item
            )
        )
    return out
