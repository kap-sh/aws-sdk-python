"""Generated from Smithy shape ``com.amazonaws.outposts#GetRenewalPricingOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.pricing_option_list
    import capo_outposts.types.pricing_result


class GetRenewalPricingOutput(TypedDict, closed=True):
    pricing_result: NotRequired["capo_outposts.types.pricing_result.PricingResult"]
    """<p>The result of the pricing request.</p>"""
    pricing_options: NotRequired[
        "capo_outposts.types.pricing_option_list.PricingOptionList"
    ]
    """<p>The pricing options for the specified Outpost.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRenewalPricingOutput) -> dict:
    out: dict = {}
    if "pricing_result" in value:
        import capo_outposts.types.pricing_result

        out["PricingResult"] = capo_outposts.types.pricing_result.serialize_json(
            value["pricing_result"]
        )
    if "pricing_options" in value:
        import capo_outposts.types.pricing_option_list

        out["PricingOptions"] = capo_outposts.types.pricing_option_list.serialize_json(
            value["pricing_options"]
        )
    return out


def deserialize_json(data: dict) -> GetRenewalPricingOutput:
    out: GetRenewalPricingOutput = {}  # type: ignore[typeddict-item]
    if "PricingResult" in data:
        import capo_outposts.types.pricing_result

        out["pricing_result"] = capo_outposts.types.pricing_result.deserialize_json(
            data["PricingResult"]
        )
    if "PricingOptions" in data:
        import capo_outposts.types.pricing_option_list

        out["pricing_options"] = (
            capo_outposts.types.pricing_option_list.deserialize_json(
                data["PricingOptions"]
            )
        )
    return out
