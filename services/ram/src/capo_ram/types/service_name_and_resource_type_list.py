"""Generated from Smithy shape ``com.amazonaws.ram#ServiceNameAndResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ram.types.service_name_and_resource_type

ServiceNameAndResourceTypeList: TypeAlias = list[
    "capo_ram.types.service_name_and_resource_type.ServiceNameAndResourceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNameAndResourceTypeList) -> list:
    import capo_ram.types.service_name_and_resource_type

    out: list = []
    for item in value:
        out.append(capo_ram.types.service_name_and_resource_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceNameAndResourceTypeList:
    import capo_ram.types.service_name_and_resource_type

    out: ServiceNameAndResourceTypeList = []
    for item in data:
        out.append(capo_ram.types.service_name_and_resource_type.deserialize_json(item))
    return out
