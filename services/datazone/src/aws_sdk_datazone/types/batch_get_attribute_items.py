"""Generated from Smithy shape ``com.amazonaws.datazone#BatchGetAttributeItems``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_datazone.types.batch_get_attribute_output

BatchGetAttributeItems: TypeAlias = list["aws_sdk_datazone.types.batch_get_attribute_output.BatchGetAttributeOutput"]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAttributeItems) -> list:
    import aws_sdk_datazone.types.batch_get_attribute_output
    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.batch_get_attribute_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetAttributeItems:
    import aws_sdk_datazone.types.batch_get_attribute_output
    out: BatchGetAttributeItems = []
    for item in data:
        out.append(aws_sdk_datazone.types.batch_get_attribute_output.deserialize_json(item))
    return out