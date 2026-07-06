"""Generated from Smithy shape ``com.amazonaws.fms#DnsRuleGroupLimitExceededViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fms.types.basic_integer
    import aws_sdk_fms.types.length_bounded_string
    import aws_sdk_fms.types.violation_target


class DnsRuleGroupLimitExceededViolation(TypedDict, closed=True):
    violation_target: NotRequired["aws_sdk_fms.types.violation_target.ViolationTarget"]
    """<p>Information about the VPC ID. </p>"""
    violation_target_description: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>A description of the violation that specifies the rule group and VPC.</p>"""
    number_of_rule_groups_already_associated: (
        "aws_sdk_fms.types.basic_integer.BasicInteger"
    )
    """<p>The number of rule groups currently associated with the VPC. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsRuleGroupLimitExceededViolation) -> dict:
    out: dict = {}
    if "violation_target" in value:
        out["ViolationTarget"] = value["violation_target"]
    if "violation_target_description" in value:
        out["ViolationTargetDescription"] = value["violation_target_description"]
    out["NumberOfRuleGroupsAlreadyAssociated"] = value.get(
        "number_of_rule_groups_already_associated", 0
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DnsRuleGroupLimitExceededViolation:
    out: DnsRuleGroupLimitExceededViolation = {}  # type: ignore[typeddict-item]
    if "ViolationTarget" in data:
        out["violation_target"] = data["ViolationTarget"]
    if "ViolationTargetDescription" in data:
        out["violation_target_description"] = data["ViolationTargetDescription"]
    if "NumberOfRuleGroupsAlreadyAssociated" in data:
        out["number_of_rule_groups_already_associated"] = data[
            "NumberOfRuleGroupsAlreadyAssociated"
        ]
    else:
        out["number_of_rule_groups_already_associated"] = 0
    return out
