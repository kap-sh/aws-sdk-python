"""Generated from Smithy shape ``com.amazonaws.greengrass#__listOfGroupInformation``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.group_information

__listOfGroupInformation: TypeAlias = list[
    "aws_sdk_greengrass.types.group_information.GroupInformation"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfGroupInformation) -> list:
    import aws_sdk_greengrass.types.group_information

    out: list = []
    for item in value:
        out.append(aws_sdk_greengrass.types.group_information.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfGroupInformation:
    import aws_sdk_greengrass.types.group_information

    out: __listOfGroupInformation = []
    for item in data:
        out.append(aws_sdk_greengrass.types.group_information.deserialize_json(item))
    return out
