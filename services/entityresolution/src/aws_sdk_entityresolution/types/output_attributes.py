"""Generated from Smithy shape ``com.amazonaws.entityresolution#OutputAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.output_attribute

OutputAttributes: TypeAlias = list[
    "aws_sdk_entityresolution.types.output_attribute.OutputAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputAttributes) -> list:
    import aws_sdk_entityresolution.types.output_attribute

    out: list = []
    for item in value:
        out.append(aws_sdk_entityresolution.types.output_attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> OutputAttributes:
    import aws_sdk_entityresolution.types.output_attribute

    out: OutputAttributes = []
    for item in data:
        out.append(
            aws_sdk_entityresolution.types.output_attribute.deserialize_json(item)
        )
    return out
