"""Generated from Smithy shape ``com.amazonaws.mturk#ReviewPolicyLevel``."""

from typing import Literal, TypeAlias, cast

ReviewPolicyLevel: TypeAlias = Literal[
    "Assignment",
    "HIT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReviewPolicyLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReviewPolicyLevel:
    return cast(ReviewPolicyLevel, data)
