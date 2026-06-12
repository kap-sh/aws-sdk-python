"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInputAttachment``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.input_attachment

__listOfInputAttachment: TypeAlias = list[
    "aws_sdk_medialive.types.input_attachment.InputAttachment"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputAttachment) -> list:
    import aws_sdk_medialive.types.input_attachment

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.input_attachment.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInputAttachment:
    import aws_sdk_medialive.types.input_attachment

    out: __listOfInputAttachment = []
    for item in data:
        out.append(aws_sdk_medialive.types.input_attachment.deserialize_json(item))
    return out
