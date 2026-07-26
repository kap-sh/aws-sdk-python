"""Generated from Smithy shape ``com.amazonaws.pipes#MultiMeasureAttributeMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.multi_measure_attribute_mapping

MultiMeasureAttributeMappings: TypeAlias = list[
    "capo_pipes.types.multi_measure_attribute_mapping.MultiMeasureAttributeMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: MultiMeasureAttributeMappings) -> list:
    import capo_pipes.types.multi_measure_attribute_mapping

    out: list = []
    for item in value:
        out.append(
            capo_pipes.types.multi_measure_attribute_mapping.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MultiMeasureAttributeMappings:
    import capo_pipes.types.multi_measure_attribute_mapping

    out: MultiMeasureAttributeMappings = []
    for item in data:
        out.append(
            capo_pipes.types.multi_measure_attribute_mapping.deserialize_json(item)
        )
    return out
