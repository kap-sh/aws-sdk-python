"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListPurchaseOptionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.next_token
    import aws_sdk_marketplace_discovery.types.purchase_option_summary_list


class ListPurchaseOptionsOutput(TypedDict):
    purchase_options: NotRequired[
        "aws_sdk_marketplace_discovery.types.purchase_option_summary_list.PurchaseOptionSummaryList"
    ]
    """<p>The purchase options available to the buyer. Each option is either an offer for a single product or an offer set spanning multiple products.</p>"""
    next_token: NotRequired["aws_sdk_marketplace_discovery.types.next_token.NextToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPurchaseOptionsOutput) -> dict:
    out: dict = {}
    if "purchase_options" in value:
        import aws_sdk_marketplace_discovery.types.purchase_option_summary_list

        out["purchaseOptions"] = (
            aws_sdk_marketplace_discovery.types.purchase_option_summary_list.serialize_json(
                value["purchase_options"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPurchaseOptionsOutput:
    out: ListPurchaseOptionsOutput = {}  # type: ignore[typeddict-item]
    if "purchaseOptions" in data:
        import aws_sdk_marketplace_discovery.types.purchase_option_summary_list

        out["purchase_options"] = (
            aws_sdk_marketplace_discovery.types.purchase_option_summary_list.deserialize_json(
                data["purchaseOptions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
