"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssociatedAssetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.associated_assets_summaries
    import aws_sdk_iotsitewise.types.next_token


class ListAssociatedAssetsResponse(TypedDict):
    asset_summaries: "aws_sdk_iotsitewise.types.associated_assets_summaries.AssociatedAssetsSummaries"
    """<p>A list that summarizes the associated assets.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociatedAssetsResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.associated_assets_summaries

    out["assetSummaries"] = (
        aws_sdk_iotsitewise.types.associated_assets_summaries.serialize_json(
            value["asset_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssociatedAssetsResponse:
    out: ListAssociatedAssetsResponse = {}  # type: ignore[typeddict-item]
    if "assetSummaries" in data:
        import aws_sdk_iotsitewise.types.associated_assets_summaries

        out["asset_summaries"] = (
            aws_sdk_iotsitewise.types.associated_assets_summaries.deserialize_json(
                data["assetSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListAssociatedAssetsResponse.asset_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
