"""Generated from Smithy shape ``com.amazonaws.ssm#ReviewStatus``."""

from typing import Literal, TypeAlias, cast

ReviewStatus: TypeAlias = Literal[
    "APPROVED",
    "NOT_REVIEWED",
    "PENDING",
    "REJECTED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReviewStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReviewStatus:
    return cast(ReviewStatus, data)
