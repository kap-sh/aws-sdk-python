"""Generated from Smithy shape ``com.amazonaws.securityhub#SortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

SortOrder: TypeAlias = Literal[
    "asc",
    "desc",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "asc",
        "desc",
    )
)


def serialize_json(value: SortOrder) -> str:
    return value


def deserialize_json(data: str) -> SortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortOrder value: {data!r}")
    return cast(SortOrder, data)
