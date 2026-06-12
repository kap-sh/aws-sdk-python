"""Generated from Smithy shape ``com.amazonaws.codecommit#PullRequestEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.pull_request_event

PullRequestEventList: TypeAlias = list[
    "aws_sdk_codecommit.types.pull_request_event.PullRequestEvent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullRequestEventList) -> list:
    import aws_sdk_codecommit.types.pull_request_event

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codecommit.types.pull_request_event.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PullRequestEventList:
    import aws_sdk_codecommit.types.pull_request_event

    out: PullRequestEventList = []
    for item in data:
        out.append(
            aws_sdk_codecommit.types.pull_request_event.deserialize_aws_json_1_1(item)
        )
    return out
