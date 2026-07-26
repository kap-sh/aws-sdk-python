"""Generated from Smithy shape ``com.amazonaws.codecommit#PullRequestStatusEnum``."""

from typing import Literal, TypeAlias, cast

PullRequestStatusEnum: TypeAlias = Literal[
    "OPEN",
    "CLOSED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullRequestStatusEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PullRequestStatusEnum:
    return cast(PullRequestStatusEnum, data)
