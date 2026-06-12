"""Generated from Smithy shape ``com.amazonaws.codepipeline#GitPullRequestEventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

GitPullRequestEventType: TypeAlias = Literal[
    "OPEN",
    "UPDATED",
    "CLOSED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OPEN",
        "UPDATED",
        "CLOSED",
    )
)


def serialize_aws_json_1_1(value: GitPullRequestEventType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GitPullRequestEventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GitPullRequestEventType value: {data!r}")
    return cast(GitPullRequestEventType, data)
