"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeleteUniqueIdErrorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.delete_unique_id_error

DeleteUniqueIdErrorsList: TypeAlias = list[
    "aws_sdk_entityresolution.types.delete_unique_id_error.DeleteUniqueIdError"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteUniqueIdErrorsList) -> list:
    import aws_sdk_entityresolution.types.delete_unique_id_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_entityresolution.types.delete_unique_id_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DeleteUniqueIdErrorsList:
    import aws_sdk_entityresolution.types.delete_unique_id_error

    out: DeleteUniqueIdErrorsList = []
    for item in data:
        out.append(
            aws_sdk_entityresolution.types.delete_unique_id_error.deserialize_json(item)
        )
    return out
