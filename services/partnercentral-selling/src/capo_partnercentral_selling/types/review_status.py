"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ReviewStatus``."""

from typing import Literal, TypeAlias, cast

ReviewStatus: TypeAlias = Literal[
    "Pending Submission",
    "Submitted",
    "In review",
    "Approved",
    "Rejected",
    "Action Required",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReviewStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ReviewStatus:
    return cast(ReviewStatus, data)
