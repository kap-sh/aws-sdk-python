"""Generated from Smithy shape ``com.amazonaws.clouddirectory#PathToObjectIdentifiersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.path_to_object_identifiers

PathToObjectIdentifiersList: TypeAlias = list[
    "aws_sdk_clouddirectory.types.path_to_object_identifiers.PathToObjectIdentifiers"
]


# --- restJson1 ser/de ---
def serialize_json(value: PathToObjectIdentifiersList) -> list:
    import aws_sdk_clouddirectory.types.path_to_object_identifiers

    out: list = []
    for item in value:
        out.append(
            aws_sdk_clouddirectory.types.path_to_object_identifiers.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PathToObjectIdentifiersList:
    import aws_sdk_clouddirectory.types.path_to_object_identifiers

    out: PathToObjectIdentifiersList = []
    for item in data:
        out.append(
            aws_sdk_clouddirectory.types.path_to_object_identifiers.deserialize_json(
                item
            )
        )
    return out
