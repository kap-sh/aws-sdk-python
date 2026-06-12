"""Generated from Smithy shape ``com.amazonaws.greengrass#__listOfVersionInformation``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.version_information

__listOfVersionInformation: TypeAlias = list[
    "aws_sdk_greengrass.types.version_information.VersionInformation"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfVersionInformation) -> list:
    import aws_sdk_greengrass.types.version_information

    out: list = []
    for item in value:
        out.append(aws_sdk_greengrass.types.version_information.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfVersionInformation:
    import aws_sdk_greengrass.types.version_information

    out: __listOfVersionInformation = []
    for item in data:
        out.append(aws_sdk_greengrass.types.version_information.deserialize_json(item))
    return out
