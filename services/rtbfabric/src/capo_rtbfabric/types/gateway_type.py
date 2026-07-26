"""Generated from Smithy shape ``com.amazonaws.rtbfabric#GatewayType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of gateway.</p>"""
GatewayType: TypeAlias = Literal[
    "EXTERNAL",
    "INTERNAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayType) -> str:
    return value


def deserialize_json(data: str) -> GatewayType:
    return cast(GatewayType, data)
