"""Generated from Smithy shape ``com.amazonaws.devopsguru#AnomalyResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.anomaly_resource

AnomalyResources: TypeAlias = list[
    "aws_sdk_devops_guru.types.anomaly_resource.AnomalyResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyResources) -> list:
    import aws_sdk_devops_guru.types.anomaly_resource

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_guru.types.anomaly_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnomalyResources:
    import aws_sdk_devops_guru.types.anomaly_resource

    out: AnomalyResources = []
    for item in data:
        out.append(aws_sdk_devops_guru.types.anomaly_resource.deserialize_json(item))
    return out
