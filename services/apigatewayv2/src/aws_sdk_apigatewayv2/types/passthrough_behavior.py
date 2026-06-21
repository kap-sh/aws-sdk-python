"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#PassthroughBehavior``."""

from typing import Literal, TypeAlias, cast

"""<p>Represents passthrough behavior for an integration response. Supported only for WebSocket APIs.</p>"""
PassthroughBehavior: TypeAlias = Literal[
    "WHEN_NO_MATCH",
    "NEVER",
    "WHEN_NO_TEMPLATES",
]


# --- restJson1 ser/de ---
def serialize_json(value: PassthroughBehavior) -> str:
    return value


def deserialize_json(data: str) -> PassthroughBehavior:
    return cast(PassthroughBehavior, data)
