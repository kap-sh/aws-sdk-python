"""Generated from Smithy shape ``com.amazonaws.fms#AwsVPCSecurityGroupViolation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.length_bounded_string
    import aws_sdk_fms.types.partial_matches
    import aws_sdk_fms.types.security_group_remediation_actions
    import aws_sdk_fms.types.violation_target


class AwsVPCSecurityGroupViolation(TypedDict):
    violation_target: NotRequired["aws_sdk_fms.types.violation_target.ViolationTarget"]
    """<p>The security group rule that is being evaluated.</p>"""
    violation_target_description: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>A description of the security group that violates the policy.</p>"""
    partial_matches: NotRequired["aws_sdk_fms.types.partial_matches.PartialMatches"]
    """<p>List of rules specified in the security group of the Firewall Manager policy that partially match the <code>ViolationTarget</code> rule.</p>"""
    possible_security_group_remediation_actions: NotRequired[
        "aws_sdk_fms.types.security_group_remediation_actions.SecurityGroupRemediationActions"
    ]
    """<p>Remediation options for the rule specified in the <code>ViolationTarget</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AwsVPCSecurityGroupViolation) -> dict:
    out: dict = {}
    if "violation_target" in value:
        out["ViolationTarget"] = value["violation_target"]
    if "violation_target_description" in value:
        out["ViolationTargetDescription"] = value["violation_target_description"]
    if "partial_matches" in value:
        import aws_sdk_fms.types.partial_matches

        out["PartialMatches"] = (
            aws_sdk_fms.types.partial_matches.serialize_aws_json_1_1(
                value["partial_matches"]
            )
        )
    if "possible_security_group_remediation_actions" in value:
        import aws_sdk_fms.types.security_group_remediation_actions

        out["PossibleSecurityGroupRemediationActions"] = (
            aws_sdk_fms.types.security_group_remediation_actions.serialize_aws_json_1_1(
                value["possible_security_group_remediation_actions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AwsVPCSecurityGroupViolation:
    out: AwsVPCSecurityGroupViolation = {}  # type: ignore[typeddict-item]
    if "ViolationTarget" in data:
        out["violation_target"] = data["ViolationTarget"]
    if "ViolationTargetDescription" in data:
        out["violation_target_description"] = data["ViolationTargetDescription"]
    if "PartialMatches" in data:
        import aws_sdk_fms.types.partial_matches

        out["partial_matches"] = (
            aws_sdk_fms.types.partial_matches.deserialize_aws_json_1_1(
                data["PartialMatches"]
            )
        )
    if "PossibleSecurityGroupRemediationActions" in data:
        import aws_sdk_fms.types.security_group_remediation_actions

        out["possible_security_group_remediation_actions"] = (
            aws_sdk_fms.types.security_group_remediation_actions.deserialize_aws_json_1_1(
                data["PossibleSecurityGroupRemediationActions"]
            )
        )
    return out
