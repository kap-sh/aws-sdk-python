"""Generated from Smithy shape ``com.amazonaws.synthetics#VisualReferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_synthetics.types.visual_reference_input

VisualReferences: TypeAlias = list[
    "capo_synthetics.types.visual_reference_input.VisualReferenceInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: VisualReferences) -> list:
    import capo_synthetics.types.visual_reference_input

    out: list = []
    for item in value:
        out.append(capo_synthetics.types.visual_reference_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> VisualReferences:
    import capo_synthetics.types.visual_reference_input

    out: VisualReferences = []
    for item in data:
        out.append(capo_synthetics.types.visual_reference_input.deserialize_json(item))
    return out
