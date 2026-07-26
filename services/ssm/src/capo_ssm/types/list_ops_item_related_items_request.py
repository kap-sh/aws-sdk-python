"""Generated from Smithy shape ``com.amazonaws.ssm#ListOpsItemRelatedItemsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_id
    import capo_ssm.types.ops_item_related_items_filters
    import capo_ssm.types.ops_item_related_items_max_results
    import capo_ssm.types.string


class ListOpsItemRelatedItemsRequest(TypedDict, closed=True):
    ops_item_id: NotRequired["capo_ssm.types.ops_item_id.OpsItemId"]
    """<p>The ID of the OpsItem for which you want to list all related-item resources.</p>"""
    filters: NotRequired[
        "capo_ssm.types.ops_item_related_items_filters.OpsItemRelatedItemsFilters"
    ]
    """<p>One or more OpsItem filters. Use a filter to return a more specific list of results. </p>"""
    max_results: NotRequired[
        "capo_ssm.types.ops_item_related_items_max_results.OpsItemRelatedItemsMaxResults"
    ]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_ssm.types.string.String"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOpsItemRelatedItemsRequest) -> dict:
    out: dict = {}
    if "ops_item_id" in value:
        out["OpsItemId"] = value["ops_item_id"]
    if "filters" in value:
        import capo_ssm.types.ops_item_related_items_filters

        out["Filters"] = (
            capo_ssm.types.ops_item_related_items_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOpsItemRelatedItemsRequest:
    out: ListOpsItemRelatedItemsRequest = {}  # type: ignore[typeddict-item]
    if "OpsItemId" in data:
        out["ops_item_id"] = data["OpsItemId"]
    if "Filters" in data:
        import capo_ssm.types.ops_item_related_items_filters

        out["filters"] = (
            capo_ssm.types.ops_item_related_items_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
