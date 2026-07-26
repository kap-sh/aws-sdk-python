"""Generated from Smithy shape ``com.amazonaws.costexplorer#ListCostAllocationTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.cost_allocation_tag_key_list
    import capo_cost_explorer.types.cost_allocation_tag_status
    import capo_cost_explorer.types.cost_allocation_tag_type
    import capo_cost_explorer.types.cost_allocation_tags_max_results
    import capo_cost_explorer.types.next_page_token


class ListCostAllocationTagsRequest(TypedDict, closed=True):
    status: NotRequired[
        "capo_cost_explorer.types.cost_allocation_tag_status.CostAllocationTagStatus"
    ]
    """<p>The status of cost allocation tag keys that are returned for this request. </p>"""
    tag_keys: NotRequired[
        "capo_cost_explorer.types.cost_allocation_tag_key_list.CostAllocationTagKeyList"
    ]
    """<p>The list of cost allocation tag keys that are returned for this request. </p>"""
    type: NotRequired[
        "capo_cost_explorer.types.cost_allocation_tag_type.CostAllocationTagType"
    ]
    """<p>The type of <code>CostAllocationTag</code> object that are returned for this request. The <code>AWSGenerated</code> type tags are tags that Amazon Web Services defines and applies to support Amazon Web Services resources for cost allocation purposes. The <code>UserDefined</code> type tags are tags that you define, create, and apply to resources. </p>"""
    next_token: NotRequired["capo_cost_explorer.types.next_page_token.NextPageToken"]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>"""
    max_results: NotRequired[
        "capo_cost_explorer.types.cost_allocation_tags_max_results.CostAllocationTagsMaxResults"
    ]
    """<p>The maximum number of objects that are returned for this request. By default, the request returns 100 results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCostAllocationTagsRequest) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_cost_explorer.types.cost_allocation_tag_status

        out["Status"] = (
            capo_cost_explorer.types.cost_allocation_tag_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "tag_keys" in value:
        import capo_cost_explorer.types.cost_allocation_tag_key_list

        out["TagKeys"] = (
            capo_cost_explorer.types.cost_allocation_tag_key_list.serialize_aws_json_1_1(
                value["tag_keys"]
            )
        )
    if "type" in value:
        import capo_cost_explorer.types.cost_allocation_tag_type

        out["Type"] = (
            capo_cost_explorer.types.cost_allocation_tag_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCostAllocationTagsRequest:
    out: ListCostAllocationTagsRequest = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_cost_explorer.types.cost_allocation_tag_status

        out["status"] = (
            capo_cost_explorer.types.cost_allocation_tag_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "TagKeys" in data:
        import capo_cost_explorer.types.cost_allocation_tag_key_list

        out["tag_keys"] = (
            capo_cost_explorer.types.cost_allocation_tag_key_list.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    if "Type" in data:
        import capo_cost_explorer.types.cost_allocation_tag_type

        out["type"] = (
            capo_cost_explorer.types.cost_allocation_tag_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
