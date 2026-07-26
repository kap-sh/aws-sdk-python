"""Generated from Smithy shape ``com.amazonaws.connect#MetricResultV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.dimensions_v2_map
    import capo_connect.types.metric_data_collections_v2
    import capo_connect.types.metric_interval


class MetricResultV2(TypedDict, closed=True):
    dimensions: NotRequired["capo_connect.types.dimensions_v2_map.DimensionsV2Map"]
    """<p>The dimension for the metrics.</p>"""
    metric_interval: NotRequired["capo_connect.types.metric_interval.MetricInterval"]
    """<p>The interval period with the start and end time for the metrics.</p>"""
    collections: NotRequired[
        "capo_connect.types.metric_data_collections_v2.MetricDataCollectionsV2"
    ]
    """<p>The set of metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricResultV2) -> dict:
    out: dict = {}
    if "dimensions" in value:
        import capo_connect.types.dimensions_v2_map

        out["Dimensions"] = capo_connect.types.dimensions_v2_map.serialize_json(
            value["dimensions"]
        )
    if "metric_interval" in value:
        import capo_connect.types.metric_interval

        out["MetricInterval"] = capo_connect.types.metric_interval.serialize_json(
            value["metric_interval"]
        )
    if "collections" in value:
        import capo_connect.types.metric_data_collections_v2

        out["Collections"] = (
            capo_connect.types.metric_data_collections_v2.serialize_json(
                value["collections"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetricResultV2:
    out: MetricResultV2 = {}  # type: ignore[typeddict-item]
    if "Dimensions" in data:
        import capo_connect.types.dimensions_v2_map

        out["dimensions"] = capo_connect.types.dimensions_v2_map.deserialize_json(
            data["Dimensions"]
        )
    if "MetricInterval" in data:
        import capo_connect.types.metric_interval

        out["metric_interval"] = capo_connect.types.metric_interval.deserialize_json(
            data["MetricInterval"]
        )
    if "Collections" in data:
        import capo_connect.types.metric_data_collections_v2

        out["collections"] = (
            capo_connect.types.metric_data_collections_v2.deserialize_json(
                data["Collections"]
            )
        )
    return out
