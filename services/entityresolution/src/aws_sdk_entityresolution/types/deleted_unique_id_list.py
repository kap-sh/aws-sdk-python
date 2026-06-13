"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeletedUniqueIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.deleted_unique_id

DeletedUniqueIdList: TypeAlias = list[
    "aws_sdk_entityresolution.types.deleted_unique_id.DeletedUniqueId"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeletedUniqueIdList) -> list:
    import aws_sdk_entityresolution.types.deleted_unique_id

    out: list = []
    for item in value:
        out.append(
            aws_sdk_entityresolution.types.deleted_unique_id.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DeletedUniqueIdList:
    import aws_sdk_entityresolution.types.deleted_unique_id

    out: DeletedUniqueIdList = []
    for item in data:
        out.append(
            aws_sdk_entityresolution.types.deleted_unique_id.deserialize_json(item)
        )
    return out
