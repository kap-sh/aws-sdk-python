"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DailyVolumes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.daily_volume

DailyVolumes: TypeAlias = list["aws_sdk_pinpoint_email.types.daily_volume.DailyVolume"]


# --- restJson1 ser/de ---
def serialize_json(value: DailyVolumes) -> list:
    import aws_sdk_pinpoint_email.types.daily_volume

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint_email.types.daily_volume.serialize_json(item))
    return out


def deserialize_json(data: list) -> DailyVolumes:
    import aws_sdk_pinpoint_email.types.daily_volume

    out: DailyVolumes = []
    for item in data:
        out.append(aws_sdk_pinpoint_email.types.daily_volume.deserialize_json(item))
    return out
