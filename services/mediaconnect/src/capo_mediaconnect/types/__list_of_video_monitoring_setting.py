"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfVideoMonitoringSetting``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.video_monitoring_setting

__listOfVideoMonitoringSetting: TypeAlias = list[
    "capo_mediaconnect.types.video_monitoring_setting.VideoMonitoringSetting"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfVideoMonitoringSetting) -> list:
    import capo_mediaconnect.types.video_monitoring_setting

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.video_monitoring_setting.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfVideoMonitoringSetting:
    import capo_mediaconnect.types.video_monitoring_setting

    out: __listOfVideoMonitoringSetting = []
    for item in data:
        out.append(
            capo_mediaconnect.types.video_monitoring_setting.deserialize_json(item)
        )
    return out
