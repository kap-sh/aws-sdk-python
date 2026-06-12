"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_error_entries
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_skipped_entries
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_success_entries
    import aws_sdk_iotsitewise.types.next_token


class BatchGetAssetPropertyValueResponse(TypedDict):
    error_entries: "aws_sdk_iotsitewise.types.batch_get_asset_property_value_error_entries.BatchGetAssetPropertyValueErrorEntries"
    """<p>A list of the errors (if any) associated with the batch request. Each error entry contains the <code>entryId</code> of the entry that failed.</p>"""
    success_entries: "aws_sdk_iotsitewise.types.batch_get_asset_property_value_success_entries.BatchGetAssetPropertyValueSuccessEntries"
    """<p>A list of entries that were processed successfully by this batch request. Each success entry contains the <code>entryId</code> of the entry that succeeded and the latest query result.</p>"""
    skipped_entries: "aws_sdk_iotsitewise.types.batch_get_asset_property_value_skipped_entries.BatchGetAssetPropertyValueSkippedEntries"
    """<p>A list of entries that were not processed by this batch request. because these entries had been completely processed by previous paginated requests. Each skipped entry contains the <code>entryId</code> of the entry that skipped.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_error_entries

    out["errorEntries"] = (
        aws_sdk_iotsitewise.types.batch_get_asset_property_value_error_entries.serialize_json(
            value["error_entries"]
        )
    )
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_success_entries

    out["successEntries"] = (
        aws_sdk_iotsitewise.types.batch_get_asset_property_value_success_entries.serialize_json(
            value["success_entries"]
        )
    )
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_skipped_entries

    out["skippedEntries"] = (
        aws_sdk_iotsitewise.types.batch_get_asset_property_value_skipped_entries.serialize_json(
            value["skipped_entries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> BatchGetAssetPropertyValueResponse:
    out: BatchGetAssetPropertyValueResponse = {}  # type: ignore[typeddict-item]
    if "errorEntries" in data:
        import aws_sdk_iotsitewise.types.batch_get_asset_property_value_error_entries

        out["error_entries"] = (
            aws_sdk_iotsitewise.types.batch_get_asset_property_value_error_entries.deserialize_json(
                data["errorEntries"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyValueResponse.error_entries required"
        )
    if "successEntries" in data:
        import aws_sdk_iotsitewise.types.batch_get_asset_property_value_success_entries

        out["success_entries"] = (
            aws_sdk_iotsitewise.types.batch_get_asset_property_value_success_entries.deserialize_json(
                data["successEntries"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyValueResponse.success_entries required"
        )
    if "skippedEntries" in data:
        import aws_sdk_iotsitewise.types.batch_get_asset_property_value_skipped_entries

        out["skipped_entries"] = (
            aws_sdk_iotsitewise.types.batch_get_asset_property_value_skipped_entries.deserialize_json(
                data["skippedEntries"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyValueResponse.skipped_entries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
