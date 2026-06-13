"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectResourceTagParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.resource_tag_parameter

ProjectResourceTagParameters: TypeAlias = list[
    "aws_sdk_datazone.types.resource_tag_parameter.ResourceTagParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProjectResourceTagParameters) -> list:
    import aws_sdk_datazone.types.resource_tag_parameter

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.resource_tag_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProjectResourceTagParameters:
    import aws_sdk_datazone.types.resource_tag_parameter

    out: ProjectResourceTagParameters = []
    for item in data:
        out.append(aws_sdk_datazone.types.resource_tag_parameter.deserialize_json(item))
    return out
