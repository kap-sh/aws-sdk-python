"""Generated from Smithy shape ``com.amazonaws.pinpoint#MapOfMetricDimension``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.metric_dimension

MapOfMetricDimension: TypeAlias = dict[
    "capo_pinpoint.types.__string.__string",
    "capo_pinpoint.types.metric_dimension.MetricDimension",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfMetricDimension) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_pinpoint.types.metric_dimension

        out[key] = capo_pinpoint.types.metric_dimension.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfMetricDimension:
    out: MapOfMetricDimension = {}
    for key, value in data.items():
        import capo_pinpoint.types.metric_dimension

        out[key] = capo_pinpoint.types.metric_dimension.deserialize_json(value)
    return out
