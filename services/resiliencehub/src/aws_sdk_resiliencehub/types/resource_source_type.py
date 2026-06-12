"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

ResourceSourceType: TypeAlias = Literal[
    "AppTemplate",
    "Discovered",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AppTemplate",
        "Discovered",
    )
)


def serialize_json(value: ResourceSourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceSourceType value: {data!r}")
    return cast(ResourceSourceType, data)
