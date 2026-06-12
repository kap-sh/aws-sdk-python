"""Generated from Smithy shape ``com.amazonaws.synthetics#VisualReferencesOutput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.visual_reference_output

VisualReferencesOutput: TypeAlias = list[
    "aws_sdk_synthetics.types.visual_reference_output.VisualReferenceOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: VisualReferencesOutput) -> list:
    import aws_sdk_synthetics.types.visual_reference_output

    out: list = []
    for item in value:
        out.append(
            aws_sdk_synthetics.types.visual_reference_output.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> VisualReferencesOutput:
    import aws_sdk_synthetics.types.visual_reference_output

    out: VisualReferencesOutput = []
    for item in data:
        out.append(
            aws_sdk_synthetics.types.visual_reference_output.deserialize_json(item)
        )
    return out
