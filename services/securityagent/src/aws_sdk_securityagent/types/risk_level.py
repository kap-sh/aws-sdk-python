"""Generated from Smithy shape ``com.amazonaws.securityagent#RiskLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "UNKNOWN",
        "INFORMATIONAL",
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL",
    )
)


def serialize_json(value: RiskLevel) -> str:
    return value


def deserialize_json(data: str) -> RiskLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RiskLevel value: {data!r}")
    return cast(RiskLevel, data)
