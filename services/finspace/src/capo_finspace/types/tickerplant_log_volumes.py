"""Generated from Smithy shape ``com.amazonaws.finspace#TickerplantLogVolumes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace.types.volume_name

TickerplantLogVolumes: TypeAlias = list["capo_finspace.types.volume_name.VolumeName"]


# --- restJson1 ser/de ---
def serialize_json(value: TickerplantLogVolumes) -> list:
    return list(value)


def deserialize_json(data: list) -> TickerplantLogVolumes:
    return list(data)
