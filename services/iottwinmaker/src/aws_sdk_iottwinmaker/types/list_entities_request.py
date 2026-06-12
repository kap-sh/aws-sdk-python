"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListEntitiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.list_entities_filters
    import aws_sdk_iottwinmaker.types.max_results
    import aws_sdk_iottwinmaker.types.next_token


class ListEntitiesRequest(TypedDict):
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace.</p>"""
    filters: NotRequired[
        "aws_sdk_iottwinmaker.types.list_entities_filters.ListEntitiesFilters"
    ]
    """<p>A list of objects that filter the request.</p> <note> <p>Only one object is accepted as a valid input.</p> </note>"""
    max_results: NotRequired["aws_sdk_iottwinmaker.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time. The default is 25.</p> <p>Valid Range: Minimum value of 1. Maximum value of 250.</p>"""
    next_token: NotRequired["aws_sdk_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEntitiesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_iottwinmaker.types.list_entities_filters

        out["filters"] = (
            aws_sdk_iottwinmaker.types.list_entities_filters.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEntitiesRequest:
    out: ListEntitiesRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_iottwinmaker.types.list_entities_filters

        out["filters"] = (
            aws_sdk_iottwinmaker.types.list_entities_filters.deserialize_json(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
