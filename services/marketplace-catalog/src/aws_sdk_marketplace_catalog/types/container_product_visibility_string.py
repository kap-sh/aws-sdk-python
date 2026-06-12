"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ContainerProductVisibilityString``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

ContainerProductVisibilityString: TypeAlias = Literal[
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


def serialize_json(value: ContainerProductVisibilityString) -> str:
    return value


def deserialize_json(data: str) -> ContainerProductVisibilityString:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ContainerProductVisibilityString value: {data!r}"
        )
    return cast(ContainerProductVisibilityString, data)
