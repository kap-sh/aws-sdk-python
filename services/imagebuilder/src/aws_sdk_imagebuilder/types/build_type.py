"""Generated from Smithy shape ``com.amazonaws.imagebuilder#BuildType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

BuildType: TypeAlias = Literal[
    "USER_INITIATED",
    "SCHEDULED",
    "IMPORT",
    "IMPORT_ISO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER_INITIATED",
        "SCHEDULED",
        "IMPORT",
        "IMPORT_ISO",
    )
)


def serialize_json(value: BuildType) -> str:
    return value


def deserialize_json(data: str) -> BuildType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BuildType value: {data!r}")
    return cast(BuildType, data)
