"""Generated from Smithy shape ``com.amazonaws.datazone#ListingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

ListingStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_json(value: ListingStatus) -> str:
    return value


def deserialize_json(data: str) -> ListingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListingStatus value: {data!r}")
    return cast(ListingStatus, data)
