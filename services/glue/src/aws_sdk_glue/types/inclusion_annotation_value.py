"""Generated from Smithy shape ``com.amazonaws.glue#InclusionAnnotationValue``."""

from typing import Literal, TypeAlias, cast

InclusionAnnotationValue: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InclusionAnnotationValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InclusionAnnotationValue:
    return cast(InclusionAnnotationValue, data)
