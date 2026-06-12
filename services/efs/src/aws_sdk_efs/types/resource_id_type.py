"""Generated from Smithy shape ``com.amazonaws.efs#ResourceIdType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_efs.errors import DeserializationError

"""A preference indicating a choice to use 63bit/32bit IDs for all applicable resources."""
ResourceIdType: TypeAlias = Literal[
    "LONG_ID",
    "SHORT_ID",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LONG_ID",
        "SHORT_ID",
    )
)


def serialize_json(value: ResourceIdType) -> str:
    return value


def deserialize_json(data: str) -> ResourceIdType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceIdType value: {data!r}")
    return cast(ResourceIdType, data)
