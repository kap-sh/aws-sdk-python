"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#Status``."""

from typing import Literal, TypeAlias, cast

"""<p>The status.</p>"""
Status: TypeAlias = Literal[
    "AVAILABLE",
    "IN_PROGRESS",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
