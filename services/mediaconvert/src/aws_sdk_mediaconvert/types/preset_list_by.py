"""Generated from Smithy shape ``com.amazonaws.mediaconvert#PresetListBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Optional. When you request a list of presets, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don't specify, the service will list them by name."""
PresetListBy: TypeAlias = Literal[
    "NAME",
    "CREATION_DATE",
    "SYSTEM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAME",
        "CREATION_DATE",
        "SYSTEM",
    )
)


def serialize_json(value: PresetListBy) -> str:
    return value


def deserialize_json(data: str) -> PresetListBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PresetListBy value: {data!r}")
    return cast(PresetListBy, data)
