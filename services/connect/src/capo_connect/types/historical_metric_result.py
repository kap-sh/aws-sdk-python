"""Generated from Smithy shape ``com.amazonaws.connect#HistoricalMetricResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.dimensions
    import capo_connect.types.historical_metric_data_collections


class HistoricalMetricResult(TypedDict, closed=True):
    dimensions: NotRequired["capo_connect.types.dimensions.Dimensions"]
    """<p>The dimension for the metrics.</p>"""
    collections: NotRequired[
        "capo_connect.types.historical_metric_data_collections.HistoricalMetricDataCollections"
    ]
    """<p>The set of metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HistoricalMetricResult) -> dict:
    out: dict = {}
    if "dimensions" in value:
        import capo_connect.types.dimensions

        out["Dimensions"] = capo_connect.types.dimensions.serialize_json(
            value["dimensions"]
        )
    if "collections" in value:
        import capo_connect.types.historical_metric_data_collections

        out["Collections"] = (
            capo_connect.types.historical_metric_data_collections.serialize_json(
                value["collections"]
            )
        )
    return out


def deserialize_json(data: dict) -> HistoricalMetricResult:
    out: HistoricalMetricResult = {}  # type: ignore[typeddict-item]
    if "Dimensions" in data:
        import capo_connect.types.dimensions

        out["dimensions"] = capo_connect.types.dimensions.deserialize_json(
            data["Dimensions"]
        )
    if "Collections" in data:
        import capo_connect.types.historical_metric_data_collections

        out["collections"] = (
            capo_connect.types.historical_metric_data_collections.deserialize_json(
                data["Collections"]
            )
        )
    return out
