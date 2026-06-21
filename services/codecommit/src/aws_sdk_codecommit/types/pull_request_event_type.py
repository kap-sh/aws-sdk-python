"""Generated from Smithy shape ``com.amazonaws.codecommit#PullRequestEventType``."""

from typing import Literal, TypeAlias, cast

PullRequestEventType: TypeAlias = Literal[
    "PULL_REQUEST_CREATED",
    "PULL_REQUEST_STATUS_CHANGED",
    "PULL_REQUEST_SOURCE_REFERENCE_UPDATED",
    "PULL_REQUEST_MERGE_STATE_CHANGED",
    "PULL_REQUEST_APPROVAL_RULE_CREATED",
    "PULL_REQUEST_APPROVAL_RULE_UPDATED",
    "PULL_REQUEST_APPROVAL_RULE_DELETED",
    "PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN",
    "PULL_REQUEST_APPROVAL_STATE_CHANGED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullRequestEventType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PullRequestEventType:
    return cast(PullRequestEventType, data)
