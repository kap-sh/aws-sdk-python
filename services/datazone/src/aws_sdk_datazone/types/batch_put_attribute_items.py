"""Generated from Smithy shape ``com.amazonaws.datazone#BatchPutAttributeItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.batch_put_attribute_output

BatchPutAttributeItems: TypeAlias = list[
    "aws_sdk_datazone.types.batch_put_attribute_output.BatchPutAttributeOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutAttributeItems) -> list:
    import aws_sdk_datazone.types.batch_put_attribute_output

    out: list = []
    for item in value:
        out.append(
            aws_sdk_datazone.types.batch_put_attribute_output.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchPutAttributeItems:
    import aws_sdk_datazone.types.batch_put_attribute_output

    out: BatchPutAttributeItems = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.batch_put_attribute_output.deserialize_json(item)
        )
    return out
