"""Generated from Smithy shape ``com.amazonaws.mailmanager#BounceAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.action_failure_policy
    import aws_sdk_mailmanager.types.bounce_message
    import aws_sdk_mailmanager.types.diagnostic_message
    import aws_sdk_mailmanager.types.email_address
    import aws_sdk_mailmanager.types.iam_role_arn
    import aws_sdk_mailmanager.types.smtp_reply_code
    import aws_sdk_mailmanager.types.status_code


class BounceAction(TypedDict, closed=True):
    action_failure_policy: NotRequired[
        "aws_sdk_mailmanager.types.action_failure_policy.ActionFailurePolicy"
    ]
    """<p>A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the caller does not have the permissions to call the SendBounce API.</p>"""
    role_arn: "aws_sdk_mailmanager.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role to use to send the bounce message.</p>"""
    sender: "aws_sdk_mailmanager.types.email_address.EmailAddress"
    """<p>The sender email address of the bounce message.</p>"""
    status_code: "aws_sdk_mailmanager.types.status_code.StatusCode"
    """<p>The enhanced status code for the bounce, in the format of x.y.z (e.g. 5.1.1).</p>"""
    smtp_reply_code: "aws_sdk_mailmanager.types.smtp_reply_code.SmtpReplyCode"
    """<p>The SMTP reply code for the bounce, as defined by RFC 5321.</p>"""
    diagnostic_message: "aws_sdk_mailmanager.types.diagnostic_message.DiagnosticMessage"
    """<p>The diagnostic message included in the Diagnostic-Code header of the bounce.</p>"""
    message: NotRequired["aws_sdk_mailmanager.types.bounce_message.BounceMessage"]
    """<p>The human-readable text to include in the bounce message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BounceAction) -> dict:
    out: dict = {}
    if "action_failure_policy" in value:
        import aws_sdk_mailmanager.types.action_failure_policy

        out["ActionFailurePolicy"] = (
            aws_sdk_mailmanager.types.action_failure_policy.serialize_aws_json_1_0(
                value["action_failure_policy"]
            )
        )
    out["RoleArn"] = value["role_arn"]
    out["Sender"] = value["sender"]
    out["StatusCode"] = value["status_code"]
    out["SmtpReplyCode"] = value["smtp_reply_code"]
    out["DiagnosticMessage"] = value["diagnostic_message"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BounceAction:
    out: BounceAction = {}  # type: ignore[typeddict-item]
    if "ActionFailurePolicy" in data:
        import aws_sdk_mailmanager.types.action_failure_policy

        out["action_failure_policy"] = (
            aws_sdk_mailmanager.types.action_failure_policy.deserialize_aws_json_1_0(
                data["ActionFailurePolicy"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("BounceAction.role_arn required")
    if "Sender" in data:
        out["sender"] = data["Sender"]
    else:
        raise DeserializationError("BounceAction.sender required")
    if "StatusCode" in data:
        out["status_code"] = data["StatusCode"]
    else:
        raise DeserializationError("BounceAction.status_code required")
    if "SmtpReplyCode" in data:
        out["smtp_reply_code"] = data["SmtpReplyCode"]
    else:
        raise DeserializationError("BounceAction.smtp_reply_code required")
    if "DiagnosticMessage" in data:
        out["diagnostic_message"] = data["DiagnosticMessage"]
    else:
        raise DeserializationError("BounceAction.diagnostic_message required")
    if "Message" in data:
        out["message"] = data["Message"]
    return out
