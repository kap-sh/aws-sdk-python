"""Generated from Smithy shape ``com.amazonaws.codecommit#Approval``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_state
    import aws_sdk_codecommit.types.arn


class Approval(TypedDict):
    user_arn: NotRequired["aws_sdk_codecommit.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the user.</p>"""
    approval_state: NotRequired["aws_sdk_codecommit.types.approval_state.ApprovalState"]
    """<p>The state of the approval, APPROVE or REVOKE. REVOKE states are not stored.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Approval) -> dict:
    out: dict = {}
    if "user_arn" in value:
        out["userArn"] = value["user_arn"]
    if "approval_state" in value:
        import aws_sdk_codecommit.types.approval_state

        out["approvalState"] = (
            aws_sdk_codecommit.types.approval_state.serialize_aws_json_1_1(
                value["approval_state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Approval:
    out: Approval = {}  # type: ignore[typeddict-item]
    if "userArn" in data:
        out["user_arn"] = data["userArn"]
    if "approvalState" in data:
        import aws_sdk_codecommit.types.approval_state

        out["approval_state"] = (
            aws_sdk_codecommit.types.approval_state.deserialize_aws_json_1_1(
                data["approvalState"]
            )
        )
    return out
