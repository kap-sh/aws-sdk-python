"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentReviewAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

DocumentReviewAction: TypeAlias = Literal[
    "SendForReview",
    "UpdateReview",
    "Approve",
    "Reject",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SendForReview",
        "UpdateReview",
        "Approve",
        "Reject",
    )
)


def serialize_aws_json_1_1(value: DocumentReviewAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentReviewAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentReviewAction value: {data!r}")
    return cast(DocumentReviewAction, data)
