"""Generated from Smithy shape ``com.amazonaws.fms#PartialMatch``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.reference_rule
    import aws_sdk_fms.types.target_violation_reasons


class PartialMatch(TypedDict):
    reference: NotRequired["aws_sdk_fms.types.reference_rule.ReferenceRule"]
    """<p>The reference rule from the primary security group of the Firewall Manager policy.</p>"""
    target_violation_reasons: NotRequired[
        "aws_sdk_fms.types.target_violation_reasons.TargetViolationReasons"
    ]
    """<p>The violation reason.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartialMatch) -> dict:
    out: dict = {}
    if "reference" in value:
        out["Reference"] = value["reference"]
    if "target_violation_reasons" in value:
        import aws_sdk_fms.types.target_violation_reasons

        out["TargetViolationReasons"] = (
            aws_sdk_fms.types.target_violation_reasons.serialize_aws_json_1_1(
                value["target_violation_reasons"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PartialMatch:
    out: PartialMatch = {}  # type: ignore[typeddict-item]
    if "Reference" in data:
        out["reference"] = data["Reference"]
    if "TargetViolationReasons" in data:
        import aws_sdk_fms.types.target_violation_reasons

        out["target_violation_reasons"] = (
            aws_sdk_fms.types.target_violation_reasons.deserialize_aws_json_1_1(
                data["TargetViolationReasons"]
            )
        )
    return out
