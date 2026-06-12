"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssetRelationshipsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_relationship_summaries
    import aws_sdk_iotsitewise.types.next_token


class ListAssetRelationshipsResponse(TypedDict):
    asset_relationship_summaries: "aws_sdk_iotsitewise.types.asset_relationship_summaries.AssetRelationshipSummaries"
    """<p>A list that summarizes each asset relationship.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetRelationshipsResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.asset_relationship_summaries

    out["assetRelationshipSummaries"] = (
        aws_sdk_iotsitewise.types.asset_relationship_summaries.serialize_json(
            value["asset_relationship_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssetRelationshipsResponse:
    out: ListAssetRelationshipsResponse = {}  # type: ignore[typeddict-item]
    if "assetRelationshipSummaries" in data:
        import aws_sdk_iotsitewise.types.asset_relationship_summaries

        out["asset_relationship_summaries"] = (
            aws_sdk_iotsitewise.types.asset_relationship_summaries.deserialize_json(
                data["assetRelationshipSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListAssetRelationshipsResponse.asset_relationship_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
