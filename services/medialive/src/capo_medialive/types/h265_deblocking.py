"""Generated from Smithy shape ``com.amazonaws.medialive#H265Deblocking``."""

from typing import Literal, TypeAlias, cast

"""H265 Deblocking"""
H265Deblocking: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265Deblocking) -> str:
    return value


def deserialize_json(data: str) -> H265Deblocking:
    return cast(H265Deblocking, data)
