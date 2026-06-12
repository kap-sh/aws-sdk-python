"""Generated from Smithy shape ``com.amazonaws.medialive#H264SceneChangeDetect``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H264 Scene Change Detect"""
H264SceneChangeDetect: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: H264SceneChangeDetect) -> str:
    return value


def deserialize_json(data: str) -> H264SceneChangeDetect:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264SceneChangeDetect value: {data!r}")
    return cast(H264SceneChangeDetect, data)
