"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListComponentTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_type_summaries
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.max_results
    import aws_sdk_iottwinmaker.types.next_token


class ListComponentTypesResponse(TypedDict, closed=True):
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace.</p>"""
    component_type_summaries: (
        "aws_sdk_iottwinmaker.types.component_type_summaries.ComponentTypeSummaries"
    )
    """<p>A list of objects that contain information about the component types.</p>"""
    next_token: NotRequired["aws_sdk_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_iottwinmaker.types.max_results.MaxResults"]
    """<p>Specifies the maximum number of results to display.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentTypesResponse) -> dict:
    out: dict = {}
    out["workspaceId"] = value["workspace_id"]
    import aws_sdk_iottwinmaker.types.component_type_summaries

    out["componentTypeSummaries"] = (
        aws_sdk_iottwinmaker.types.component_type_summaries.serialize_json(
            value["component_type_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListComponentTypesResponse:
    out: ListComponentTypesResponse = {}  # type: ignore[typeddict-item]
    if "workspaceId" in data:
        out["workspace_id"] = data["workspaceId"]
    else:
        raise DeserializationError("ListComponentTypesResponse.workspace_id required")
    if "componentTypeSummaries" in data:
        import aws_sdk_iottwinmaker.types.component_type_summaries

        out["component_type_summaries"] = (
            aws_sdk_iottwinmaker.types.component_type_summaries.deserialize_json(
                data["componentTypeSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListComponentTypesResponse.component_type_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
