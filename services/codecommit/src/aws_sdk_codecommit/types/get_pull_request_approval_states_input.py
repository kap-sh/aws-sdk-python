"""Generated from Smithy shape ``com.amazonaws.codecommit#GetPullRequestApprovalStatesInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.pull_request_id
    import aws_sdk_codecommit.types.revision_id


class GetPullRequestApprovalStatesInput(TypedDict):
    pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID for the pull request.</p>"""
    revision_id: "aws_sdk_codecommit.types.revision_id.RevisionId"
    """<p>The system-generated ID for the pull request revision.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPullRequestApprovalStatesInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    out["revisionId"] = value["revision_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPullRequestApprovalStatesInput:
    out: GetPullRequestApprovalStatesInput = {}  # type: ignore[typeddict-item]
    if "pullRequestId" in data:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        raise DeserializationError(
            "GetPullRequestApprovalStatesInput.pull_request_id required"
        )
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    else:
        raise DeserializationError(
            "GetPullRequestApprovalStatesInput.revision_id required"
        )
    return out
