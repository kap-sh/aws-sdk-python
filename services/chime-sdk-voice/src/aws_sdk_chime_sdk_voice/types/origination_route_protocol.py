"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#OriginationRouteProtocol``."""

from typing import Literal, TypeAlias, cast

OriginationRouteProtocol: TypeAlias = Literal[
    "TCP",
    "UDP",
]


# --- restJson1 ser/de ---
def serialize_json(value: OriginationRouteProtocol) -> str:
    return value


def deserialize_json(data: str) -> OriginationRouteProtocol:
    return cast(OriginationRouteProtocol, data)
