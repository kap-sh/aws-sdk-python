"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#LoggingLevel``."""

from typing import Literal, TypeAlias, cast

"""<p>The logging level.</p>"""
LoggingLevel: TypeAlias = Literal[
    "ERROR",
    "INFO",
    "OFF",
]


# --- restJson1 ser/de ---
def serialize_json(value: LoggingLevel) -> str:
    return value


def deserialize_json(data: str) -> LoggingLevel:
    return cast(LoggingLevel, data)
