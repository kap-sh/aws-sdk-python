"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ListServiceIndexesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.region_list


class ListServiceIndexesInput(TypedDict, closed=True):
    regions: NotRequired["aws_sdk_resource_explorer_2.types.region_list.RegionList"]
    """<p>A list of Amazon Web Services Regions to include in the search for indexes. If not specified, indexes from all Regions are returned.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of index results to return in a single response. Valid values are between <code>1</code> and <code>100</code>.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token from a previous <code>ListServiceIndexes</code> response. Use this token to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceIndexesInput) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> ListServiceIndexesInput:
    out: ListServiceIndexesInput = {}  # type: ignore[typeddict-item]
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
