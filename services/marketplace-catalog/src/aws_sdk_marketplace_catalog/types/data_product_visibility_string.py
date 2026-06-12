"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#DataProductVisibilityString``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

DataProductVisibilityString: TypeAlias = Literal[
    "Limited",
    "Public",
    "Restricted",
    "Unavailable",
    "Draft",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Limited",
        "Public",
        "Restricted",
        "Unavailable",
        "Draft",
    )
)


def serialize_json(value: DataProductVisibilityString) -> str:
    return value


def deserialize_json(data: str) -> DataProductVisibilityString:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataProductVisibilityString value: {data!r}"
        )
    return cast(DataProductVisibilityString, data)
