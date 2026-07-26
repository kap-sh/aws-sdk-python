"""Generated from Smithy shape ``com.amazonaws.clouddirectory#LinkNameToObjectIdentifierMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.link_name
    import capo_clouddirectory.types.object_identifier

LinkNameToObjectIdentifierMap: TypeAlias = dict[
    "capo_clouddirectory.types.link_name.LinkName",
    "capo_clouddirectory.types.object_identifier.ObjectIdentifier",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LinkNameToObjectIdentifierMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> LinkNameToObjectIdentifierMap:
    out: LinkNameToObjectIdentifierMap = {}
    for key, value in data.items():
        out[key] = value
    return out
