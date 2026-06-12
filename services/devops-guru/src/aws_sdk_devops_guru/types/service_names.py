"""Generated from Smithy shape ``com.amazonaws.devopsguru#ServiceNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.service_name

ServiceNames: TypeAlias = list["aws_sdk_devops_guru.types.service_name.ServiceName"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNames) -> list:
    import aws_sdk_devops_guru.types.service_name

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_guru.types.service_name.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceNames:
    import aws_sdk_devops_guru.types.service_name

    out: ServiceNames = []
    for item in data:
        out.append(aws_sdk_devops_guru.types.service_name.deserialize_json(item))
    return out
