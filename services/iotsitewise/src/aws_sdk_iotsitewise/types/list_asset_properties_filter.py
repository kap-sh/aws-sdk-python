"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssetPropertiesFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

ListAssetPropertiesFilter: TypeAlias = Literal[
    "ALL",
    "BASE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "BASE",
    )
)


def serialize_json(value: ListAssetPropertiesFilter) -> str:
    return value


def deserialize_json(data: str) -> ListAssetPropertiesFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListAssetPropertiesFilter value: {data!r}")
    return cast(ListAssetPropertiesFilter, data)
