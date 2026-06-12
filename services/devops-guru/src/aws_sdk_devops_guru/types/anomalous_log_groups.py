"""Generated from Smithy shape ``com.amazonaws.devopsguru#AnomalousLogGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.anomalous_log_group

AnomalousLogGroups: TypeAlias = list[
    "aws_sdk_devops_guru.types.anomalous_log_group.AnomalousLogGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnomalousLogGroups) -> list:
    import aws_sdk_devops_guru.types.anomalous_log_group

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_guru.types.anomalous_log_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnomalousLogGroups:
    import aws_sdk_devops_guru.types.anomalous_log_group

    out: AnomalousLogGroups = []
    for item in data:
        out.append(aws_sdk_devops_guru.types.anomalous_log_group.deserialize_json(item))
    return out
