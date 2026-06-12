"""Generated from Smithy shape ``com.amazonaws.codebuild#PullRequestBuildCommentApproval``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

PullRequestBuildCommentApproval: TypeAlias = Literal[
    "DISABLED",
    "ALL_PULL_REQUESTS",
    "FORK_PULL_REQUESTS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ALL_PULL_REQUESTS",
        "FORK_PULL_REQUESTS",
    )
)


def serialize_aws_json_1_1(value: PullRequestBuildCommentApproval) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PullRequestBuildCommentApproval:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PullRequestBuildCommentApproval value: {data!r}"
        )
    return cast(PullRequestBuildCommentApproval, data)
