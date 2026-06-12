"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GetAssetPropertyValueHistoryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_property_value_history
    import aws_sdk_iotsitewise.types.next_token


class GetAssetPropertyValueHistoryResponse(TypedDict):
    asset_property_value_history: "aws_sdk_iotsitewise.types.asset_property_value_history.AssetPropertyValueHistory"
    """<p>The asset property's value history.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssetPropertyValueHistoryResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.asset_property_value_history

    out["assetPropertyValueHistory"] = (
        aws_sdk_iotsitewise.types.asset_property_value_history.serialize_json(
            value["asset_property_value_history"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetAssetPropertyValueHistoryResponse:
    out: GetAssetPropertyValueHistoryResponse = {}  # type: ignore[typeddict-item]
    if "assetPropertyValueHistory" in data:
        import aws_sdk_iotsitewise.types.asset_property_value_history

        out["asset_property_value_history"] = (
            aws_sdk_iotsitewise.types.asset_property_value_history.deserialize_json(
                data["assetPropertyValueHistory"]
            )
        )
    else:
        raise DeserializationError(
            "GetAssetPropertyValueHistoryResponse.asset_property_value_history required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
