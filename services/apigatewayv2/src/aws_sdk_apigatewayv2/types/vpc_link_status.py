"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#VpcLinkStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of the VPC link.</p>"""
VpcLinkStatus: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "DELETING",
    "FAILED",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: VpcLinkStatus) -> str:
    return value


def deserialize_json(data: str) -> VpcLinkStatus:
    return cast(VpcLinkStatus, data)
