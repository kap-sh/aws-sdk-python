"""Generated from Smithy shape ``com.amazonaws.ram#ReplacePermissionAssociationsWorkIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ram.types.string

ReplacePermissionAssociationsWorkIdList: TypeAlias = list[
    "aws_sdk_ram.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplacePermissionAssociationsWorkIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ReplacePermissionAssociationsWorkIdList:
    return list(data)
