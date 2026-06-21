"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#TryItState``."""

from typing import Literal, TypeAlias, cast

"""<p>Represents the try it state for a product REST endpoint page.</p>"""
TryItState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TryItState) -> str:
    return value


def deserialize_json(data: str) -> TryItState:
    return cast(TryItState, data)
