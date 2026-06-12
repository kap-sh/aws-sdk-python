"""Generated from Smithy shape ``com.amazonaws.connect#HistoricalMetricResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.dimensions
    import aws_sdk_connect.types.historical_metric_data_collections


class HistoricalMetricResult(TypedDict):
    dimensions: NotRequired["aws_sdk_connect.types.dimensions.Dimensions"]
    """<p>The dimension for the metrics.</p>"""
    collections: NotRequired[
        "aws_sdk_connect.types.historical_metric_data_collections.HistoricalMetricDataCollections"
    ]
    """<p>The set of metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HistoricalMetricResult) -> dict:
    out: dict = {}
    if "dimensions" in value:
        import aws_sdk_connect.types.dimensions

        out["Dimensions"] = aws_sdk_connect.types.dimensions.serialize_json(
            value["dimensions"]
        )
    if "collections" in value:
        import aws_sdk_connect.types.historical_metric_data_collections

        out["Collections"] = (
            aws_sdk_connect.types.historical_metric_data_collections.serialize_json(
                value["collections"]
            )
        )
    return out


def deserialize_json(data: dict) -> HistoricalMetricResult:
    out: HistoricalMetricResult = {}  # type: ignore[typeddict-item]
    if "Dimensions" in data:
        import aws_sdk_connect.types.dimensions

        out["dimensions"] = aws_sdk_connect.types.dimensions.deserialize_json(
            data["Dimensions"]
        )
    if "Collections" in data:
        import aws_sdk_connect.types.historical_metric_data_collections

        out["collections"] = (
            aws_sdk_connect.types.historical_metric_data_collections.deserialize_json(
                data["Collections"]
            )
        )
    return out
