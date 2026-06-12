"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListResourcesAssociatedToCustomLineItemInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_period
    import aws_sdk_billingconductor.types.custom_line_item_arn
    import aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_filter
    import aws_sdk_billingconductor.types.max_custom_line_item_results
    import aws_sdk_billingconductor.types.token


class ListResourcesAssociatedToCustomLineItemInput(TypedDict):
    billing_period: NotRequired[
        "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p> The billing period for which the resource associations will be listed. </p>"""
    arn: "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn"
    """<p> The ARN of the custom line item for which the resource associations will be listed. </p>"""
    max_results: NotRequired[
        "aws_sdk_billingconductor.types.max_custom_line_item_results.MaxCustomLineItemResults"
    ]
    """<p> (Optional) The maximum number of resource associations to be retrieved. </p>"""
    next_token: NotRequired["aws_sdk_billingconductor.types.token.Token"]
    """<p> (Optional) The pagination token that's returned by a previous request. </p>"""
    filters: NotRequired[
        "aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_filter.ListResourcesAssociatedToCustomLineItemFilter"
    ]
    """<p> (Optional) A <code>ListResourcesAssociatedToCustomLineItemFilter</code> that can specify the types of resources that should be retrieved. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcesAssociatedToCustomLineItemInput) -> dict:
    out: dict = {}
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    out["Arn"] = value["arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_filter

        out["Filters"] = (
            aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_filter.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListResourcesAssociatedToCustomLineItemInput:
    out: ListResourcesAssociatedToCustomLineItemInput = {}  # type: ignore[typeddict-item]
    if "BillingPeriod" in data:
        out["billing_period"] = data["BillingPeriod"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError(
            "ListResourcesAssociatedToCustomLineItemInput.arn required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filters" in data:
        import aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_filter

        out["filters"] = (
            aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_filter.deserialize_json(
                data["Filters"]
            )
        )
    return out
