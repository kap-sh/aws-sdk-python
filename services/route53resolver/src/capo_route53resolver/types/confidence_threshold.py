"""Generated from Smithy shape ``com.amazonaws.route53resolver#ConfidenceThreshold``."""

from typing import Literal, TypeAlias, cast

ConfidenceThreshold: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfidenceThreshold) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfidenceThreshold:
    return cast(ConfidenceThreshold, data)
