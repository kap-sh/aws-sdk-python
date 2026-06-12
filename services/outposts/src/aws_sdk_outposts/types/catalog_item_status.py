"""Generated from Smithy shape ``com.amazonaws.outposts#CatalogItemStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

CatalogItemStatus: TypeAlias = Literal[
    "AVAILABLE",
    "DISCONTINUED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "DISCONTINUED",
    )
)


def serialize_json(value: CatalogItemStatus) -> str:
    return value


def deserialize_json(data: str) -> CatalogItemStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CatalogItemStatus value: {data!r}")
    return cast(CatalogItemStatus, data)
