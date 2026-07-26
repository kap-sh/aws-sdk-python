"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#AnomalyInstances``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.anomaly_instance

AnomalyInstances: TypeAlias = list[
    "capo_codeguruprofiler.types.anomaly_instance.AnomalyInstance"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyInstances) -> list:
    import capo_codeguruprofiler.types.anomaly_instance

    out: list = []
    for item in value:
        out.append(capo_codeguruprofiler.types.anomaly_instance.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnomalyInstances:
    import capo_codeguruprofiler.types.anomaly_instance

    out: AnomalyInstances = []
    for item in data:
        out.append(capo_codeguruprofiler.types.anomaly_instance.deserialize_json(item))
    return out
