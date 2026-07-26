"""Generated from Smithy shape ``com.amazonaws.iot#Percentiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.percent_pair

Percentiles: TypeAlias = list["capo_iot.types.percent_pair.PercentPair"]


# --- restJson1 ser/de ---
def serialize_json(value: Percentiles) -> list:
    import capo_iot.types.percent_pair

    out: list = []
    for item in value:
        out.append(capo_iot.types.percent_pair.serialize_json(item))
    return out


def deserialize_json(data: list) -> Percentiles:
    import capo_iot.types.percent_pair

    out: Percentiles = []
    for item in data:
        out.append(capo_iot.types.percent_pair.deserialize_json(item))
    return out
