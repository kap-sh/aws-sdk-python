"""Generated from Smithy shape ``com.amazonaws.pipes#MultiMeasureAttributeMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pipes.types.multi_measure_attribute_mapping

MultiMeasureAttributeMappings: TypeAlias = list[
    "aws_sdk_pipes.types.multi_measure_attribute_mapping.MultiMeasureAttributeMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: MultiMeasureAttributeMappings) -> list:
    import aws_sdk_pipes.types.multi_measure_attribute_mapping

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pipes.types.multi_measure_attribute_mapping.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MultiMeasureAttributeMappings:
    import aws_sdk_pipes.types.multi_measure_attribute_mapping

    out: MultiMeasureAttributeMappings = []
    for item in data:
        out.append(
            aws_sdk_pipes.types.multi_measure_attribute_mapping.deserialize_json(item)
        )
    return out
