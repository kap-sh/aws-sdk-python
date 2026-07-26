"""Generated from Smithy shape ``com.amazonaws.datazone#BatchPutAttributeItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.batch_put_attribute_output

BatchPutAttributeItems: TypeAlias = list[
    "capo_datazone.types.batch_put_attribute_output.BatchPutAttributeOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutAttributeItems) -> list:
    import capo_datazone.types.batch_put_attribute_output

    out: list = []
    for item in value:
        out.append(capo_datazone.types.batch_put_attribute_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchPutAttributeItems:
    import capo_datazone.types.batch_put_attribute_output

    out: BatchPutAttributeItems = []
    for item in data:
        out.append(
            capo_datazone.types.batch_put_attribute_output.deserialize_json(item)
        )
    return out
