"""Generated from Smithy shape ``com.amazonaws.pipes#SingleMeasureMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pipes.types.single_measure_mapping

SingleMeasureMappings: TypeAlias = list[
    "aws_sdk_pipes.types.single_measure_mapping.SingleMeasureMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: SingleMeasureMappings) -> list:
    import aws_sdk_pipes.types.single_measure_mapping

    out: list = []
    for item in value:
        out.append(aws_sdk_pipes.types.single_measure_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> SingleMeasureMappings:
    import aws_sdk_pipes.types.single_measure_mapping

    out: SingleMeasureMappings = []
    for item in data:
        out.append(aws_sdk_pipes.types.single_measure_mapping.deserialize_json(item))
    return out
