"""Generated from Smithy shape ``com.amazonaws.mturk#HITReviewStatus``."""

from typing import Literal, TypeAlias, cast

HITReviewStatus: TypeAlias = Literal[
    "NotReviewed",
    "MarkedForReview",
    "ReviewedAppropriate",
    "ReviewedInappropriate",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HITReviewStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HITReviewStatus:
    return cast(HITReviewStatus, data)
