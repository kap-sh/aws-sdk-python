"""Generated from Smithy shape ``com.amazonaws.pi#Severity``."""

from typing import Literal, TypeAlias, cast

Severity: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Severity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Severity:
    return cast(Severity, data)
