"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#UpdatePricingPlanRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.pricing_bundles
    import aws_sdk_iottwinmaker.types.pricing_mode


class UpdatePricingPlanRequest(TypedDict):
    pricing_mode: "aws_sdk_iottwinmaker.types.pricing_mode.PricingMode"
    """<p>The pricing mode.</p>"""
    bundle_names: NotRequired[
        "aws_sdk_iottwinmaker.types.pricing_bundles.PricingBundles"
    ]
    """<p>The bundle names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePricingPlanRequest) -> dict:
    out: dict = {}
    out["pricingMode"] = value["pricing_mode"]
    if "bundle_names" in value:
        import aws_sdk_iottwinmaker.types.pricing_bundles

        out["bundleNames"] = aws_sdk_iottwinmaker.types.pricing_bundles.serialize_json(
            value["bundle_names"]
        )
    return out


def deserialize_json(data: dict) -> UpdatePricingPlanRequest:
    out: UpdatePricingPlanRequest = {}  # type: ignore[typeddict-item]
    if "pricingMode" in data:
        out["pricing_mode"] = data["pricingMode"]
    else:
        raise DeserializationError("UpdatePricingPlanRequest.pricing_mode required")
    if "bundleNames" in data:
        import aws_sdk_iottwinmaker.types.pricing_bundles

        out["bundle_names"] = (
            aws_sdk_iottwinmaker.types.pricing_bundles.deserialize_json(
                data["bundleNames"]
            )
        )
    return out
