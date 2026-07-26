"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfCloudWatchAlarmTemplateSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.cloud_watch_alarm_template_summary

__listOfCloudWatchAlarmTemplateSummary: TypeAlias = list[
    "capo_medialive.types.cloud_watch_alarm_template_summary.CloudWatchAlarmTemplateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCloudWatchAlarmTemplateSummary) -> list:
    import capo_medialive.types.cloud_watch_alarm_template_summary

    out: list = []
    for item in value:
        out.append(
            capo_medialive.types.cloud_watch_alarm_template_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfCloudWatchAlarmTemplateSummary:
    import capo_medialive.types.cloud_watch_alarm_template_summary

    out: __listOfCloudWatchAlarmTemplateSummary = []
    for item in data:
        out.append(
            capo_medialive.types.cloud_watch_alarm_template_summary.deserialize_json(
                item
            )
        )
    return out
