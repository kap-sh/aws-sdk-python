"""Generated from Smithy shape ``com.amazonaws.datazone#ResourceConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.resource_configuration

ResourceConfigurations: TypeAlias = list[
    "aws_sdk_datazone.types.resource_configuration.ResourceConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceConfigurations) -> list:
    import aws_sdk_datazone.types.resource_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.resource_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceConfigurations:
    import aws_sdk_datazone.types.resource_configuration

    out: ResourceConfigurations = []
    for item in data:
        out.append(aws_sdk_datazone.types.resource_configuration.deserialize_json(item))
    return out
