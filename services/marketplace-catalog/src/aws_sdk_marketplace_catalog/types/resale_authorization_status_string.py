"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationStatusString``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

ResaleAuthorizationStatusString: TypeAlias = Literal[
    "Draft",
    "Active",
    "Restricted",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Draft",
        "Active",
        "Restricted",
    )
)


def serialize_json(value: ResaleAuthorizationStatusString) -> str:
    return value


def deserialize_json(data: str) -> ResaleAuthorizationStatusString:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResaleAuthorizationStatusString value: {data!r}"
        )
    return cast(ResaleAuthorizationStatusString, data)
