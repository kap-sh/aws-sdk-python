"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#MappedResourceConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.mapped_resource_configuration_list_item

MappedResourceConfigurationList: TypeAlias = list[
    "aws_sdk_kinesis_video.types.mapped_resource_configuration_list_item.MappedResourceConfigurationListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: MappedResourceConfigurationList) -> list:
    import aws_sdk_kinesis_video.types.mapped_resource_configuration_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_video.types.mapped_resource_configuration_list_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MappedResourceConfigurationList:
    import aws_sdk_kinesis_video.types.mapped_resource_configuration_list_item

    out: MappedResourceConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_kinesis_video.types.mapped_resource_configuration_list_item.deserialize_json(
                item
            )
        )
    return out
