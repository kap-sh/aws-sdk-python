"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceCodec``."""

from typing import Literal, TypeAlias, cast

"""The codec to use on the video that the device produces."""
InputDeviceCodec: TypeAlias = Literal[
    "HEVC",
    "AVC",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputDeviceCodec) -> str:
    return value


def deserialize_json(data: str) -> InputDeviceCodec:
    return cast(InputDeviceCodec, data)
