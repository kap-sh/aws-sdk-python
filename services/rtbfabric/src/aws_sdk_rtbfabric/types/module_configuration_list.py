"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ModuleConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.module_configuration

ModuleConfigurationList: TypeAlias = list[
    "aws_sdk_rtbfabric.types.module_configuration.ModuleConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ModuleConfigurationList) -> list:
    import aws_sdk_rtbfabric.types.module_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_rtbfabric.types.module_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ModuleConfigurationList:
    import aws_sdk_rtbfabric.types.module_configuration

    out: ModuleConfigurationList = []
    for item in data:
        out.append(aws_sdk_rtbfabric.types.module_configuration.deserialize_json(item))
    return out
