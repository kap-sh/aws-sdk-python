"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#Anomalies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.anomaly

Anomalies: TypeAlias = list["capo_codeguruprofiler.types.anomaly.Anomaly"]


# --- restJson1 ser/de ---
def serialize_json(value: Anomalies) -> list:
    import capo_codeguruprofiler.types.anomaly

    out: list = []
    for item in value:
        out.append(capo_codeguruprofiler.types.anomaly.serialize_json(item))
    return out


def deserialize_json(data: list) -> Anomalies:
    import capo_codeguruprofiler.types.anomaly

    out: Anomalies = []
    for item in data:
        out.append(capo_codeguruprofiler.types.anomaly.deserialize_json(item))
    return out
