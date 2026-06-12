"""Generated from Smithy shape ``com.amazonaws.codebuild#WebhookStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

WebhookStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "ACTIVE",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATE_FAILED",
        "ACTIVE",
        "DELETING",
    )
)


def serialize_aws_json_1_1(value: WebhookStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WebhookStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WebhookStatus value: {data!r}")
    return cast(WebhookStatus, data)
