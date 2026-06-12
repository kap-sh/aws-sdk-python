"""Generated from Smithy shape ``com.amazonaws.mturk#EventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mturk.errors import DeserializationError

EventType: TypeAlias = Literal[
    "AssignmentAccepted",
    "AssignmentAbandoned",
    "AssignmentReturned",
    "AssignmentSubmitted",
    "AssignmentRejected",
    "AssignmentApproved",
    "HITCreated",
    "HITExpired",
    "HITReviewable",
    "HITExtended",
    "HITDisposed",
    "Ping",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AssignmentAccepted",
        "AssignmentAbandoned",
        "AssignmentReturned",
        "AssignmentSubmitted",
        "AssignmentRejected",
        "AssignmentApproved",
        "HITCreated",
        "HITExpired",
        "HITReviewable",
        "HITExtended",
        "HITDisposed",
        "Ping",
    )
)


def serialize_aws_json_1_1(value: EventType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventType value: {data!r}")
    return cast(EventType, data)
