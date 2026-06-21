"""Generated from Smithy shape ``com.amazonaws.codeartifact#EndpointType``."""

from typing import Literal, TypeAlias, cast

EndpointType: TypeAlias = Literal[
    "dualstack",
    "ipv4",
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointType) -> str:
    return value


def deserialize_json(data: str) -> EndpointType:
    return cast(EndpointType, data)
