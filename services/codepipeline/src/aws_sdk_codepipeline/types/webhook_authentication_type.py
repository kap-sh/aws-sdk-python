"""Generated from Smithy shape ``com.amazonaws.codepipeline#WebhookAuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

WebhookAuthenticationType: TypeAlias = Literal[
    "GITHUB_HMAC",
    "IP",
    "UNAUTHENTICATED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GITHUB_HMAC",
        "IP",
        "UNAUTHENTICATED",
    )
)


def serialize_aws_json_1_1(value: WebhookAuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WebhookAuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WebhookAuthenticationType value: {data!r}")
    return cast(WebhookAuthenticationType, data)
