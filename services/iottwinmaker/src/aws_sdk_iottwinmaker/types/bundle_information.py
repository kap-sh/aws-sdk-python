"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#BundleInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.pricing_bundles
    import aws_sdk_iottwinmaker.types.pricing_tier


class BundleInformation(TypedDict, closed=True):
    bundle_names: "aws_sdk_iottwinmaker.types.pricing_bundles.PricingBundles"
    """<p>The bundle names.</p>"""
    pricing_tier: NotRequired["aws_sdk_iottwinmaker.types.pricing_tier.PricingTier"]
    """<p>The pricing tier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BundleInformation) -> dict:
    out: dict = {}
    import aws_sdk_iottwinmaker.types.pricing_bundles

    out["bundleNames"] = aws_sdk_iottwinmaker.types.pricing_bundles.serialize_json(
        value["bundle_names"]
    )
    if "pricing_tier" in value:
        out["pricingTier"] = value["pricing_tier"]
    return out


def deserialize_json(data: dict) -> BundleInformation:
    out: BundleInformation = {}  # type: ignore[typeddict-item]
    if "bundleNames" in data:
        import aws_sdk_iottwinmaker.types.pricing_bundles

        out["bundle_names"] = (
            aws_sdk_iottwinmaker.types.pricing_bundles.deserialize_json(
                data["bundleNames"]
            )
        )
    else:
        raise DeserializationError("BundleInformation.bundle_names required")
    if "pricingTier" in data:
        out["pricing_tier"] = data["pricingTier"]
    return out
