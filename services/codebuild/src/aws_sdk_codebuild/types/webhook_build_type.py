"""Generated from Smithy shape ``com.amazonaws.codebuild#WebhookBuildType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

WebhookBuildType: TypeAlias = Literal[
    "BUILD",
    "BUILD_BATCH",
    "RUNNER_BUILDKITE_BUILD",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BUILD",
        "BUILD_BATCH",
        "RUNNER_BUILDKITE_BUILD",
    )
)


def serialize_aws_json_1_1(value: WebhookBuildType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WebhookBuildType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WebhookBuildType value: {data!r}")
    return cast(WebhookBuildType, data)
