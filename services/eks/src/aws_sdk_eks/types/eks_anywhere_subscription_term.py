"""Generated from Smithy shape ``com.amazonaws.eks#EksAnywhereSubscriptionTerm``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.eks_anywhere_subscription_term_unit
    import aws_sdk_eks.types.integer


class EksAnywhereSubscriptionTerm(TypedDict):
    duration: "aws_sdk_eks.types.integer.Integer"
    """<p>The duration of the subscription term. Valid values are 12 and 36, indicating a 12 month or 36 month subscription.</p>"""
    unit: NotRequired[
        "aws_sdk_eks.types.eks_anywhere_subscription_term_unit.EksAnywhereSubscriptionTermUnit"
    ]
    """<p>The term unit of the subscription. Valid value is <code>MONTHS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksAnywhereSubscriptionTerm) -> dict:
    out: dict = {}
    out["duration"] = value.get("duration", 0)
    if "unit" in value:
        import aws_sdk_eks.types.eks_anywhere_subscription_term_unit

        out["unit"] = (
            aws_sdk_eks.types.eks_anywhere_subscription_term_unit.serialize_json(
                value["unit"]
            )
        )
    return out


def deserialize_json(data: dict) -> EksAnywhereSubscriptionTerm:
    out: EksAnywhereSubscriptionTerm = {}  # type: ignore[typeddict-item]
    if "duration" in data:
        out["duration"] = data["duration"]
    else:
        out["duration"] = 0
    if "unit" in data:
        import aws_sdk_eks.types.eks_anywhere_subscription_term_unit

        out["unit"] = (
            aws_sdk_eks.types.eks_anywhere_subscription_term_unit.deserialize_json(
                data["unit"]
            )
        )
    return out
