"""Generated from Smithy shape ``com.amazonaws.guardduty#AnomalyProfileFeatureObjects``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.anomaly_object

AnomalyProfileFeatureObjects: TypeAlias = list[
    "capo_guardduty.types.anomaly_object.AnomalyObject"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyProfileFeatureObjects) -> list:
    import capo_guardduty.types.anomaly_object

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.anomaly_object.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnomalyProfileFeatureObjects:
    import capo_guardduty.types.anomaly_object

    out: AnomalyProfileFeatureObjects = []
    for item in data:
        out.append(capo_guardduty.types.anomaly_object.deserialize_json(item))
    return out
