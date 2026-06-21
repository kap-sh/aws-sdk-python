"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ConfidenceThreshold``."""

from typing import Literal, TypeAlias, cast

ConfidenceThreshold: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfidenceThreshold) -> str:
    return value


def deserialize_json(data: str) -> ConfidenceThreshold:
    return cast(ConfidenceThreshold, data)
