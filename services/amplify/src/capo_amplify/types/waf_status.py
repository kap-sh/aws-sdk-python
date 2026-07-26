"""Generated from Smithy shape ``com.amazonaws.amplify#WafStatus``."""

from typing import Literal, TypeAlias, cast

WafStatus: TypeAlias = Literal[
    "ASSOCIATING",
    "ASSOCIATION_FAILED",
    "ASSOCIATION_SUCCESS",
    "DISASSOCIATING",
    "DISASSOCIATION_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: WafStatus) -> str:
    return value


def deserialize_json(data: str) -> WafStatus:
    return cast(WafStatus, data)
