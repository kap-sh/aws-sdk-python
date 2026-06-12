"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceCodec``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The codec to use on the video that the device produces."""
InputDeviceCodec: TypeAlias = Literal[
    "HEVC",
    "AVC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEVC",
        "AVC",
    )
)


def serialize_json(value: InputDeviceCodec) -> str:
    return value


def deserialize_json(data: str) -> InputDeviceCodec:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputDeviceCodec value: {data!r}")
    return cast(InputDeviceCodec, data)
