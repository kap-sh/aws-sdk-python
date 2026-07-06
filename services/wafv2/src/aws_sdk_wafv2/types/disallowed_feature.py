"""Generated from Smithy shape ``com.amazonaws.wafv2#DisallowedFeature``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.pricing_plan_feature_name
    import aws_sdk_wafv2.types.required_pricing_plan_name


class DisallowedFeature(TypedDict, closed=True):
    feature: NotRequired[
        "aws_sdk_wafv2.types.pricing_plan_feature_name.PricingPlanFeatureName"
    ]
    """<p>The name of the disallowed WAF feature.</p>"""
    required_pricing_plan: NotRequired[
        "aws_sdk_wafv2.types.required_pricing_plan_name.RequiredPricingPlanName"
    ]
    """<p>The name of the CloudFront pricing plan required to use the WAF feature.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisallowedFeature) -> dict:
    out: dict = {}
    if "feature" in value:
        out["Feature"] = value["feature"]
    if "required_pricing_plan" in value:
        out["RequiredPricingPlan"] = value["required_pricing_plan"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisallowedFeature:
    out: DisallowedFeature = {}  # type: ignore[typeddict-item]
    if "Feature" in data:
        out["feature"] = data["Feature"]
    if "RequiredPricingPlan" in data:
        out["required_pricing_plan"] = data["RequiredPricingPlan"]
    return out
