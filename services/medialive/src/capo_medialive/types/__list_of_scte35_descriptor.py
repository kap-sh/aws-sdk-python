"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfScte35Descriptor``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.scte35_descriptor

__listOfScte35Descriptor: TypeAlias = list[
    "capo_medialive.types.scte35_descriptor.Scte35Descriptor"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfScte35Descriptor) -> list:
    import capo_medialive.types.scte35_descriptor

    out: list = []
    for item in value:
        out.append(capo_medialive.types.scte35_descriptor.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfScte35Descriptor:
    import capo_medialive.types.scte35_descriptor

    out: __listOfScte35Descriptor = []
    for item in data:
        out.append(capo_medialive.types.scte35_descriptor.deserialize_json(item))
    return out
