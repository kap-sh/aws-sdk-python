"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListComponentTypesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.list_component_types_filters
    import aws_sdk_iottwinmaker.types.max_results
    import aws_sdk_iottwinmaker.types.next_token


class ListComponentTypesRequest(TypedDict, closed=True):
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace.</p>"""
    filters: NotRequired[
        "aws_sdk_iottwinmaker.types.list_component_types_filters.ListComponentTypesFilters"
    ]
    """<p>A list of objects that filter the request.</p>"""
    next_token: NotRequired["aws_sdk_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_iottwinmaker.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time. The default is 25.</p> <p>Valid Range: Minimum value of 1. Maximum value of 250.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentTypesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_iottwinmaker.types.list_component_types_filters

        out["filters"] = (
            aws_sdk_iottwinmaker.types.list_component_types_filters.serialize_json(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListComponentTypesRequest:
    out: ListComponentTypesRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_iottwinmaker.types.list_component_types_filters

        out["filters"] = (
            aws_sdk_iottwinmaker.types.list_component_types_filters.deserialize_json(
                data["filters"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
