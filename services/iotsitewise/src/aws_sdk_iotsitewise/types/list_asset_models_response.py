"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssetModelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_model_summaries
    import aws_sdk_iotsitewise.types.next_token


class ListAssetModelsResponse(TypedDict, closed=True):
    asset_model_summaries: (
        "aws_sdk_iotsitewise.types.asset_model_summaries.AssetModelSummaries"
    )
    """<p>A list that summarizes each asset model.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetModelsResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.asset_model_summaries

    out["assetModelSummaries"] = (
        aws_sdk_iotsitewise.types.asset_model_summaries.serialize_json(
            value["asset_model_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssetModelsResponse:
    out: ListAssetModelsResponse = {}  # type: ignore[typeddict-item]
    if "assetModelSummaries" in data:
        import aws_sdk_iotsitewise.types.asset_model_summaries

        out["asset_model_summaries"] = (
            aws_sdk_iotsitewise.types.asset_model_summaries.deserialize_json(
                data["assetModelSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListAssetModelsResponse.asset_model_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
