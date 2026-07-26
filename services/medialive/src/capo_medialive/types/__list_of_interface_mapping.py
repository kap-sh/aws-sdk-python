"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInterfaceMapping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.interface_mapping

__listOfInterfaceMapping: TypeAlias = list[
    "capo_medialive.types.interface_mapping.InterfaceMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInterfaceMapping) -> list:
    import capo_medialive.types.interface_mapping

    out: list = []
    for item in value:
        out.append(capo_medialive.types.interface_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInterfaceMapping:
    import capo_medialive.types.interface_mapping

    out: __listOfInterfaceMapping = []
    for item in data:
        out.append(capo_medialive.types.interface_mapping.deserialize_json(item))
    return out
