"""Generated from Smithy shape ``com.amazonaws.pipes#MultiMeasureMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.multi_measure_mapping

MultiMeasureMappings: TypeAlias = list[
    "capo_pipes.types.multi_measure_mapping.MultiMeasureMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: MultiMeasureMappings) -> list:
    import capo_pipes.types.multi_measure_mapping

    out: list = []
    for item in value:
        out.append(capo_pipes.types.multi_measure_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> MultiMeasureMappings:
    import capo_pipes.types.multi_measure_mapping

    out: MultiMeasureMappings = []
    for item in data:
        out.append(capo_pipes.types.multi_measure_mapping.deserialize_json(item))
    return out
