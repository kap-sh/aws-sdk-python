"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListCustomLineItemsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.custom_line_item_list
    import aws_sdk_billingconductor.types.token


class ListCustomLineItemsOutput(TypedDict, closed=True):
    custom_line_items: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_list.CustomLineItemList"
    ]
    """<p> A list of <code>FreeFormLineItemListElements</code> received. </p>"""
    next_token: NotRequired["aws_sdk_billingconductor.types.token.Token"]
    """<p> The pagination token that's used on subsequent calls to get custom line items (FFLIs). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomLineItemsOutput) -> dict:
    out: dict = {}
    if "custom_line_items" in value:
        import aws_sdk_billingconductor.types.custom_line_item_list

        out["CustomLineItems"] = (
            aws_sdk_billingconductor.types.custom_line_item_list.serialize_json(
                value["custom_line_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCustomLineItemsOutput:
    out: ListCustomLineItemsOutput = {}  # type: ignore[typeddict-item]
    if "CustomLineItems" in data:
        import aws_sdk_billingconductor.types.custom_line_item_list

        out["custom_line_items"] = (
            aws_sdk_billingconductor.types.custom_line_item_list.deserialize_json(
                data["CustomLineItems"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
