"""Generated from Smithy shape ``com.amazonaws.osis#VpcEndpointManagement``."""

from typing import Literal, TypeAlias, cast

VpcEndpointManagement: TypeAlias = Literal[
    "CUSTOMER",
    "SERVICE",
]


# --- restJson1 ser/de ---
def serialize_json(value: VpcEndpointManagement) -> str:
    return value


def deserialize_json(data: str) -> VpcEndpointManagement:
    return cast(VpcEndpointManagement, data)
