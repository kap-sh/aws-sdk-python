"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ListIndexesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.index_type
    import aws_sdk_resource_explorer_2.types.region_list


class ListIndexesInput(TypedDict, closed=True):
    type: NotRequired["aws_sdk_resource_explorer_2.types.index_type.IndexType"]
    """<p>If specified, limits the output to only indexes of the specified Type, either <code>LOCAL</code> or <code>AGGREGATOR</code>.</p> <p>Use this option to discover the aggregator index for your account.</p>"""
    regions: NotRequired["aws_sdk_resource_explorer_2.types.region_list.RegionList"]
    """<p>If specified, limits the response to only information about the index in the specified list of Amazon Web Services Regions.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>"""
    next_token: NotRequired["str"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIndexesInput) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "regions" in value:
        import aws_sdk_resource_explorer_2.types.region_list

        out["Regions"] = aws_sdk_resource_explorer_2.types.region_list.serialize_json(
            value["regions"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIndexesInput:
    out: ListIndexesInput = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Regions" in data:
        import aws_sdk_resource_explorer_2.types.region_list

        out["regions"] = aws_sdk_resource_explorer_2.types.region_list.deserialize_json(
            data["Regions"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
