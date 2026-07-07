"""Generated from Smithy shape ``com.amazonaws.fms#SecurityGroupRemediationAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fms.types.boolean
    import aws_sdk_fms.types.remediation_action_description
    import aws_sdk_fms.types.remediation_action_type
    import aws_sdk_fms.types.security_group_rule_description


class SecurityGroupRemediationAction(TypedDict, closed=True):
    remediation_action_type: NotRequired[
        "aws_sdk_fms.types.remediation_action_type.RemediationActionType"
    ]
    """<p>The remediation action that will be performed.</p>"""
    description: NotRequired[
        "aws_sdk_fms.types.remediation_action_description.RemediationActionDescription"
    ]
    """<p>Brief description of the action that will be performed.</p>"""
    remediation_result: NotRequired[
        "aws_sdk_fms.types.security_group_rule_description.SecurityGroupRuleDescription"
    ]
    """<p>The final state of the rule specified in the <code>ViolationTarget</code> after it is remediated.</p>"""
    is_default_action: "aws_sdk_fms.types.boolean.Boolean"
    """<p>Indicates if the current action is the default action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityGroupRemediationAction) -> dict:
    out: dict = {}
    if "remediation_action_type" in value:
        import aws_sdk_fms.types.remediation_action_type

        out["RemediationActionType"] = (
            aws_sdk_fms.types.remediation_action_type.serialize_aws_json_1_1(
                value["remediation_action_type"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "remediation_result" in value:
        import aws_sdk_fms.types.security_group_rule_description

        out["RemediationResult"] = (
            aws_sdk_fms.types.security_group_rule_description.serialize_aws_json_1_1(
                value["remediation_result"]
            )
        )
    out["IsDefaultAction"] = value.get("is_default_action", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> SecurityGroupRemediationAction:
    out: SecurityGroupRemediationAction = {}  # type: ignore[typeddict-item]
    if "RemediationActionType" in data:
        import aws_sdk_fms.types.remediation_action_type

        out["remediation_action_type"] = (
            aws_sdk_fms.types.remediation_action_type.deserialize_aws_json_1_1(
                data["RemediationActionType"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "RemediationResult" in data:
        import aws_sdk_fms.types.security_group_rule_description

        out["remediation_result"] = (
            aws_sdk_fms.types.security_group_rule_description.deserialize_aws_json_1_1(
                data["RemediationResult"]
            )
        )
    if "IsDefaultAction" in data:
        out["is_default_action"] = data["IsDefaultAction"]
    else:
        out["is_default_action"] = False
    return out
