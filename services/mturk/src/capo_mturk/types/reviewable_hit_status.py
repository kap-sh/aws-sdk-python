"""Generated from Smithy shape ``com.amazonaws.mturk#ReviewableHITStatus``."""

from typing import Literal, TypeAlias, cast

ReviewableHITStatus: TypeAlias = Literal[
    "Reviewable",
    "Reviewing",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReviewableHITStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReviewableHITStatus:
    return cast(ReviewableHITStatus, data)
