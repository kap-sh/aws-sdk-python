"""Generated from Smithy shape ``com.amazonaws.devopsguru#CloudFormationHealths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.cloud_formation_health

CloudFormationHealths: TypeAlias = list[
    "capo_devops_guru.types.cloud_formation_health.CloudFormationHealth"
]


# --- restJson1 ser/de ---
def serialize_json(value: CloudFormationHealths) -> list:
    import capo_devops_guru.types.cloud_formation_health

    out: list = []
    for item in value:
        out.append(capo_devops_guru.types.cloud_formation_health.serialize_json(item))
    return out


def deserialize_json(data: list) -> CloudFormationHealths:
    import capo_devops_guru.types.cloud_formation_health

    out: CloudFormationHealths = []
    for item in data:
        out.append(capo_devops_guru.types.cloud_formation_health.deserialize_json(item))
    return out
