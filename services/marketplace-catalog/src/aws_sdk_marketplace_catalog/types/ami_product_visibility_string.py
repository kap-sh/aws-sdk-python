"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#AmiProductVisibilityString``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

AmiProductVisibilityString: TypeAlias = Literal[
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


def serialize_json(value: AmiProductVisibilityString) -> str:
    return value


def deserialize_json(data: str) -> AmiProductVisibilityString:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AmiProductVisibilityString value: {data!r}"
        )
    return cast(AmiProductVisibilityString, data)
