"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchPutAssetPropertyValueResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.batch_put_asset_property_error_entries


class BatchPutAssetPropertyValueResponse(TypedDict, closed=True):
    error_entries: "aws_sdk_iotsitewise.types.batch_put_asset_property_error_entries.BatchPutAssetPropertyErrorEntries"
    """<p>A list of the errors (if any) associated with the batch put request. Each error entry contains the <code>entryId</code> of the entry that failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutAssetPropertyValueResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.batch_put_asset_property_error_entries

    out["errorEntries"] = (
        aws_sdk_iotsitewise.types.batch_put_asset_property_error_entries.serialize_json(
            value["error_entries"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchPutAssetPropertyValueResponse:
    out: BatchPutAssetPropertyValueResponse = {}  # type: ignore[typeddict-item]
    if "errorEntries" in data:
        import aws_sdk_iotsitewise.types.batch_put_asset_property_error_entries

        out["error_entries"] = (
            aws_sdk_iotsitewise.types.batch_put_asset_property_error_entries.deserialize_json(
                data["errorEntries"]
            )
        )
    else:
        raise DeserializationError(
            "BatchPutAssetPropertyValueResponse.error_entries required"
        )
    return out
