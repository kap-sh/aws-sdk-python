"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyAggregatesErrorInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_error_code
    import aws_sdk_iotsitewise.types.timestamp


class BatchGetAssetPropertyAggregatesErrorInfo(TypedDict, closed=True):
    error_code: "aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_error_code.BatchGetAssetPropertyAggregatesErrorCode"
    """<p>The error code.</p>"""
    error_timestamp: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the error occurred, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyAggregatesErrorInfo) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_error_code

    out["errorCode"] = (
        aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_error_code.serialize_json(
            value["error_code"]
        )
    )
    import aws_sdk_iotsitewise.types.timestamp

    out["errorTimestamp"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["error_timestamp"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetAssetPropertyAggregatesErrorInfo:
    out: BatchGetAssetPropertyAggregatesErrorInfo = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        import aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_error_code

        out["error_code"] = (
            aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyAggregatesErrorInfo.error_code required"
        )
    if "errorTimestamp" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["error_timestamp"] = aws_sdk_iotsitewise.types.timestamp.deserialize_json(
            data["errorTimestamp"]
        )
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyAggregatesErrorInfo.error_timestamp required"
        )
    return out
