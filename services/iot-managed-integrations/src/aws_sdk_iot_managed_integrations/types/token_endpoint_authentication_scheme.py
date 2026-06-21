"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#TokenEndpointAuthenticationScheme``."""

from typing import Literal, TypeAlias, cast

TokenEndpointAuthenticationScheme: TypeAlias = Literal[
    "HTTP_BASIC",
    "REQUEST_BODY_CREDENTIALS",
]


# --- restJson1 ser/de ---
def serialize_json(value: TokenEndpointAuthenticationScheme) -> str:
    return value


def deserialize_json(data: str) -> TokenEndpointAuthenticationScheme:
    return cast(TokenEndpointAuthenticationScheme, data)
