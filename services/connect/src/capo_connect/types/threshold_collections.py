"""Generated from Smithy shape ``com.amazonaws.connect#ThresholdCollections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.threshold_v2

ThresholdCollections: TypeAlias = list["capo_connect.types.threshold_v2.ThresholdV2"]


# --- restJson1 ser/de ---
def serialize_json(value: ThresholdCollections) -> list:
    import capo_connect.types.threshold_v2

    out: list = []
    for item in value:
        out.append(capo_connect.types.threshold_v2.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThresholdCollections:
    import capo_connect.types.threshold_v2

    out: ThresholdCollections = []
    for item in data:
        out.append(capo_connect.types.threshold_v2.deserialize_json(item))
    return out
