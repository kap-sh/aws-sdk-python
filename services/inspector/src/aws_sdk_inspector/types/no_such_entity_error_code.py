"""Generated from Smithy shape ``com.amazonaws.inspector#NoSuchEntityErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "ASSESSMENT_TARGET_DOES_NOT_EXIST",
        "ASSESSMENT_TEMPLATE_DOES_NOT_EXIST",
        "ASSESSMENT_RUN_DOES_NOT_EXIST",
        "FINDING_DOES_NOT_EXIST",
        "RESOURCE_GROUP_DOES_NOT_EXIST",
        "RULES_PACKAGE_DOES_NOT_EXIST",
        "SNS_TOPIC_DOES_NOT_EXIST",
        "IAM_ROLE_DOES_NOT_EXIST",
    )
)


def serialize_aws_json_1_1(value: NoSuchEntityErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NoSuchEntityErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NoSuchEntityErrorCode value: {data!r}")
    return cast(NoSuchEntityErrorCode, data)
