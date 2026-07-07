"""Generated from Smithy shape ``com.amazonaws.billingconductor#ComputationPreference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.pricing_plan_full_arn


class ComputationPreference(TypedDict, closed=True):
    pricing_plan_arn: (
        "aws_sdk_billingconductor.types.pricing_plan_full_arn.PricingPlanFullArn"
    )
    """<p> The Amazon Resource Name (ARN) of the pricing plan that's used to compute the Amazon Web Services charges for a billing group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputationPreference) -> dict:
    out: dict = {}
    out["PricingPlanArn"] = value["pricing_plan_arn"]
    return out


def deserialize_json(data: dict) -> ComputationPreference:
    out: ComputationPreference = {}  # type: ignore[typeddict-item]
    if "PricingPlanArn" in data:
        out["pricing_plan_arn"] = data["PricingPlanArn"]
    else:
        raise DeserializationError("ComputationPreference.pricing_plan_arn required")
    return out
