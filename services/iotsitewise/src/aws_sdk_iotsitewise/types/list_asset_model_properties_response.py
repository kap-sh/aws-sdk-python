"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssetModelPropertiesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_model_property_summaries
    import aws_sdk_iotsitewise.types.next_token


class ListAssetModelPropertiesResponse(TypedDict):
    asset_model_property_summaries: "aws_sdk_iotsitewise.types.asset_model_property_summaries.AssetModelPropertySummaries"
    """<p>A list that summarizes the properties associated with the specified asset model.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetModelPropertiesResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.asset_model_property_summaries

    out["assetModelPropertySummaries"] = (
        aws_sdk_iotsitewise.types.asset_model_property_summaries.serialize_json(
            value["asset_model_property_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssetModelPropertiesResponse:
    out: ListAssetModelPropertiesResponse = {}  # type: ignore[typeddict-item]
    if "assetModelPropertySummaries" in data:
        import aws_sdk_iotsitewise.types.asset_model_property_summaries

        out["asset_model_property_summaries"] = (
            aws_sdk_iotsitewise.types.asset_model_property_summaries.deserialize_json(
                data["assetModelPropertySummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListAssetModelPropertiesResponse.asset_model_property_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
