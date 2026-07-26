"""Generated from Smithy shape ``com.amazonaws.rekognition#QualityFilter``."""

from typing import Literal, TypeAlias, cast

QualityFilter: TypeAlias = Literal[
    "NONE",
    "AUTO",
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QualityFilter) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QualityFilter:
    return cast(QualityFilter, data)
