"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueSkippedEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.batch_entry_completion_status
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_error_info
    import aws_sdk_iotsitewise.types.entry_id


class BatchGetAssetPropertyValueSkippedEntry(TypedDict, closed=True):
    entry_id: "aws_sdk_iotsitewise.types.entry_id.EntryId"
    """<p>The ID of the entry.</p>"""
    completion_status: "aws_sdk_iotsitewise.types.batch_entry_completion_status.BatchEntryCompletionStatus"
    r"""<p>The completion status of each entry that is associated with the <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyValue.html\">BatchGetAssetPropertyValue</a> request.</p>"""
    error_info: NotRequired[
        "aws_sdk_iotsitewise.types.batch_get_asset_property_value_error_info.BatchGetAssetPropertyValueErrorInfo"
    ]
    """<p>The error information, such as the error code and the timestamp.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueSkippedEntry) -> dict:
    out: dict = {}
    out["entryId"] = value["entry_id"]
    import aws_sdk_iotsitewise.types.batch_entry_completion_status

    out["completionStatus"] = (
        aws_sdk_iotsitewise.types.batch_entry_completion_status.serialize_json(
            value["completion_status"]
        )
    )
    if "error_info" in value:
        import aws_sdk_iotsitewise.types.batch_get_asset_property_value_error_info

        out["errorInfo"] = (
            aws_sdk_iotsitewise.types.batch_get_asset_property_value_error_info.serialize_json(
                value["error_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetAssetPropertyValueSkippedEntry:
    out: BatchGetAssetPropertyValueSkippedEntry = {}  # type: ignore[typeddict-item]
    if "entryId" in data:
        out["entry_id"] = data["entryId"]
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyValueSkippedEntry.entry_id required"
        )
    if "completionStatus" in data:
        import aws_sdk_iotsitewise.types.batch_entry_completion_status

        out["completion_status"] = (
            aws_sdk_iotsitewise.types.batch_entry_completion_status.deserialize_json(
                data["completionStatus"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyValueSkippedEntry.completion_status required"
        )
    if "errorInfo" in data:
        import aws_sdk_iotsitewise.types.batch_get_asset_property_value_error_info

        out["error_info"] = (
            aws_sdk_iotsitewise.types.batch_get_asset_property_value_error_info.deserialize_json(
                data["errorInfo"]
            )
        )
    return out
