"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListEntitiesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.entity_summaries
    import aws_sdk_iottwinmaker.types.next_token


class ListEntitiesResponse(TypedDict):
    entity_summaries: NotRequired[
        "aws_sdk_iottwinmaker.types.entity_summaries.EntitySummaries"
    ]
    """<p>A list of objects that contain information about the entities.</p>"""
    next_token: NotRequired["aws_sdk_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEntitiesResponse) -> dict:
    out: dict = {}
    if "entity_summaries" in value:
        import aws_sdk_iottwinmaker.types.entity_summaries

        out["entitySummaries"] = (
            aws_sdk_iottwinmaker.types.entity_summaries.serialize_json(
                value["entity_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEntitiesResponse:
    out: ListEntitiesResponse = {}  # type: ignore[typeddict-item]
    if "entitySummaries" in data:
        import aws_sdk_iottwinmaker.types.entity_summaries

        out["entity_summaries"] = (
            aws_sdk_iottwinmaker.types.entity_summaries.deserialize_json(
                data["entitySummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
