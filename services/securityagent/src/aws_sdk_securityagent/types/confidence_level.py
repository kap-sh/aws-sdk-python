"""Generated from Smithy shape ``com.amazonaws.securityagent#ConfidenceLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Finding confidence level.</p>"""
ConfidenceLevel: TypeAlias = Literal[
    "FALSE_POSITIVE",
    "UNCONFIRMED",
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FALSE_POSITIVE",
        "UNCONFIRMED",
        "LOW",
        "MEDIUM",
        "HIGH",
    )
)


def serialize_json(value: ConfidenceLevel) -> str:
    return value


def deserialize_json(data: str) -> ConfidenceLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfidenceLevel value: {data!r}")
    return cast(ConfidenceLevel, data)
