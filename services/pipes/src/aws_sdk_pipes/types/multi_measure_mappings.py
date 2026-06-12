"""Generated from Smithy shape ``com.amazonaws.pipes#MultiMeasureMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pipes.types.multi_measure_mapping

MultiMeasureMappings: TypeAlias = list[
    "aws_sdk_pipes.types.multi_measure_mapping.MultiMeasureMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: MultiMeasureMappings) -> list:
    import aws_sdk_pipes.types.multi_measure_mapping

    out: list = []
    for item in value:
        out.append(aws_sdk_pipes.types.multi_measure_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> MultiMeasureMappings:
    import aws_sdk_pipes.types.multi_measure_mapping

    out: MultiMeasureMappings = []
    for item in data:
        out.append(aws_sdk_pipes.types.multi_measure_mapping.deserialize_json(item))
    return out
