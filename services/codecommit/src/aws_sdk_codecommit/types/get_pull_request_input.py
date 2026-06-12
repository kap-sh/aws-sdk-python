"""Generated from Smithy shape ``com.amazonaws.codecommit#GetPullRequestInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.pull_request_id


class GetPullRequestInput(TypedDict):
    pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPullRequestInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPullRequestInput:
    out: GetPullRequestInput = {}  # type: ignore[typeddict-item]
    if "pullRequestId" in data:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        raise DeserializationError("GetPullRequestInput.pull_request_id required")
    return out
