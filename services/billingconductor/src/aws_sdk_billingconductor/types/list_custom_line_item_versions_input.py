"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListCustomLineItemVersionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.custom_line_item_arn
    import aws_sdk_billingconductor.types.list_custom_line_item_versions_filter
    import aws_sdk_billingconductor.types.max_custom_line_item_results
    import aws_sdk_billingconductor.types.token


class ListCustomLineItemVersionsInput(TypedDict):
    arn: "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn"
    """<p>The Amazon Resource Name (ARN) for the custom line item.</p>"""
    max_results: NotRequired[
        "aws_sdk_billingconductor.types.max_custom_line_item_results.MaxCustomLineItemResults"
    ]
    """<p>The maximum number of custom line item versions to retrieve.</p>"""
    next_token: NotRequired["aws_sdk_billingconductor.types.token.Token"]
    """<p>The pagination token that's used on subsequent calls to retrieve custom line item versions.</p>"""
    filters: NotRequired[
        "aws_sdk_billingconductor.types.list_custom_line_item_versions_filter.ListCustomLineItemVersionsFilter"
    ]
    """<p>A <code>ListCustomLineItemVersionsFilter</code> that specifies the billing period range in which the custom line item versions are applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomLineItemVersionsInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import aws_sdk_billingconductor.types.list_custom_line_item_versions_filter

        out["Filters"] = (
            aws_sdk_billingconductor.types.list_custom_line_item_versions_filter.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCustomLineItemVersionsInput:
    out: ListCustomLineItemVersionsInput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ListCustomLineItemVersionsInput.arn required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filters" in data:
        import aws_sdk_billingconductor.types.list_custom_line_item_versions_filter

        out["filters"] = (
            aws_sdk_billingconductor.types.list_custom_line_item_versions_filter.deserialize_json(
                data["Filters"]
            )
        )
    return out
