"""Generated from Smithy shape ``com.amazonaws.codecommit#PullRequestIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.pull_request_id

PullRequestIdList: TypeAlias = list[
    "aws_sdk_codecommit.types.pull_request_id.PullRequestId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullRequestIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PullRequestIdList:
    return list(data)
