"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListInterfaceRelationshipsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.interface_relationship_summaries
    import aws_sdk_iotsitewise.types.next_token


class ListInterfaceRelationshipsResponse(TypedDict, closed=True):
    interface_relationship_summaries: "aws_sdk_iotsitewise.types.interface_relationship_summaries.InterfaceRelationshipSummaries"
    """<p>A list that summarizes each interface relationship.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInterfaceRelationshipsResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.interface_relationship_summaries

    out["interfaceRelationshipSummaries"] = (
        aws_sdk_iotsitewise.types.interface_relationship_summaries.serialize_json(
            value["interface_relationship_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInterfaceRelationshipsResponse:
    out: ListInterfaceRelationshipsResponse = {}  # type: ignore[typeddict-item]
    if "interfaceRelationshipSummaries" in data:
        import aws_sdk_iotsitewise.types.interface_relationship_summaries

        out["interface_relationship_summaries"] = (
            aws_sdk_iotsitewise.types.interface_relationship_summaries.deserialize_json(
                data["interfaceRelationshipSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListInterfaceRelationshipsResponse.interface_relationship_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
