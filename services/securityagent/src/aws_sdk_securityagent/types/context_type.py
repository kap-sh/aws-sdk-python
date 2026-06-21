"""Generated from Smithy shape ``com.amazonaws.securityagent#ContextType``."""

from typing import Literal, TypeAlias, cast

"""<p>Category of execution context.</p>"""
ContextType: TypeAlias = Literal[
    "ERROR",
    "CLIENT_ERROR",
    "WARNING",
    "INFO",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContextType) -> str:
    return value


def deserialize_json(data: str) -> ContextType:
    return cast(ContextType, data)
