"""Generated from Smithy shape ``com.amazonaws.codecommit#DeletePullRequestApprovalRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_rule_name
    import aws_sdk_codecommit.types.pull_request_id


class DeletePullRequestApprovalRuleInput(TypedDict, closed=True):
    pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID of the pull request that contains the approval rule you want to delete.</p>"""
    approval_rule_name: "aws_sdk_codecommit.types.approval_rule_name.ApprovalRuleName"
    """<p>The name of the approval rule you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePullRequestApprovalRuleInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    out["approvalRuleName"] = value["approval_rule_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePullRequestApprovalRuleInput:
    out: DeletePullRequestApprovalRuleInput = {}  # type: ignore[typeddict-item]
    if "pullRequestId" in data:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        raise DeserializationError(
            "DeletePullRequestApprovalRuleInput.pull_request_id required"
        )
    if "approvalRuleName" in data:
        out["approval_rule_name"] = data["approvalRuleName"]
    else:
        raise DeserializationError(
            "DeletePullRequestApprovalRuleInput.approval_rule_name required"
        )
    return out
