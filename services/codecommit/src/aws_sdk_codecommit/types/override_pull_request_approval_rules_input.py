"""Generated from Smithy shape ``com.amazonaws.codecommit#OverridePullRequestApprovalRulesInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.override_status
    import aws_sdk_codecommit.types.pull_request_id
    import aws_sdk_codecommit.types.revision_id


class OverridePullRequestApprovalRulesInput(TypedDict):
    pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID of the pull request for which you want to override all approval rule requirements. To get this information, use <a>GetPullRequest</a>.</p>"""
    revision_id: "aws_sdk_codecommit.types.revision_id.RevisionId"
    """<p>The system-generated ID of the most recent revision of the pull request. You cannot override approval rules for anything but the most recent revision of a pull request. To get the revision ID, use GetPullRequest.</p>"""
    override_status: "aws_sdk_codecommit.types.override_status.OverrideStatus"
    """<p>Whether you want to set aside approval rule requirements for the pull request (OVERRIDE) or revoke a previous override and apply approval rule requirements (REVOKE). REVOKE status is not stored.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OverridePullRequestApprovalRulesInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    out["revisionId"] = value["revision_id"]
    import aws_sdk_codecommit.types.override_status

    out["overrideStatus"] = (
        aws_sdk_codecommit.types.override_status.serialize_aws_json_1_1(
            value["override_status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OverridePullRequestApprovalRulesInput:
    out: OverridePullRequestApprovalRulesInput = {}  # type: ignore[typeddict-item]
    if "pullRequestId" in data:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        raise DeserializationError(
            "OverridePullRequestApprovalRulesInput.pull_request_id required"
        )
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    else:
        raise DeserializationError(
            "OverridePullRequestApprovalRulesInput.revision_id required"
        )
    if "overrideStatus" in data:
        import aws_sdk_codecommit.types.override_status

        out["override_status"] = (
            aws_sdk_codecommit.types.override_status.deserialize_aws_json_1_1(
                data["overrideStatus"]
            )
        )
    else:
        raise DeserializationError(
            "OverridePullRequestApprovalRulesInput.override_status required"
        )
    return out
