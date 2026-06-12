"""Generated from Smithy shape ``com.amazonaws.outposts#ListOrdersOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.order_summary_list_definition
    import aws_sdk_outposts.types.token


class ListOrdersOutput(TypedDict):
    orders: NotRequired[
        "aws_sdk_outposts.types.order_summary_list_definition.OrderSummaryListDefinition"
    ]
    """<p> Information about the orders. </p>"""
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOrdersOutput) -> dict:
    out: dict = {}
    if "orders" in value:
        import aws_sdk_outposts.types.order_summary_list_definition

        out["Orders"] = (
            aws_sdk_outposts.types.order_summary_list_definition.serialize_json(
                value["orders"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOrdersOutput:
    out: ListOrdersOutput = {}  # type: ignore[typeddict-item]
    if "Orders" in data:
        import aws_sdk_outposts.types.order_summary_list_definition

        out["orders"] = (
            aws_sdk_outposts.types.order_summary_list_definition.deserialize_json(
                data["Orders"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
