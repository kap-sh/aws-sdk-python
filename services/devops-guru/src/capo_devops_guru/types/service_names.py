"""Generated from Smithy shape ``com.amazonaws.devopsguru#ServiceNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.service_name

ServiceNames: TypeAlias = list["capo_devops_guru.types.service_name.ServiceName"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNames) -> list:
    import capo_devops_guru.types.service_name

    out: list = []
    for item in value:
        out.append(capo_devops_guru.types.service_name.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceNames:
    import capo_devops_guru.types.service_name

    out: ServiceNames = []
    for item in data:
        out.append(capo_devops_guru.types.service_name.deserialize_json(item))
    return out
