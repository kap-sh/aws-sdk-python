"""Generated from Smithy shape ``com.amazonaws.datazone#PutResourceConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.put_resource_configuration

PutResourceConfigurations: TypeAlias = list[
    "aws_sdk_datazone.types.put_resource_configuration.PutResourceConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: PutResourceConfigurations) -> list:
    import aws_sdk_datazone.types.put_resource_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_datazone.types.put_resource_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PutResourceConfigurations:
    import aws_sdk_datazone.types.put_resource_configuration

    out: PutResourceConfigurations = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.put_resource_configuration.deserialize_json(item)
        )
    return out
