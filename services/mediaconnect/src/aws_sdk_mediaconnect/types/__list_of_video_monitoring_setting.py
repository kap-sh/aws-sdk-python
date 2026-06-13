"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfVideoMonitoringSetting``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.video_monitoring_setting

__listOfVideoMonitoringSetting: TypeAlias = list[
    "aws_sdk_mediaconnect.types.video_monitoring_setting.VideoMonitoringSetting"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfVideoMonitoringSetting) -> list:
    import aws_sdk_mediaconnect.types.video_monitoring_setting

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconnect.types.video_monitoring_setting.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfVideoMonitoringSetting:
    import aws_sdk_mediaconnect.types.video_monitoring_setting

    out: __listOfVideoMonitoringSetting = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.video_monitoring_setting.deserialize_json(item)
        )
    return out
