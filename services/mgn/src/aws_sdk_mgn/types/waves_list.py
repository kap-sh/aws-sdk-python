"""Generated from Smithy shape ``com.amazonaws.mgn#WavesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.wave

WavesList: TypeAlias = list["aws_sdk_mgn.types.wave.Wave"]


# --- restJson1 ser/de ---
def serialize_json(value: WavesList) -> list:
    import aws_sdk_mgn.types.wave

    out: list = []
    for item in value:
        out.append(aws_sdk_mgn.types.wave.serialize_json(item))
    return out


def deserialize_json(data: list) -> WavesList:
    import aws_sdk_mgn.types.wave

    out: WavesList = []
    for item in data:
        out.append(aws_sdk_mgn.types.wave.deserialize_json(item))
    return out
