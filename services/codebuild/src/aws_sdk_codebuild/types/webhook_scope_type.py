"""Generated from Smithy shape ``com.amazonaws.codebuild#WebhookScopeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

WebhookScopeType: TypeAlias = Literal[
    "GITHUB_ORGANIZATION",
    "GITHUB_GLOBAL",
    "GITLAB_GROUP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GITHUB_ORGANIZATION",
        "GITHUB_GLOBAL",
        "GITLAB_GROUP",
    )
)


def serialize_aws_json_1_1(value: WebhookScopeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WebhookScopeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WebhookScopeType value: {data!r}")
    return cast(WebhookScopeType, data)
