"""Generated from Smithy shape ``com.amazonaws.clouddirectory#PathToObjectIdentifiersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.path_to_object_identifiers

PathToObjectIdentifiersList: TypeAlias = list[
    "capo_clouddirectory.types.path_to_object_identifiers.PathToObjectIdentifiers"
]


# --- restJson1 ser/de ---
def serialize_json(value: PathToObjectIdentifiersList) -> list:
    import capo_clouddirectory.types.path_to_object_identifiers

    out: list = []
    for item in value:
        out.append(
            capo_clouddirectory.types.path_to_object_identifiers.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PathToObjectIdentifiersList:
    import capo_clouddirectory.types.path_to_object_identifiers

    out: PathToObjectIdentifiersList = []
    for item in data:
        out.append(
            capo_clouddirectory.types.path_to_object_identifiers.deserialize_json(item)
        )
    return out
