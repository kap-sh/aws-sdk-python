"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueSuccessEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_property_value
    import aws_sdk_iotsitewise.types.entry_id


class BatchGetAssetPropertyValueSuccessEntry(TypedDict):
    entry_id: "aws_sdk_iotsitewise.types.entry_id.EntryId"
    """<p>The ID of the entry.</p>"""
    asset_property_value: NotRequired[
        "aws_sdk_iotsitewise.types.asset_property_value.AssetPropertyValue"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueSuccessEntry) -> dict:
    out: dict = {}
    out["entryId"] = value["entry_id"]
    if "asset_property_value" in value:
        import aws_sdk_iotsitewise.types.asset_property_value

        out["assetPropertyValue"] = (
            aws_sdk_iotsitewise.types.asset_property_value.serialize_json(
                value["asset_property_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetAssetPropertyValueSuccessEntry:
    out: BatchGetAssetPropertyValueSuccessEntry = {}  # type: ignore[typeddict-item]
    if "entryId" in data:
        out["entry_id"] = data["entryId"]
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyValueSuccessEntry.entry_id required"
        )
    if "assetPropertyValue" in data:
        import aws_sdk_iotsitewise.types.asset_property_value

        out["asset_property_value"] = (
            aws_sdk_iotsitewise.types.asset_property_value.deserialize_json(
                data["assetPropertyValue"]
            )
        )
    return out
