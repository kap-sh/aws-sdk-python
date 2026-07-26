"""Generated from Smithy shape ``com.amazonaws.codebuild#WebhookScopeType``."""

from typing import Literal, TypeAlias, cast

WebhookScopeType: TypeAlias = Literal[
    "GITHUB_ORGANIZATION",
    "GITHUB_GLOBAL",
    "GITLAB_GROUP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebhookScopeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WebhookScopeType:
    return cast(WebhookScopeType, data)
