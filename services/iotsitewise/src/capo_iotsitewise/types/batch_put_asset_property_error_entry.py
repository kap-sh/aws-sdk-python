"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchPutAssetPropertyErrorEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.batch_put_asset_property_errors
    import capo_iotsitewise.types.entry_id


class BatchPutAssetPropertyErrorEntry(TypedDict, closed=True):
    entry_id: "capo_iotsitewise.types.entry_id.EntryId"
    """<p>The ID of the failed entry.</p>"""
    errors: "capo_iotsitewise.types.batch_put_asset_property_errors.BatchPutAssetPropertyErrors"
    """<p>The list of update property value errors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutAssetPropertyErrorEntry) -> dict:
    out: dict = {}
    out["entryId"] = value["entry_id"]
    import capo_iotsitewise.types.batch_put_asset_property_errors

    out["errors"] = (
        capo_iotsitewise.types.batch_put_asset_property_errors.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchPutAssetPropertyErrorEntry:
    out: BatchPutAssetPropertyErrorEntry = {}  # type: ignore[typeddict-item]
    if "entryId" in data:
        out["entry_id"] = data["entryId"]
    else:
        raise DeserializationError("BatchPutAssetPropertyErrorEntry.entry_id required")
    if "errors" in data:
        import capo_iotsitewise.types.batch_put_asset_property_errors

        out["errors"] = (
            capo_iotsitewise.types.batch_put_asset_property_errors.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError("BatchPutAssetPropertyErrorEntry.errors required")
    return out
