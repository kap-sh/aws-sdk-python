"""Generated from Smithy shape ``com.amazonaws.synthetics#VisualReferencesOutput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_synthetics.types.visual_reference_output

VisualReferencesOutput: TypeAlias = list[
    "capo_synthetics.types.visual_reference_output.VisualReferenceOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: VisualReferencesOutput) -> list:
    import capo_synthetics.types.visual_reference_output

    out: list = []
    for item in value:
        out.append(capo_synthetics.types.visual_reference_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> VisualReferencesOutput:
    import capo_synthetics.types.visual_reference_output

    out: VisualReferencesOutput = []
    for item in data:
        out.append(capo_synthetics.types.visual_reference_output.deserialize_json(item))
    return out
