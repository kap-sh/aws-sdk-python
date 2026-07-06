"""Generated from Smithy shape ``com.amazonaws.codecommit#Evaluation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_rules_not_satisfied_list
    import aws_sdk_codecommit.types.approval_rules_satisfied_list
    import aws_sdk_codecommit.types.approved
    import aws_sdk_codecommit.types.overridden


class Evaluation(TypedDict, closed=True):
    approved: "aws_sdk_codecommit.types.approved.Approved"
    """<p>Whether the state of the pull request is approved.</p>"""
    overridden: "aws_sdk_codecommit.types.overridden.Overridden"
    """<p>Whether the approval rule requirements for the pull request have been overridden and no longer need to be met.</p>"""
    approval_rules_satisfied: NotRequired[
        "aws_sdk_codecommit.types.approval_rules_satisfied_list.ApprovalRulesSatisfiedList"
    ]
    """<p>The names of the approval rules that have had their conditions met.</p>"""
    approval_rules_not_satisfied: NotRequired[
        "aws_sdk_codecommit.types.approval_rules_not_satisfied_list.ApprovalRulesNotSatisfiedList"
    ]
    """<p>The names of the approval rules that have not had their conditions met.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Evaluation) -> dict:
    out: dict = {}
    out["approved"] = value.get("approved", False)
    out["overridden"] = value.get("overridden", False)
    if "approval_rules_satisfied" in value:
        import aws_sdk_codecommit.types.approval_rules_satisfied_list

        out["approvalRulesSatisfied"] = (
            aws_sdk_codecommit.types.approval_rules_satisfied_list.serialize_aws_json_1_1(
                value["approval_rules_satisfied"]
            )
        )
    if "approval_rules_not_satisfied" in value:
        import aws_sdk_codecommit.types.approval_rules_not_satisfied_list

        out["approvalRulesNotSatisfied"] = (
            aws_sdk_codecommit.types.approval_rules_not_satisfied_list.serialize_aws_json_1_1(
                value["approval_rules_not_satisfied"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Evaluation:
    out: Evaluation = {}  # type: ignore[typeddict-item]
    if "approved" in data:
        out["approved"] = data["approved"]
    else:
        out["approved"] = False
    if "overridden" in data:
        out["overridden"] = data["overridden"]
    else:
        out["overridden"] = False
    if "approvalRulesSatisfied" in data:
        import aws_sdk_codecommit.types.approval_rules_satisfied_list

        out["approval_rules_satisfied"] = (
            aws_sdk_codecommit.types.approval_rules_satisfied_list.deserialize_aws_json_1_1(
                data["approvalRulesSatisfied"]
            )
        )
    if "approvalRulesNotSatisfied" in data:
        import aws_sdk_codecommit.types.approval_rules_not_satisfied_list

        out["approval_rules_not_satisfied"] = (
            aws_sdk_codecommit.types.approval_rules_not_satisfied_list.deserialize_aws_json_1_1(
                data["approvalRulesNotSatisfied"]
            )
        )
    return out
