"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudWatchAlarmDimensionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_cloud_watch_alarm_dimensions_details

AwsCloudWatchAlarmDimensionsList: TypeAlias = list[
    "capo_securityhub.types.aws_cloud_watch_alarm_dimensions_details.AwsCloudWatchAlarmDimensionsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudWatchAlarmDimensionsList) -> list:
    import capo_securityhub.types.aws_cloud_watch_alarm_dimensions_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_cloud_watch_alarm_dimensions_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsCloudWatchAlarmDimensionsList:
    import capo_securityhub.types.aws_cloud_watch_alarm_dimensions_details

    out: AwsCloudWatchAlarmDimensionsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_cloud_watch_alarm_dimensions_details.deserialize_json(
                item
            )
        )
    return out
