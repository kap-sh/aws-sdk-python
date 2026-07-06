"""Generated from Smithy shape ``com.amazonaws.codecommit#CreatePullRequestApprovalRuleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_rule


class CreatePullRequestApprovalRuleOutput(TypedDict, closed=True):
    approval_rule: "aws_sdk_codecommit.types.approval_rule.ApprovalRule"
    """<p>Information about the created approval rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePullRequestApprovalRuleOutput) -> dict:
    out: dict = {}
    import aws_sdk_codecommit.types.approval_rule

    out["approvalRule"] = aws_sdk_codecommit.types.approval_rule.serialize_aws_json_1_1(
        value["approval_rule"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePullRequestApprovalRuleOutput:
    out: CreatePullRequestApprovalRuleOutput = {}  # type: ignore[typeddict-item]
    if "approvalRule" in data:
        import aws_sdk_codecommit.types.approval_rule

        out["approval_rule"] = (
            aws_sdk_codecommit.types.approval_rule.deserialize_aws_json_1_1(
                data["approvalRule"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePullRequestApprovalRuleOutput.approval_rule required"
        )
    return out
