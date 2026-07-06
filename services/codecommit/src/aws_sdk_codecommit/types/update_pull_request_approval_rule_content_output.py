"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdatePullRequestApprovalRuleContentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_rule


class UpdatePullRequestApprovalRuleContentOutput(TypedDict, closed=True):
    approval_rule: "aws_sdk_codecommit.types.approval_rule.ApprovalRule"
    """<p>Information about the updated approval rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePullRequestApprovalRuleContentOutput) -> dict:
    out: dict = {}
    import aws_sdk_codecommit.types.approval_rule

    out["approvalRule"] = aws_sdk_codecommit.types.approval_rule.serialize_aws_json_1_1(
        value["approval_rule"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePullRequestApprovalRuleContentOutput:
    out: UpdatePullRequestApprovalRuleContentOutput = {}  # type: ignore[typeddict-item]
    if "approvalRule" in data:
        import aws_sdk_codecommit.types.approval_rule

        out["approval_rule"] = (
            aws_sdk_codecommit.types.approval_rule.deserialize_aws_json_1_1(
                data["approvalRule"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePullRequestApprovalRuleContentOutput.approval_rule required"
        )
    return out
