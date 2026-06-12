"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdatePullRequestTitleInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.pull_request_id
    import aws_sdk_codecommit.types.title


class UpdatePullRequestTitleInput(TypedDict):
    pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>"""
    title: "aws_sdk_codecommit.types.title.Title"
    """<p>The updated title of the pull request. This replaces the existing title.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePullRequestTitleInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    out["title"] = value["title"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePullRequestTitleInput:
    out: UpdatePullRequestTitleInput = {}  # type: ignore[typeddict-item]
    if "pullRequestId" in data:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        raise DeserializationError(
            "UpdatePullRequestTitleInput.pull_request_id required"
        )
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("UpdatePullRequestTitleInput.title required")
    return out
