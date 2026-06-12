"""Generated from Smithy shape ``com.amazonaws.synthetics#VisualReferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.visual_reference_input

VisualReferences: TypeAlias = list[
    "aws_sdk_synthetics.types.visual_reference_input.VisualReferenceInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: VisualReferences) -> list:
    import aws_sdk_synthetics.types.visual_reference_input

    out: list = []
    for item in value:
        out.append(aws_sdk_synthetics.types.visual_reference_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> VisualReferences:
    import aws_sdk_synthetics.types.visual_reference_input

    out: VisualReferences = []
    for item in data:
        out.append(
            aws_sdk_synthetics.types.visual_reference_input.deserialize_json(item)
        )
    return out
