"""Generated from Smithy shape ``com.amazonaws.dlm#ResourceTypeValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dlm.errors import DeserializationError

ResourceTypeValues: TypeAlias = Literal[
    "VOLUME",
    "INSTANCE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VOLUME",
        "INSTANCE",
    )
)


def serialize_json(value: ResourceTypeValues) -> str:
    return value


def deserialize_json(data: str) -> ResourceTypeValues:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceTypeValues value: {data!r}")
    return cast(ResourceTypeValues, data)
