"""Generated from Smithy shape ``com.amazonaws.inspector#AccessDeniedErrorCode``."""

from typing import Literal, TypeAlias, cast

AccessDeniedErrorCode: TypeAlias = Literal[
    "ACCESS_DENIED_TO_ASSESSMENT_TARGET",
    "ACCESS_DENIED_TO_ASSESSMENT_TEMPLATE",
    "ACCESS_DENIED_TO_ASSESSMENT_RUN",
    "ACCESS_DENIED_TO_FINDING",
    "ACCESS_DENIED_TO_RESOURCE_GROUP",
    "ACCESS_DENIED_TO_RULES_PACKAGE",
    "ACCESS_DENIED_TO_SNS_TOPIC",
    "ACCESS_DENIED_TO_IAM_ROLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessDeniedErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessDeniedErrorCode:
    return cast(AccessDeniedErrorCode, data)
