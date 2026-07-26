"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeleteUniqueIdErrorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_entityresolution.types.delete_unique_id_error

DeleteUniqueIdErrorsList: TypeAlias = list[
    "capo_entityresolution.types.delete_unique_id_error.DeleteUniqueIdError"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteUniqueIdErrorsList) -> list:
    import capo_entityresolution.types.delete_unique_id_error

    out: list = []
    for item in value:
        out.append(
            capo_entityresolution.types.delete_unique_id_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DeleteUniqueIdErrorsList:
    import capo_entityresolution.types.delete_unique_id_error

    out: DeleteUniqueIdErrorsList = []
    for item in data:
        out.append(
            capo_entityresolution.types.delete_unique_id_error.deserialize_json(item)
        )
    return out
