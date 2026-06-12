"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfCloudWatchAlarmTemplateGroupSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.cloud_watch_alarm_template_group_summary

__listOfCloudWatchAlarmTemplateGroupSummary: TypeAlias = list[
    "aws_sdk_medialive.types.cloud_watch_alarm_template_group_summary.CloudWatchAlarmTemplateGroupSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCloudWatchAlarmTemplateGroupSummary) -> list:
    import aws_sdk_medialive.types.cloud_watch_alarm_template_group_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.cloud_watch_alarm_template_group_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfCloudWatchAlarmTemplateGroupSummary:
    import aws_sdk_medialive.types.cloud_watch_alarm_template_group_summary

    out: __listOfCloudWatchAlarmTemplateGroupSummary = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.cloud_watch_alarm_template_group_summary.deserialize_json(
                item
            )
        )
    return out
