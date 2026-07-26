"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#EndpointType``."""

from typing import Literal, TypeAlias, cast

"""<p>Represents an endpoint type.</p>"""
EndpointType: TypeAlias = Literal[
    "REGIONAL",
    "EDGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointType) -> str:
    return value


def deserialize_json(data: str) -> EndpointType:
    return cast(EndpointType, data)
