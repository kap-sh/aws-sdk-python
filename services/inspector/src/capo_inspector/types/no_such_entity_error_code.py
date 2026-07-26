"""Generated from Smithy shape ``com.amazonaws.inspector#NoSuchEntityErrorCode``."""

from typing import Literal, TypeAlias, cast

NoSuchEntityErrorCode: TypeAlias = Literal[
    "ASSESSMENT_TARGET_DOES_NOT_EXIST",
    "ASSESSMENT_TEMPLATE_DOES_NOT_EXIST",
    "ASSESSMENT_RUN_DOES_NOT_EXIST",
    "FINDING_DOES_NOT_EXIST",
    "RESOURCE_GROUP_DOES_NOT_EXIST",
    "RULES_PACKAGE_DOES_NOT_EXIST",
    "SNS_TOPIC_DOES_NOT_EXIST",
    "IAM_ROLE_DOES_NOT_EXIST",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NoSuchEntityErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NoSuchEntityErrorCode:
    return cast(NoSuchEntityErrorCode, data)
