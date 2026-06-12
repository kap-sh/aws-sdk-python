"""Generated from Smithy shape ``com.amazonaws.dlm#ResourceLocationValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dlm.errors import DeserializationError

ResourceLocationValues: TypeAlias = Literal[
    "CLOUD",
    "OUTPOST",
    "LOCAL_ZONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLOUD",
        "OUTPOST",
        "LOCAL_ZONE",
    )
)


def serialize_json(value: ResourceLocationValues) -> str:
    return value


def deserialize_json(data: str) -> ResourceLocationValues:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceLocationValues value: {data!r}")
    return cast(ResourceLocationValues, data)
