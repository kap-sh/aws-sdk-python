"""Generated from Smithy shape ``com.amazonaws.devopsguru#ServiceHealths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.service_health

ServiceHealths: TypeAlias = list[
    "aws_sdk_devops_guru.types.service_health.ServiceHealth"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceHealths) -> list:
    import aws_sdk_devops_guru.types.service_health

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_guru.types.service_health.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceHealths:
    import aws_sdk_devops_guru.types.service_health

    out: ServiceHealths = []
    for item in data:
        out.append(aws_sdk_devops_guru.types.service_health.deserialize_json(item))
    return out
