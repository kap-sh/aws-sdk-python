"""Generated from Smithy shape ``com.amazonaws.dlm#LocationValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dlm.errors import DeserializationError

LocationValues: TypeAlias = Literal[
    "CLOUD",
    "OUTPOST_LOCAL",
    "LOCAL_ZONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLOUD",
        "OUTPOST_LOCAL",
        "LOCAL_ZONE",
    )
)


def serialize_json(value: LocationValues) -> str:
    return value


def deserialize_json(data: str) -> LocationValues:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LocationValues value: {data!r}")
    return cast(LocationValues, data)
