"""Generated from Smithy shape ``com.amazonaws.mturk#ReviewActionStatus``."""

from typing import Literal, TypeAlias, cast

ReviewActionStatus: TypeAlias = Literal[
    "Intended",
    "Succeeded",
    "Failed",
    "Cancelled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReviewActionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReviewActionStatus:
    return cast(ReviewActionStatus, data)
