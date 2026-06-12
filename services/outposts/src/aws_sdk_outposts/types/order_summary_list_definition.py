"""Generated from Smithy shape ``com.amazonaws.outposts#OrderSummaryListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.order_summary

OrderSummaryListDefinition: TypeAlias = list[
    "aws_sdk_outposts.types.order_summary.OrderSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrderSummaryListDefinition) -> list:
    import aws_sdk_outposts.types.order_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_outposts.types.order_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> OrderSummaryListDefinition:
    import aws_sdk_outposts.types.order_summary

    out: OrderSummaryListDefinition = []
    for item in data:
        out.append(aws_sdk_outposts.types.order_summary.deserialize_json(item))
    return out
