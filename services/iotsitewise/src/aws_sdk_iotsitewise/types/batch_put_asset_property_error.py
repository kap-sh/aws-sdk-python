"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchPutAssetPropertyError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.batch_put_asset_property_value_error_code
    import aws_sdk_iotsitewise.types.error_message
    import aws_sdk_iotsitewise.types.timestamps


class BatchPutAssetPropertyError(TypedDict):
    error_code: "aws_sdk_iotsitewise.types.batch_put_asset_property_value_error_code.BatchPutAssetPropertyValueErrorCode"
    """<p>The error code.</p>"""
    error_message: "aws_sdk_iotsitewise.types.error_message.ErrorMessage"
    """<p>The associated error message.</p>"""
    timestamps: "aws_sdk_iotsitewise.types.timestamps.Timestamps"
    """<p>A list of timestamps for each error, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutAssetPropertyError) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.batch_put_asset_property_value_error_code

    out["errorCode"] = (
        aws_sdk_iotsitewise.types.batch_put_asset_property_value_error_code.serialize_json(
            value["error_code"]
        )
    )
    out["errorMessage"] = value["error_message"]
    import aws_sdk_iotsitewise.types.timestamps

    out["timestamps"] = aws_sdk_iotsitewise.types.timestamps.serialize_json(
        value["timestamps"]
    )
    return out


def deserialize_json(data: dict) -> BatchPutAssetPropertyError:
    out: BatchPutAssetPropertyError = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        import aws_sdk_iotsitewise.types.batch_put_asset_property_value_error_code

        out["error_code"] = (
            aws_sdk_iotsitewise.types.batch_put_asset_property_value_error_code.deserialize_json(
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
        import aws_sdk_iotsitewise.types.timestamps

        out["timestamps"] = aws_sdk_iotsitewise.types.timestamps.deserialize_json(
            data["timestamps"]
        )
    else:
        raise DeserializationError("BatchPutAssetPropertyError.timestamps required")
    return out
