"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentRunNotificationSnsStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector.errors import DeserializationError

AssessmentRunNotificationSnsStatusCode: TypeAlias = Literal[
    "SUCCESS",
    "TOPIC_DOES_NOT_EXIST",
    "ACCESS_DENIED",
    "INTERNAL_ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS",
        "TOPIC_DOES_NOT_EXIST",
        "ACCESS_DENIED",
        "INTERNAL_ERROR",
    )
)


def serialize_aws_json_1_1(value: AssessmentRunNotificationSnsStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssessmentRunNotificationSnsStatusCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AssessmentRunNotificationSnsStatusCode value: {data!r}"
        )
    return cast(AssessmentRunNotificationSnsStatusCode, data)
