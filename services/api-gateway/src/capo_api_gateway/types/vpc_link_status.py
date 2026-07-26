"""Generated from Smithy shape ``com.amazonaws.apigateway#VpcLinkStatus``."""

from typing import Literal, TypeAlias, cast

VpcLinkStatus: TypeAlias = Literal[
    "AVAILABLE",
    "PENDING",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: VpcLinkStatus) -> str:
    return value


def deserialize_json(data: str) -> VpcLinkStatus:
    return cast(VpcLinkStatus, data)
