"""Generated from Smithy shape ``com.amazonaws.outposts#CapacitySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.quote_capacity_list


class CapacitySummary(TypedDict, closed=True):
    existing_capacities: NotRequired[
        "capo_outposts.types.quote_capacity_list.QuoteCapacityList"
    ]
    """<p>The existing capacities on the Outpost before the quote is fulfilled.</p>"""
    final_capacities: NotRequired[
        "capo_outposts.types.quote_capacity_list.QuoteCapacityList"
    ]
    """<p>The final capacities on the Outpost after the quote is fulfilled.</p>"""
    capacity_change: NotRequired[
        "capo_outposts.types.quote_capacity_list.QuoteCapacityList"
    ]
    """<p>The change in capacity between the existing and final state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacitySummary) -> dict:
    out: dict = {}
    if "existing_capacities" in value:
        import capo_outposts.types.quote_capacity_list

        out["ExistingCapacities"] = (
            capo_outposts.types.quote_capacity_list.serialize_json(
                value["existing_capacities"]
            )
        )
    if "final_capacities" in value:
        import capo_outposts.types.quote_capacity_list

        out["FinalCapacities"] = capo_outposts.types.quote_capacity_list.serialize_json(
            value["final_capacities"]
        )
    if "capacity_change" in value:
        import capo_outposts.types.quote_capacity_list

        out["CapacityChange"] = capo_outposts.types.quote_capacity_list.serialize_json(
            value["capacity_change"]
        )
    return out


def deserialize_json(data: dict) -> CapacitySummary:
    out: CapacitySummary = {}  # type: ignore[typeddict-item]
    if "ExistingCapacities" in data:
        import capo_outposts.types.quote_capacity_list

        out["existing_capacities"] = (
            capo_outposts.types.quote_capacity_list.deserialize_json(
                data["ExistingCapacities"]
            )
        )
    if "FinalCapacities" in data:
        import capo_outposts.types.quote_capacity_list

        out["final_capacities"] = (
            capo_outposts.types.quote_capacity_list.deserialize_json(
                data["FinalCapacities"]
            )
        )
    if "CapacityChange" in data:
        import capo_outposts.types.quote_capacity_list

        out["capacity_change"] = (
            capo_outposts.types.quote_capacity_list.deserialize_json(
                data["CapacityChange"]
            )
        )
    return out
