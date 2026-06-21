"""Generated from Smithy shape ``com.amazonaws.inspector#LimitExceededErrorCode``."""

from typing import Literal, TypeAlias, cast

LimitExceededErrorCode: TypeAlias = Literal[
    "ASSESSMENT_TARGET_LIMIT_EXCEEDED",
    "ASSESSMENT_TEMPLATE_LIMIT_EXCEEDED",
    "ASSESSMENT_RUN_LIMIT_EXCEEDED",
    "RESOURCE_GROUP_LIMIT_EXCEEDED",
    "EVENT_SUBSCRIPTION_LIMIT_EXCEEDED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LimitExceededErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LimitExceededErrorCode:
    return cast(LimitExceededErrorCode, data)
