"""Generated from Smithy shape ``com.amazonaws.mailmanager#RelayAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.action_failure_policy
    import aws_sdk_mailmanager.types.id_or_arn
    import aws_sdk_mailmanager.types.mail_from


class RelayAction(TypedDict):
    action_failure_policy: NotRequired[
        "aws_sdk_mailmanager.types.action_failure_policy.ActionFailurePolicy"
    ]
    """<p>A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the specified relay has been deleted.</p>"""
    relay: "aws_sdk_mailmanager.types.id_or_arn.IdOrArn"
    """<p>The identifier of the relay resource to be used when relaying an email.</p>"""
    mail_from: NotRequired["aws_sdk_mailmanager.types.mail_from.MailFrom"]
    """<p>This action specifies whether to preserve or replace original mail from address while relaying received emails to a destination server.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RelayAction) -> dict:
    out: dict = {}
    if "action_failure_policy" in value:
        import aws_sdk_mailmanager.types.action_failure_policy

        out["ActionFailurePolicy"] = (
            aws_sdk_mailmanager.types.action_failure_policy.serialize_aws_json_1_0(
                value["action_failure_policy"]
            )
        )
    out["Relay"] = value["relay"]
    if "mail_from" in value:
        import aws_sdk_mailmanager.types.mail_from

        out["MailFrom"] = aws_sdk_mailmanager.types.mail_from.serialize_aws_json_1_0(
            value["mail_from"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RelayAction:
    out: RelayAction = {}  # type: ignore[typeddict-item]
    if "ActionFailurePolicy" in data:
        import aws_sdk_mailmanager.types.action_failure_policy

        out["action_failure_policy"] = (
            aws_sdk_mailmanager.types.action_failure_policy.deserialize_aws_json_1_0(
                data["ActionFailurePolicy"]
            )
        )
    if "Relay" in data:
        out["relay"] = data["Relay"]
    else:
        raise DeserializationError("RelayAction.relay required")
    if "MailFrom" in data:
        import aws_sdk_mailmanager.types.mail_from

        out["mail_from"] = aws_sdk_mailmanager.types.mail_from.deserialize_aws_json_1_0(
            data["MailFrom"]
        )
    return out
