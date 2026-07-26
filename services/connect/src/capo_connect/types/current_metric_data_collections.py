"""Generated from Smithy shape ``com.amazonaws.connect#CurrentMetricDataCollections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.current_metric_data

CurrentMetricDataCollections: TypeAlias = list[
    "capo_connect.types.current_metric_data.CurrentMetricData"
]


# --- restJson1 ser/de ---
def serialize_json(value: CurrentMetricDataCollections) -> list:
    import capo_connect.types.current_metric_data

    out: list = []
    for item in value:
        out.append(capo_connect.types.current_metric_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> CurrentMetricDataCollections:
    import capo_connect.types.current_metric_data

    out: CurrentMetricDataCollections = []
    for item in data:
        out.append(capo_connect.types.current_metric_data.deserialize_json(item))
    return out
