"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListCompositionRelationshipsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.composition_relationship_summaries
    import capo_iotsitewise.types.next_token


class ListCompositionRelationshipsResponse(TypedDict, closed=True):
    composition_relationship_summaries: "capo_iotsitewise.types.composition_relationship_summaries.CompositionRelationshipSummaries"
    """<p>A list that summarizes each composition relationship.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCompositionRelationshipsResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.composition_relationship_summaries

    out["compositionRelationshipSummaries"] = (
        capo_iotsitewise.types.composition_relationship_summaries.serialize_json(
            value["composition_relationship_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCompositionRelationshipsResponse:
    out: ListCompositionRelationshipsResponse = {}  # type: ignore[typeddict-item]
    if "compositionRelationshipSummaries" in data:
        import capo_iotsitewise.types.composition_relationship_summaries

        out["composition_relationship_summaries"] = (
            capo_iotsitewise.types.composition_relationship_summaries.deserialize_json(
                data["compositionRelationshipSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListCompositionRelationshipsResponse.composition_relationship_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
