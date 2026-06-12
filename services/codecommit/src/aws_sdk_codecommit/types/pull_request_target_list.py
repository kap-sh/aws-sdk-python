"""Generated from Smithy shape ``com.amazonaws.codecommit#PullRequestTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.pull_request_target

PullRequestTargetList: TypeAlias = list[
    "aws_sdk_codecommit.types.pull_request_target.PullRequestTarget"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullRequestTargetList) -> list:
    import aws_sdk_codecommit.types.pull_request_target

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codecommit.types.pull_request_target.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PullRequestTargetList:
    import aws_sdk_codecommit.types.pull_request_target

    out: PullRequestTargetList = []
    for item in data:
        out.append(
            aws_sdk_codecommit.types.pull_request_target.deserialize_aws_json_1_1(item)
        )
    return out
