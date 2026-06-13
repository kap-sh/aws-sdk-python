"""Generated from Smithy shape ``com.amazonaws.mgn#WaveIDsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.wave_id

WaveIDsFilter: TypeAlias = list["aws_sdk_mgn.types.wave_id.WaveID"]


# --- restJson1 ser/de ---
def serialize_json(value: WaveIDsFilter) -> list:
    return list(value)


def deserialize_json(data: list) -> WaveIDsFilter:
    return list(data)
