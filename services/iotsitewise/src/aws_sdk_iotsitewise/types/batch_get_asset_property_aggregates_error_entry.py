"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyAggregatesErrorEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_error_code
    import aws_sdk_iotsitewise.types.entry_id
    import aws_sdk_iotsitewise.types.error_message


class BatchGetAssetPropertyAggregatesErrorEntry(TypedDict, closed=True):
    error_code: "aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_error_code.BatchGetAssetPropertyAggregatesErrorCode"
    """<p>The error code.</p>"""
    error_message: "aws_sdk_iotsitewise.types.error_message.ErrorMessage"
    """<p>The associated error message.</p>"""
    entry_id: "aws_sdk_iotsitewise.types.entry_id.EntryId"
    """<p>The ID of the entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyAggregatesErrorEntry) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_error_code

    out["errorCode"] = (
        aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_error_code.serialize_json(
            value["error_code"]
        )
    )
    out["errorMessage"] = value["error_message"]
    out["entryId"] = value["entry_id"]
    return out


def deserialize_json(data: dict) -> BatchGetAssetPropertyAggregatesErrorEntry:
    out: BatchGetAssetPropertyAggregatesErrorEntry = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        import aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_error_code

        out["error_code"] = (
            aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyAggregatesErrorEntry.error_code required"
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyAggregatesErrorEntry.error_message required"
        )
    if "entryId" in data:
        out["entry_id"] = data["entryId"]
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyAggregatesErrorEntry.entry_id required"
        )
    return out
