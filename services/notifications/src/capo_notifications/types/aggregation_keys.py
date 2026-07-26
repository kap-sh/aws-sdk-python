"""Generated from Smithy shape ``com.amazonaws.notifications#AggregationKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_notifications.types.aggregation_key

AggregationKeys: TypeAlias = list[
    "capo_notifications.types.aggregation_key.AggregationKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregationKeys) -> list:
    import capo_notifications.types.aggregation_key

    out: list = []
    for item in value:
        out.append(capo_notifications.types.aggregation_key.serialize_json(item))
    return out


def deserialize_json(data: list) -> AggregationKeys:
    import capo_notifications.types.aggregation_key

    out: AggregationKeys = []
    for item in data:
        out.append(capo_notifications.types.aggregation_key.deserialize_json(item))
    return out
