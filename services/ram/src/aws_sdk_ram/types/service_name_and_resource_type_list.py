"""Generated from Smithy shape ``com.amazonaws.ram#ServiceNameAndResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ram.types.service_name_and_resource_type

ServiceNameAndResourceTypeList: TypeAlias = list[
    "aws_sdk_ram.types.service_name_and_resource_type.ServiceNameAndResourceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNameAndResourceTypeList) -> list:
    import aws_sdk_ram.types.service_name_and_resource_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ram.types.service_name_and_resource_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ServiceNameAndResourceTypeList:
    import aws_sdk_ram.types.service_name_and_resource_type

    out: ServiceNameAndResourceTypeList = []
    for item in data:
        out.append(
            aws_sdk_ram.types.service_name_and_resource_type.deserialize_json(item)
        )
    return out
