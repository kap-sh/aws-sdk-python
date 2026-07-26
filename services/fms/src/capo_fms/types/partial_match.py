"""Generated from Smithy shape ``com.amazonaws.fms#PartialMatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.reference_rule
    import capo_fms.types.target_violation_reasons


class PartialMatch(TypedDict, closed=True):
    reference: NotRequired["capo_fms.types.reference_rule.ReferenceRule"]
    """<p>The reference rule from the primary security group of the Firewall Manager policy.</p>"""
    target_violation_reasons: NotRequired[
        "capo_fms.types.target_violation_reasons.TargetViolationReasons"
    ]
    """<p>The violation reason.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartialMatch) -> dict:
    out: dict = {}
    if "reference" in value:
        out["Reference"] = value["reference"]
    if "target_violation_reasons" in value:
        import capo_fms.types.target_violation_reasons

        out["TargetViolationReasons"] = (
            capo_fms.types.target_violation_reasons.serialize_aws_json_1_1(
                value["target_violation_reasons"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PartialMatch:
    out: PartialMatch = {}  # type: ignore[typeddict-item]
    if "Reference" in data:
        out["reference"] = data["Reference"]
    if "TargetViolationReasons" in data:
        import capo_fms.types.target_violation_reasons

        out["target_violation_reasons"] = (
            capo_fms.types.target_violation_reasons.deserialize_aws_json_1_1(
                data["TargetViolationReasons"]
            )
        )
    return out
