"""Generated from Smithy shape ``com.amazonaws.devopsguru#AnomalousLogGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.anomalous_log_group

AnomalousLogGroups: TypeAlias = list[
    "capo_devops_guru.types.anomalous_log_group.AnomalousLogGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnomalousLogGroups) -> list:
    import capo_devops_guru.types.anomalous_log_group

    out: list = []
    for item in value:
        out.append(capo_devops_guru.types.anomalous_log_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnomalousLogGroups:
    import capo_devops_guru.types.anomalous_log_group

    out: AnomalousLogGroups = []
    for item in data:
        out.append(capo_devops_guru.types.anomalous_log_group.deserialize_json(item))
    return out
