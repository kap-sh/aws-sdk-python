"""Generated from Smithy shape ``com.amazonaws.connect#MetricResultV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.dimensions_v2_map
    import aws_sdk_connect.types.metric_data_collections_v2
    import aws_sdk_connect.types.metric_interval


class MetricResultV2(TypedDict, closed=True):
    dimensions: NotRequired["aws_sdk_connect.types.dimensions_v2_map.DimensionsV2Map"]
    """<p>The dimension for the metrics.</p>"""
    metric_interval: NotRequired["aws_sdk_connect.types.metric_interval.MetricInterval"]
    """<p>The interval period with the start and end time for the metrics.</p>"""
    collections: NotRequired[
        "aws_sdk_connect.types.metric_data_collections_v2.MetricDataCollectionsV2"
    ]
    """<p>The set of metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricResultV2) -> dict:
    out: dict = {}
    if "dimensions" in value:
        import aws_sdk_connect.types.dimensions_v2_map

        out["Dimensions"] = aws_sdk_connect.types.dimensions_v2_map.serialize_json(
            value["dimensions"]
        )
    if "metric_interval" in value:
        import aws_sdk_connect.types.metric_interval

        out["MetricInterval"] = aws_sdk_connect.types.metric_interval.serialize_json(
            value["metric_interval"]
        )
    if "collections" in value:
        import aws_sdk_connect.types.metric_data_collections_v2

        out["Collections"] = (
            aws_sdk_connect.types.metric_data_collections_v2.serialize_json(
                value["collections"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetricResultV2:
    out: MetricResultV2 = {}  # type: ignore[typeddict-item]
    if "Dimensions" in data:
        import aws_sdk_connect.types.dimensions_v2_map

        out["dimensions"] = aws_sdk_connect.types.dimensions_v2_map.deserialize_json(
            data["Dimensions"]
        )
    if "MetricInterval" in data:
        import aws_sdk_connect.types.metric_interval

        out["metric_interval"] = aws_sdk_connect.types.metric_interval.deserialize_json(
            data["MetricInterval"]
        )
    if "Collections" in data:
        import aws_sdk_connect.types.metric_data_collections_v2

        out["collections"] = (
            aws_sdk_connect.types.metric_data_collections_v2.deserialize_json(
                data["Collections"]
            )
        )
    return out
