"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssetModelPropertiesFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

ListAssetModelPropertiesFilter: TypeAlias = Literal[
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


def serialize_json(value: ListAssetModelPropertiesFilter) -> str:
    return value


def deserialize_json(data: str) -> ListAssetModelPropertiesFilter:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListAssetModelPropertiesFilter value: {data!r}"
        )
    return cast(ListAssetModelPropertiesFilter, data)
