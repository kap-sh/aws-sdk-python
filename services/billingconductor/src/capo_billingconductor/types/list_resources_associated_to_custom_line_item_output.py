"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListResourcesAssociatedToCustomLineItemOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_line_item_arn
    import capo_billingconductor.types.list_resources_associated_to_custom_line_item_response_list
    import capo_billingconductor.types.token


class ListResourcesAssociatedToCustomLineItemOutput(TypedDict, closed=True):
    arn: NotRequired[
        "capo_billingconductor.types.custom_line_item_arn.CustomLineItemArn"
    ]
    """<p> The custom line item ARN for which the resource associations are listed. </p>"""
    associated_resources: NotRequired[
        "capo_billingconductor.types.list_resources_associated_to_custom_line_item_response_list.ListResourcesAssociatedToCustomLineItemResponseList"
    ]
    """<p> A list of <code>ListResourcesAssociatedToCustomLineItemResponseElement</code> for each resource association retrieved. </p>"""
    next_token: NotRequired["capo_billingconductor.types.token.Token"]
    """<p> The pagination token to be used in subsequent requests to retrieve additional results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcesAssociatedToCustomLineItemOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "associated_resources" in value:
        import capo_billingconductor.types.list_resources_associated_to_custom_line_item_response_list

        out["AssociatedResources"] = (
            capo_billingconductor.types.list_resources_associated_to_custom_line_item_response_list.serialize_json(
                value["associated_resources"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourcesAssociatedToCustomLineItemOutput:
    out: ListResourcesAssociatedToCustomLineItemOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AssociatedResources" in data:
        import capo_billingconductor.types.list_resources_associated_to_custom_line_item_response_list

        out["associated_resources"] = (
            capo_billingconductor.types.list_resources_associated_to_custom_line_item_response_list.deserialize_json(
                data["AssociatedResources"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
