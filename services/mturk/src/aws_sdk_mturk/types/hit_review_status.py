"""Generated from Smithy shape ``com.amazonaws.mturk#HITReviewStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mturk.errors import DeserializationError

HITReviewStatus: TypeAlias = Literal[
    "NotReviewed",
    "MarkedForReview",
    "ReviewedAppropriate",
    "ReviewedInappropriate",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NotReviewed",
        "MarkedForReview",
        "ReviewedAppropriate",
        "ReviewedInappropriate",
    )
)


def serialize_aws_json_1_1(value: HITReviewStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HITReviewStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HITReviewStatus value: {data!r}")
    return cast(HITReviewStatus, data)
