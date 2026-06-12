"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueHistorySuccessEntry``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_property_value_history
    import aws_sdk_iotsitewise.types.entry_id


class BatchGetAssetPropertyValueHistorySuccessEntry(TypedDict):
    entry_id: "aws_sdk_iotsitewise.types.entry_id.EntryId"
    """<p>The ID of the entry.</p>"""
    asset_property_value_history: "aws_sdk_iotsitewise.types.asset_property_value_history.AssetPropertyValueHistory"
    """<p>The requested historical values for the specified asset property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueHistorySuccessEntry) -> dict:
    out: dict = {}
    out["entryId"] = value["entry_id"]
    import aws_sdk_iotsitewise.types.asset_property_value_history

    out["assetPropertyValueHistory"] = (
        aws_sdk_iotsitewise.types.asset_property_value_history.serialize_json(
            value["asset_property_value_history"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetAssetPropertyValueHistorySuccessEntry:
    out: BatchGetAssetPropertyValueHistorySuccessEntry = {}  # type: ignore[typeddict-item]
    if "entryId" in data:
        out["entry_id"] = data["entryId"]
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyValueHistorySuccessEntry.entry_id required"
        )
    if "assetPropertyValueHistory" in data:
        import aws_sdk_iotsitewise.types.asset_property_value_history

        out["asset_property_value_history"] = (
            aws_sdk_iotsitewise.types.asset_property_value_history.deserialize_json(
                data["assetPropertyValueHistory"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyValueHistorySuccessEntry.asset_property_value_history required"
        )
    return out
