"""Generated from Smithy shape ``com.amazonaws.inspector#LimitExceededErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector.errors import DeserializationError

LimitExceededErrorCode: TypeAlias = Literal[
    "ASSESSMENT_TARGET_LIMIT_EXCEEDED",
    "ASSESSMENT_TEMPLATE_LIMIT_EXCEEDED",
    "ASSESSMENT_RUN_LIMIT_EXCEEDED",
    "RESOURCE_GROUP_LIMIT_EXCEEDED",
    "EVENT_SUBSCRIPTION_LIMIT_EXCEEDED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSESSMENT_TARGET_LIMIT_EXCEEDED",
        "ASSESSMENT_TEMPLATE_LIMIT_EXCEEDED",
        "ASSESSMENT_RUN_LIMIT_EXCEEDED",
        "RESOURCE_GROUP_LIMIT_EXCEEDED",
        "EVENT_SUBSCRIPTION_LIMIT_EXCEEDED",
    )
)


def serialize_aws_json_1_1(value: LimitExceededErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LimitExceededErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LimitExceededErrorCode value: {data!r}")
    return cast(LimitExceededErrorCode, data)
