"""Generated from Smithy shape ``com.amazonaws.securityagent#RiskLevel``."""

from typing import Literal, TypeAlias, cast

"""<p>Risk severity level.</p>"""
RiskLevel: TypeAlias = Literal[
    "UNKNOWN",
    "INFORMATIONAL",
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: RiskLevel) -> str:
    return value


def deserialize_json(data: str) -> RiskLevel:
    return cast(RiskLevel, data)
