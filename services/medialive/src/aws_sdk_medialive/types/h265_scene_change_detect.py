"""Generated from Smithy shape ``com.amazonaws.medialive#H265SceneChangeDetect``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H265 Scene Change Detect"""
H265SceneChangeDetect: TypeAlias = Literal[
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


def serialize_json(value: H265SceneChangeDetect) -> str:
    return value


def deserialize_json(data: str) -> H265SceneChangeDetect:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265SceneChangeDetect value: {data!r}")
    return cast(H265SceneChangeDetect, data)
