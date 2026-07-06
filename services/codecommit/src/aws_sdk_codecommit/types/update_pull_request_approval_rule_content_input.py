"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdatePullRequestApprovalRuleContentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_rule_content
    import aws_sdk_codecommit.types.approval_rule_name
    import aws_sdk_codecommit.types.pull_request_id
    import aws_sdk_codecommit.types.rule_content_sha256


class UpdatePullRequestApprovalRuleContentInput(TypedDict, closed=True):
    pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID of the pull request.</p>"""
    approval_rule_name: "aws_sdk_codecommit.types.approval_rule_name.ApprovalRuleName"
    """<p>The name of the approval rule you want to update.</p>"""
    existing_rule_content_sha256: NotRequired[
        "aws_sdk_codecommit.types.rule_content_sha256.RuleContentSha256"
    ]
    """<p>The SHA-256 hash signature for the content of the approval rule. You can retrieve this information by using <a>GetPullRequest</a>.</p>"""
    new_rule_content: (
        "aws_sdk_codecommit.types.approval_rule_content.ApprovalRuleContent"
    )
    r"""<p>The updated content for the approval rule.</p> <note> <p>When you update the content of the approval rule, you can specify approvers in an approval pool in one of two ways:</p> <ul> <li> <p> <b>CodeCommitApprovers</b>: This option only requires an Amazon Web Services account and a resource. It can be used for both IAM users and federated access users whose name matches the provided resource name. This is a very powerful option that offers a great deal of flexibility. For example, if you specify the Amazon Web Services account <i>123456789012</i> and <i>Mary_Major</i>, all of the following are counted as approvals coming from that user:</p> <ul> <li> <p>An IAM user in the account (arn:aws:iam::<i>123456789012</i>:user/<i>Mary_Major</i>)</p> </li> <li> <p>A federated user identified in IAM as Mary_Major (arn:aws:sts::<i>123456789012</i>:federated-user/<i>Mary_Major</i>)</p> </li> </ul> <p>This option does not recognize an active session of someone assuming the role of CodeCommitReview with a role session name of <i>Mary_Major</i> (arn:aws:sts::<i>123456789012</i>:assumed-role/CodeCommitReview/<i>Mary_Major</i>) unless you include a wildcard (*Mary_Major).</p> </li> <li> <p> <b>Fully qualified ARN</b>: This option allows you to specify the fully qualified Amazon Resource Name (ARN) of the IAM user or role. </p> </li> </ul> <p>For more information about IAM ARNs, wildcards, and formats, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html\">IAM Identifiers</a> in the <i>IAM User Guide</i>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePullRequestApprovalRuleContentInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    out["approvalRuleName"] = value["approval_rule_name"]
    if "existing_rule_content_sha256" in value:
        out["existingRuleContentSha256"] = value["existing_rule_content_sha256"]
    out["newRuleContent"] = value["new_rule_content"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePullRequestApprovalRuleContentInput:
    out: UpdatePullRequestApprovalRuleContentInput = {}  # type: ignore[typeddict-item]
    if "pullRequestId" in data:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        raise DeserializationError(
            "UpdatePullRequestApprovalRuleContentInput.pull_request_id required"
        )
    if "approvalRuleName" in data:
        out["approval_rule_name"] = data["approvalRuleName"]
    else:
        raise DeserializationError(
            "UpdatePullRequestApprovalRuleContentInput.approval_rule_name required"
        )
    if "existingRuleContentSha256" in data:
        out["existing_rule_content_sha256"] = data["existingRuleContentSha256"]
    if "newRuleContent" in data:
        out["new_rule_content"] = data["newRuleContent"]
    else:
        raise DeserializationError(
            "UpdatePullRequestApprovalRuleContentInput.new_rule_content required"
        )
    return out
