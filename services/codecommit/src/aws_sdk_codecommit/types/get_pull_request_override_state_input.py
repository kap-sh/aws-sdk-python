"""Generated from Smithy shape ``com.amazonaws.codecommit#GetPullRequestOverrideStateInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.pull_request_id
    import aws_sdk_codecommit.types.revision_id


class GetPullRequestOverrideStateInput(TypedDict):
    pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId"
    """<p>The ID of the pull request for which you want to get information about whether approval rules have been set aside (overridden).</p>"""
    revision_id: "aws_sdk_codecommit.types.revision_id.RevisionId"
    """<p>The system-generated ID of the revision for the pull request. To retrieve the most recent revision ID, use <a>GetPullRequest</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPullRequestOverrideStateInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    out["revisionId"] = value["revision_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPullRequestOverrideStateInput:
    out: GetPullRequestOverrideStateInput = {}  # type: ignore[typeddict-item]
    if "pullRequestId" in data:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        raise DeserializationError(
            "GetPullRequestOverrideStateInput.pull_request_id required"
        )
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    else:
        raise DeserializationError(
            "GetPullRequestOverrideStateInput.revision_id required"
        )
    return out
