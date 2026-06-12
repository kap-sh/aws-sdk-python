"""Generated from Smithy shape ``com.amazonaws.codebuild#WebhookFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

WebhookFilterType: TypeAlias = Literal[
    "EVENT",
    "BASE_REF",
    "HEAD_REF",
    "ACTOR_ACCOUNT_ID",
    "FILE_PATH",
    "COMMIT_MESSAGE",
    "WORKFLOW_NAME",
    "TAG_NAME",
    "RELEASE_NAME",
    "REPOSITORY_NAME",
    "ORGANIZATION_NAME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EVENT",
        "BASE_REF",
        "HEAD_REF",
        "ACTOR_ACCOUNT_ID",
        "FILE_PATH",
        "COMMIT_MESSAGE",
        "WORKFLOW_NAME",
        "TAG_NAME",
        "RELEASE_NAME",
        "REPOSITORY_NAME",
        "ORGANIZATION_NAME",
    )
)


def serialize_aws_json_1_1(value: WebhookFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WebhookFilterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WebhookFilterType value: {data!r}")
    return cast(WebhookFilterType, data)
