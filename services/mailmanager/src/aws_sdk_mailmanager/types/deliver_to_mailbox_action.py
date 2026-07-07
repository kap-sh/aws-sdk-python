"""Generated from Smithy shape ``com.amazonaws.mailmanager#DeliverToMailboxAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.action_failure_policy
    import aws_sdk_mailmanager.types.iam_role_arn
    import aws_sdk_mailmanager.types.name_or_arn


class DeliverToMailboxAction(TypedDict, closed=True):
    action_failure_policy: NotRequired[
        "aws_sdk_mailmanager.types.action_failure_policy.ActionFailurePolicy"
    ]
    """<p>A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the mailbox ARN is no longer valid.</p>"""
    mailbox_arn: "aws_sdk_mailmanager.types.name_or_arn.NameOrArn"
    """<p>The Amazon Resource Name (ARN) of a WorkMail organization to deliver the email to.</p>"""
    role_arn: "aws_sdk_mailmanager.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role to use to execute this action. The role must have access to the workmail:DeliverToMailbox API.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeliverToMailboxAction) -> dict:
    out: dict = {}
    if "action_failure_policy" in value:
        import aws_sdk_mailmanager.types.action_failure_policy

        out["ActionFailurePolicy"] = (
            aws_sdk_mailmanager.types.action_failure_policy.serialize_aws_json_1_0(
                value["action_failure_policy"]
            )
        )
    out["MailboxArn"] = value["mailbox_arn"]
    out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeliverToMailboxAction:
    out: DeliverToMailboxAction = {}  # type: ignore[typeddict-item]
    if "ActionFailurePolicy" in data:
        import aws_sdk_mailmanager.types.action_failure_policy

        out["action_failure_policy"] = (
            aws_sdk_mailmanager.types.action_failure_policy.deserialize_aws_json_1_0(
                data["ActionFailurePolicy"]
            )
        )
    if "MailboxArn" in data:
        out["mailbox_arn"] = data["MailboxArn"]
    else:
        raise DeserializationError("DeliverToMailboxAction.mailbox_arn required")
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("DeliverToMailboxAction.role_arn required")
    return out
