"""Generated from Smithy shape ``com.amazonaws.entityresolution#OutputAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_entityresolution.types.output_attribute

OutputAttributes: TypeAlias = list[
    "capo_entityresolution.types.output_attribute.OutputAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputAttributes) -> list:
    import capo_entityresolution.types.output_attribute

    out: list = []
    for item in value:
        out.append(capo_entityresolution.types.output_attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> OutputAttributes:
    import capo_entityresolution.types.output_attribute

    out: OutputAttributes = []
    for item in data:
        out.append(capo_entityresolution.types.output_attribute.deserialize_json(item))
    return out
