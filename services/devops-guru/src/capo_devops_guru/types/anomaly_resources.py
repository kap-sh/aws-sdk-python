"""Generated from Smithy shape ``com.amazonaws.devopsguru#AnomalyResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.anomaly_resource

AnomalyResources: TypeAlias = list[
    "capo_devops_guru.types.anomaly_resource.AnomalyResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyResources) -> list:
    import capo_devops_guru.types.anomaly_resource

    out: list = []
    for item in value:
        out.append(capo_devops_guru.types.anomaly_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnomalyResources:
    import capo_devops_guru.types.anomaly_resource

    out: AnomalyResources = []
    for item in data:
        out.append(capo_devops_guru.types.anomaly_resource.deserialize_json(item))
    return out
