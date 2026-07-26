"""Generated from Smithy shape ``com.amazonaws.outposts#OrderSummaryListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.order_summary

OrderSummaryListDefinition: TypeAlias = list[
    "capo_outposts.types.order_summary.OrderSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrderSummaryListDefinition) -> list:
    import capo_outposts.types.order_summary

    out: list = []
    for item in value:
        out.append(capo_outposts.types.order_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> OrderSummaryListDefinition:
    import capo_outposts.types.order_summary

    out: OrderSummaryListDefinition = []
    for item in data:
        out.append(capo_outposts.types.order_summary.deserialize_json(item))
    return out
