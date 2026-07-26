"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchPutAssetPropertyError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.batch_put_asset_property_value_error_code
    import capo_iotsitewise.types.error_message
    import capo_iotsitewise.types.timestamps


class BatchPutAssetPropertyError(TypedDict, closed=True):
    error_code: "capo_iotsitewise.types.batch_put_asset_property_value_error_code.BatchPutAssetPropertyValueErrorCode"
    """<p>The error code.</p>"""
    error_message: "capo_iotsitewise.types.error_message.ErrorMessage"
    """<p>The associated error message.</p>"""
    timestamps: "capo_iotsitewise.types.timestamps.Timestamps"
    """<p>A list of timestamps for each error, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutAssetPropertyError) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.batch_put_asset_property_value_error_code

    out["errorCode"] = (
        capo_iotsitewise.types.batch_put_asset_property_value_error_code.serialize_json(
            value["error_code"]
        )
    )
    out["errorMessage"] = value["error_message"]
    import capo_iotsitewise.types.timestamps

    out["timestamps"] = capo_iotsitewise.types.timestamps.serialize_json(
        value["timestamps"]
    )
    return out


def deserialize_json(data: dict) -> BatchPutAssetPropertyError:
    out: BatchPutAssetPropertyError = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        import capo_iotsitewise.types.batch_put_asset_property_value_error_code

        out["error_code"] = (
            capo_iotsitewise.types.batch_put_asset_property_value_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    else:
        raise DeserializationError("BatchPutAssetPropertyError.error_code required")
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    else:
        raise DeserializationError("BatchPutAssetPropertyError.error_message required")
    if "timestamps" in data:
        import capo_iotsitewise.types.timestamps

        out["timestamps"] = capo_iotsitewise.types.timestamps.deserialize_json(
            data["timestamps"]
        )
    else:
        raise DeserializationError("BatchPutAssetPropertyError.timestamps required")
    return out
