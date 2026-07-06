"""Generated from Smithy shape ``com.amazonaws.forecast#TimeSeriesReplacementsDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.format
    import aws_sdk_forecast.types.s3_config
    import aws_sdk_forecast.types.schema
    import aws_sdk_forecast.types.timestamp_format


class TimeSeriesReplacementsDataSource(TypedDict, closed=True):
    s3_config: "aws_sdk_forecast.types.s3_config.S3Config"
    schema: "aws_sdk_forecast.types.schema.Schema"
    format: NotRequired["aws_sdk_forecast.types.format.Format"]
    """<p>The format of the replacement data, CSV or PARQUET.</p>"""
    timestamp_format: NotRequired[
        "aws_sdk_forecast.types.timestamp_format.TimestampFormat"
    ]
    """<p>The timestamp format of the replacement data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeSeriesReplacementsDataSource) -> dict:
    out: dict = {}
    import aws_sdk_forecast.types.s3_config

    out["S3Config"] = aws_sdk_forecast.types.s3_config.serialize_aws_json_1_1(
        value["s3_config"]
    )
    import aws_sdk_forecast.types.schema

    out["Schema"] = aws_sdk_forecast.types.schema.serialize_aws_json_1_1(
        value["schema"]
    )
    if "format" in value:
        out["Format"] = value["format"]
    if "timestamp_format" in value:
        out["TimestampFormat"] = value["timestamp_format"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeSeriesReplacementsDataSource:
    out: TimeSeriesReplacementsDataSource = {}  # type: ignore[typeddict-item]
    if "S3Config" in data:
        import aws_sdk_forecast.types.s3_config

        out["s3_config"] = aws_sdk_forecast.types.s3_config.deserialize_aws_json_1_1(
            data["S3Config"]
        )
    else:
        raise DeserializationError(
            "TimeSeriesReplacementsDataSource.s3_config required"
        )
    if "Schema" in data:
        import aws_sdk_forecast.types.schema

        out["schema"] = aws_sdk_forecast.types.schema.deserialize_aws_json_1_1(
            data["Schema"]
        )
    else:
        raise DeserializationError("TimeSeriesReplacementsDataSource.schema required")
    if "Format" in data:
        out["format"] = data["Format"]
    if "TimestampFormat" in data:
        out["timestamp_format"] = data["TimestampFormat"]
    return out
