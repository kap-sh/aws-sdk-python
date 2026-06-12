"""Generated from Smithy shape ``com.amazonaws.greengrassv2#VendorGuidance``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

VendorGuidance: TypeAlias = Literal[
    "ACTIVE",
    "DISCONTINUED",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DISCONTINUED",
        "DELETED",
    )
)


def serialize_json(value: VendorGuidance) -> str:
    return value


def deserialize_json(data: str) -> VendorGuidance:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VendorGuidance value: {data!r}")
    return cast(VendorGuidance, data)
