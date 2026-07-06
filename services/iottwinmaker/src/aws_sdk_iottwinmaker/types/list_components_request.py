"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListComponentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_path
    import aws_sdk_iottwinmaker.types.entity_id
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.max_results
    import aws_sdk_iottwinmaker.types.next_token


class ListComponentsRequest(TypedDict, closed=True):
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The workspace ID.</p>"""
    entity_id: "aws_sdk_iottwinmaker.types.entity_id.EntityId"
    """<p>The ID for the entity whose metadata (component/properties) is returned by the operation.</p>"""
    component_path: NotRequired[
        "aws_sdk_iottwinmaker.types.component_path.ComponentPath"
    ]
    """<p>This string specifies the path to the composite component, starting from the top-level component.</p>"""
    max_results: NotRequired["aws_sdk_iottwinmaker.types.max_results.MaxResults"]
    """<p>The maximum number of results returned at one time. The default is 25.</p>"""
    next_token: NotRequired["aws_sdk_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentsRequest) -> dict:
    out: dict = {}
    if "component_path" in value:
        out["componentPath"] = value["component_path"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListComponentsRequest:
    out: ListComponentsRequest = {}  # type: ignore[typeddict-item]
    if "componentPath" in data:
        out["component_path"] = data["componentPath"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
