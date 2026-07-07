"""Generated from Smithy shape ``com.amazonaws.forecast#ExplainabilityConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.time_point_granularity
    import aws_sdk_forecast.types.time_series_granularity


class ExplainabilityConfig(TypedDict, closed=True):
    time_series_granularity: (
        "aws_sdk_forecast.types.time_series_granularity.TimeSeriesGranularity"
    )
    """<p>To create an Explainability for all time series in your datasets, use <code>ALL</code>. To create an Explainability for specific time series in your datasets, use <code>SPECIFIC</code>.</p> <p>Specify time series by uploading a CSV or Parquet file to an Amazon S3 bucket and set the location within the <a>DataDestination</a> data type.</p>"""
    time_point_granularity: (
        "aws_sdk_forecast.types.time_point_granularity.TimePointGranularity"
    )
    """<p>To create an Explainability for all time points in your forecast horizon, use <code>ALL</code>. To create an Explainability for specific time points in your forecast horizon, use <code>SPECIFIC</code>.</p> <p>Specify time points with the <code>StartDateTime</code> and <code>EndDateTime</code> parameters within the <a>CreateExplainability</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExplainabilityConfig) -> dict:
    out: dict = {}
    import aws_sdk_forecast.types.time_series_granularity

    out["TimeSeriesGranularity"] = (
        aws_sdk_forecast.types.time_series_granularity.serialize_aws_json_1_1(
            value["time_series_granularity"]
        )
    )
    import aws_sdk_forecast.types.time_point_granularity

    out["TimePointGranularity"] = (
        aws_sdk_forecast.types.time_point_granularity.serialize_aws_json_1_1(
            value["time_point_granularity"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExplainabilityConfig:
    out: ExplainabilityConfig = {}  # type: ignore[typeddict-item]
    if "TimeSeriesGranularity" in data:
        import aws_sdk_forecast.types.time_series_granularity

        out["time_series_granularity"] = (
            aws_sdk_forecast.types.time_series_granularity.deserialize_aws_json_1_1(
                data["TimeSeriesGranularity"]
            )
        )
    else:
        raise DeserializationError(
            "ExplainabilityConfig.time_series_granularity required"
        )
    if "TimePointGranularity" in data:
        import aws_sdk_forecast.types.time_point_granularity

        out["time_point_granularity"] = (
            aws_sdk_forecast.types.time_point_granularity.deserialize_aws_json_1_1(
                data["TimePointGranularity"]
            )
        )
    else:
        raise DeserializationError(
            "ExplainabilityConfig.time_point_granularity required"
        )
    return out
