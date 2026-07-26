"""Generated from Smithy shape ``com.amazonaws.greengrassv2#VendorGuidance``."""

from typing import Literal, TypeAlias, cast

VendorGuidance: TypeAlias = Literal[
    "ACTIVE",
    "DISCONTINUED",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: VendorGuidance) -> str:
    return value


def deserialize_json(data: str) -> VendorGuidance:
    return cast(VendorGuidance, data)
