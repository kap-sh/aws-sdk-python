"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.capacity_summary
    import capo_outposts.types.pricing_option_list
    import capo_outposts.types.quote_capacity_list
    import capo_outposts.types.quote_option_identifier
    import capo_outposts.types.quote_specification_list


class QuoteOption(TypedDict, closed=True):
    quote_option_identifier: NotRequired[
        "capo_outposts.types.quote_option_identifier.QuoteOptionIdentifier"
    ]
    """<p>The ID of the quote option.</p>"""
    capacities: NotRequired["capo_outposts.types.quote_capacity_list.QuoteCapacityList"]
    """<p>The capacities included in this quote option.</p>"""
    capacity_summary: NotRequired[
        "capo_outposts.types.capacity_summary.CapacitySummary"
    ]
    """<p>A summary of the existing, final, and changed capacity for this quote option.</p>"""
    specifications: NotRequired[
        "capo_outposts.types.quote_specification_list.QuoteSpecificationList"
    ]
    """<p>The physical specifications for the racks or servers in this quote option.</p>"""
    pricing_options: NotRequired[
        "capo_outposts.types.pricing_option_list.PricingOptionList"
    ]
    """<p>The pricing options for this quote option.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuoteOption) -> dict:
    out: dict = {}
    if "quote_option_identifier" in value:
        out["QuoteOptionIdentifier"] = value["quote_option_identifier"]
    if "capacities" in value:
        import capo_outposts.types.quote_capacity_list

        out["Capacities"] = capo_outposts.types.quote_capacity_list.serialize_json(
            value["capacities"]
        )
    if "capacity_summary" in value:
        import capo_outposts.types.capacity_summary

        out["CapacitySummary"] = capo_outposts.types.capacity_summary.serialize_json(
            value["capacity_summary"]
        )
    if "specifications" in value:
        import capo_outposts.types.quote_specification_list

        out["Specifications"] = (
            capo_outposts.types.quote_specification_list.serialize_json(
                value["specifications"]
            )
        )
    if "pricing_options" in value:
        import capo_outposts.types.pricing_option_list

        out["PricingOptions"] = capo_outposts.types.pricing_option_list.serialize_json(
            value["pricing_options"]
        )
    return out


def deserialize_json(data: dict) -> QuoteOption:
    out: QuoteOption = {}  # type: ignore[typeddict-item]
    if "QuoteOptionIdentifier" in data:
        out["quote_option_identifier"] = data["QuoteOptionIdentifier"]
    if "Capacities" in data:
        import capo_outposts.types.quote_capacity_list

        out["capacities"] = capo_outposts.types.quote_capacity_list.deserialize_json(
            data["Capacities"]
        )
    if "CapacitySummary" in data:
        import capo_outposts.types.capacity_summary

        out["capacity_summary"] = capo_outposts.types.capacity_summary.deserialize_json(
            data["CapacitySummary"]
        )
    if "Specifications" in data:
        import capo_outposts.types.quote_specification_list

        out["specifications"] = (
            capo_outposts.types.quote_specification_list.deserialize_json(
                data["Specifications"]
            )
        )
    if "PricingOptions" in data:
        import capo_outposts.types.pricing_option_list

        out["pricing_options"] = (
            capo_outposts.types.pricing_option_list.deserialize_json(
                data["PricingOptions"]
            )
        )
    return out
