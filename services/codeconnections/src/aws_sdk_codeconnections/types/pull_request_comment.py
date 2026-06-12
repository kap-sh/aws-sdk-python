"""Generated from Smithy shape ``com.amazonaws.codeconnections#PullRequestComment``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeconnections.errors import DeserializationError

PullRequestComment: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_0(value: PullRequestComment) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PullRequestComment:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PullRequestComment value: {data!r}")
    return cast(PullRequestComment, data)
