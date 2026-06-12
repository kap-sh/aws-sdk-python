"""Generated from Smithy shape ``com.amazonaws.outposts#CatalogItemClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

CatalogItemClass: TypeAlias = Literal[
    "RACK",
    "SERVER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RACK",
        "SERVER",
    )
)


def serialize_json(value: CatalogItemClass) -> str:
    return value


def deserialize_json(data: str) -> CatalogItemClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CatalogItemClass value: {data!r}")
    return cast(CatalogItemClass, data)
