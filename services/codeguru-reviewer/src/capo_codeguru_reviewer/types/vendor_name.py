"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#VendorName``."""

from typing import Literal, TypeAlias, cast

VendorName: TypeAlias = Literal[
    "GitHub",
    "GitLab",
    "NativeS3",
]


# --- restJson1 ser/de ---
def serialize_json(value: VendorName) -> str:
    return value


def deserialize_json(data: str) -> VendorName:
    return cast(VendorName, data)
