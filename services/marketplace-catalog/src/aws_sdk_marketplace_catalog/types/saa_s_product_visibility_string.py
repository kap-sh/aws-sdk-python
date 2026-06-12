"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SaaSProductVisibilityString``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

SaaSProductVisibilityString: TypeAlias = Literal[
    "Limited",
    "Public",
    "Restricted",
    "Draft",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Limited",
        "Public",
        "Restricted",
        "Draft",
    )
)


def serialize_json(value: SaaSProductVisibilityString) -> str:
    return value


def deserialize_json(data: str) -> SaaSProductVisibilityString:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SaaSProductVisibilityString value: {data!r}"
        )
    return cast(SaaSProductVisibilityString, data)
