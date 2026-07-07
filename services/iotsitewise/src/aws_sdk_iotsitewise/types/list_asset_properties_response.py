"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssetPropertiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_property_summaries
    import aws_sdk_iotsitewise.types.next_token


class ListAssetPropertiesResponse(TypedDict, closed=True):
    asset_property_summaries: (
        "aws_sdk_iotsitewise.types.asset_property_summaries.AssetPropertySummaries"
    )
    """<p>A list that summarizes the properties associated with the specified asset.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetPropertiesResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.asset_property_summaries

    out["assetPropertySummaries"] = (
        aws_sdk_iotsitewise.types.asset_property_summaries.serialize_json(
            value["asset_property_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssetPropertiesResponse:
    out: ListAssetPropertiesResponse = {}  # type: ignore[typeddict-item]
    if "assetPropertySummaries" in data:
        import aws_sdk_iotsitewise.types.asset_property_summaries

        out["asset_property_summaries"] = (
            aws_sdk_iotsitewise.types.asset_property_summaries.deserialize_json(
                data["assetPropertySummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListAssetPropertiesResponse.asset_property_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
