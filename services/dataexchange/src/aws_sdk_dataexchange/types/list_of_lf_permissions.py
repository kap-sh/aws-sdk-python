"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfLFPermissions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.lf_permission

ListOfLFPermissions: TypeAlias = list[
    "aws_sdk_dataexchange.types.lf_permission.LFPermission"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfLFPermissions) -> list:
    return list(value)


def deserialize_json(data: list) -> ListOfLFPermissions:
    return list(data)
