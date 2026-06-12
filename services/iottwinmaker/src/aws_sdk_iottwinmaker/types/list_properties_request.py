"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListPropertiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_path
    import aws_sdk_iottwinmaker.types.entity_id
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.max_results
    import aws_sdk_iottwinmaker.types.name
    import aws_sdk_iottwinmaker.types.next_token


class ListPropertiesRequest(TypedDict):
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The workspace ID.</p>"""
    component_name: NotRequired["aws_sdk_iottwinmaker.types.name.Name"]
    """<p>The name of the component whose properties are returned by the operation.</p>"""
    component_path: NotRequired[
        "aws_sdk_iottwinmaker.types.component_path.ComponentPath"
    ]
    """<p>This string specifies the path to the composite component, starting from the top-level component.</p>"""
    entity_id: "aws_sdk_iottwinmaker.types.entity_id.EntityId"
    """<p>The ID for the entity whose metadata (component/properties) is returned by the operation.</p>"""
    max_results: NotRequired["aws_sdk_iottwinmaker.types.max_results.MaxResults"]
    """<p>The maximum number of results returned at one time. The default is 25.</p>"""
    next_token: NotRequired["aws_sdk_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPropertiesRequest) -> dict:
    out: dict = {}
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    if "component_path" in value:
        out["componentPath"] = value["component_path"]
    out["entityId"] = value["entity_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPropertiesRequest:
    out: ListPropertiesRequest = {}  # type: ignore[typeddict-item]
    if "componentName" in data:
        out["component_name"] = data["componentName"]
    if "componentPath" in data:
        out["component_path"] = data["componentPath"]
    if "entityId" in data:
        out["entity_id"] = data["entityId"]
    else:
        raise DeserializationError("ListPropertiesRequest.entity_id required")
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
