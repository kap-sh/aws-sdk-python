"""Generated from Smithy shape ``com.amazonaws.apigateway#EndpointAccessMode``."""

from typing import Literal, TypeAlias, cast

EndpointAccessMode: TypeAlias = Literal[
    "BASIC",
    "STRICT",
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointAccessMode) -> str:
    return value


def deserialize_json(data: str) -> EndpointAccessMode:
    return cast(EndpointAccessMode, data)
