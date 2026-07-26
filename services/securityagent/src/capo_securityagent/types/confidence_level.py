"""Generated from Smithy shape ``com.amazonaws.securityagent#ConfidenceLevel``."""

from typing import Literal, TypeAlias, cast

"""<p>Finding confidence level.</p>"""
ConfidenceLevel: TypeAlias = Literal[
    "FALSE_POSITIVE",
    "UNCONFIRMED",
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfidenceLevel) -> str:
    return value


def deserialize_json(data: str) -> ConfidenceLevel:
    return cast(ConfidenceLevel, data)
