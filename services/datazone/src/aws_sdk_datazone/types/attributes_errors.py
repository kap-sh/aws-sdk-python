"""Generated from Smithy shape ``com.amazonaws.datazone#AttributesErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.attribute_error

AttributesErrors: TypeAlias = list[
    "aws_sdk_datazone.types.attribute_error.AttributeError"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributesErrors) -> list:
    import aws_sdk_datazone.types.attribute_error

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.attribute_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttributesErrors:
    import aws_sdk_datazone.types.attribute_error

    out: AttributesErrors = []
    for item in data:
        out.append(aws_sdk_datazone.types.attribute_error.deserialize_json(item))
    return out
