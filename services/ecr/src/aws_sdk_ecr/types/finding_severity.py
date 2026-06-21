"""Generated from Smithy shape ``com.amazonaws.ecr#FindingSeverity``."""

from typing import Literal, TypeAlias, cast

FindingSeverity: TypeAlias = Literal[
    "INFORMATIONAL",
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL",
    "UNDEFINED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FindingSeverity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FindingSeverity:
    return cast(FindingSeverity, data)
