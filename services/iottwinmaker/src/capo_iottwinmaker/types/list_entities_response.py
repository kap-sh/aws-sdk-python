"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListEntitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.entity_summaries
    import capo_iottwinmaker.types.next_token


class ListEntitiesResponse(TypedDict, closed=True):
    entity_summaries: NotRequired[
        "capo_iottwinmaker.types.entity_summaries.EntitySummaries"
    ]
    """<p>A list of objects that contain information about the entities.</p>"""
    next_token: NotRequired["capo_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEntitiesResponse) -> dict:
    out: dict = {}
    if "entity_summaries" in value:
        import capo_iottwinmaker.types.entity_summaries

        out["entitySummaries"] = (
            capo_iottwinmaker.types.entity_summaries.serialize_json(
                value["entity_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEntitiesResponse:
    out: ListEntitiesResponse = {}  # type: ignore[typeddict-item]
    if "entitySummaries" in data:
        import capo_iottwinmaker.types.entity_summaries

        out["entity_summaries"] = (
            capo_iottwinmaker.types.entity_summaries.deserialize_json(
                data["entitySummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
