"""Generated from Smithy shape ``com.amazonaws.finspace#KxNAS1Type``."""

from typing import Literal, TypeAlias, cast

KxNAS1Type: TypeAlias = Literal[
    "SSD_1000",
    "SSD_250",
    "HDD_12",
]


# --- restJson1 ser/de ---
def serialize_json(value: KxNAS1Type) -> str:
    return value


def deserialize_json(data: str) -> KxNAS1Type:
    return cast(KxNAS1Type, data)
