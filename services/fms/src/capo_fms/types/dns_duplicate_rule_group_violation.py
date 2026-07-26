"""Generated from Smithy shape ``com.amazonaws.fms#DnsDuplicateRuleGroupViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.length_bounded_string
    import capo_fms.types.violation_target


class DnsDuplicateRuleGroupViolation(TypedDict, closed=True):
    violation_target: NotRequired["capo_fms.types.violation_target.ViolationTarget"]
    """<p>Information about the VPC ID. </p>"""
    violation_target_description: NotRequired[
        "capo_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>A description of the violation that specifies the rule group and VPC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsDuplicateRuleGroupViolation) -> dict:
    out: dict = {}
    if "violation_target" in value:
        out["ViolationTarget"] = value["violation_target"]
    if "violation_target_description" in value:
        out["ViolationTargetDescription"] = value["violation_target_description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DnsDuplicateRuleGroupViolation:
    out: DnsDuplicateRuleGroupViolation = {}  # type: ignore[typeddict-item]
    if "ViolationTarget" in data:
        out["violation_target"] = data["ViolationTarget"]
    if "ViolationTargetDescription" in data:
        out["violation_target_description"] = data["ViolationTargetDescription"]
    return out
