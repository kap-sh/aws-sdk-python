"""Generated from Smithy shape ``com.amazonaws.forecast#TimeSeriesSelector``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.time_series_identifiers


class TimeSeriesSelector(TypedDict):
    time_series_identifiers: NotRequired[
        "aws_sdk_forecast.types.time_series_identifiers.TimeSeriesIdentifiers"
    ]
    """<p>Details about the import file that contains the time series for which you want to create forecasts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeSeriesSelector) -> dict:
    out: dict = {}
    if "time_series_identifiers" in value:
        import aws_sdk_forecast.types.time_series_identifiers

        out["TimeSeriesIdentifiers"] = (
            aws_sdk_forecast.types.time_series_identifiers.serialize_aws_json_1_1(
                value["time_series_identifiers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeSeriesSelector:
    out: TimeSeriesSelector = {}  # type: ignore[typeddict-item]
    if "TimeSeriesIdentifiers" in data:
        import aws_sdk_forecast.types.time_series_identifiers

        out["time_series_identifiers"] = (
            aws_sdk_forecast.types.time_series_identifiers.deserialize_aws_json_1_1(
                data["TimeSeriesIdentifiers"]
            )
        )
    return out
