"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DailyVolumes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_email.types.daily_volume

DailyVolumes: TypeAlias = list["capo_pinpoint_email.types.daily_volume.DailyVolume"]


# --- restJson1 ser/de ---
def serialize_json(value: DailyVolumes) -> list:
    import capo_pinpoint_email.types.daily_volume

    out: list = []
    for item in value:
        out.append(capo_pinpoint_email.types.daily_volume.serialize_json(item))
    return out


def deserialize_json(data: list) -> DailyVolumes:
    import capo_pinpoint_email.types.daily_volume

    out: DailyVolumes = []
    for item in data:
        out.append(capo_pinpoint_email.types.daily_volume.deserialize_json(item))
    return out
