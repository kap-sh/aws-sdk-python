"""Generated from Smithy shape ``com.amazonaws.codepipeline#WebhookAuthenticationType``."""

from typing import Literal, TypeAlias, cast

WebhookAuthenticationType: TypeAlias = Literal[
    "GITHUB_HMAC",
    "IP",
    "UNAUTHENTICATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebhookAuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WebhookAuthenticationType:
    return cast(WebhookAuthenticationType, data)
