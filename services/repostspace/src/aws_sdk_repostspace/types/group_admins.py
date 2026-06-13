"""Generated from Smithy shape ``com.amazonaws.repostspace#GroupAdmins``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.admin_id

GroupAdmins: TypeAlias = list["aws_sdk_repostspace.types.admin_id.AdminId"]


# --- restJson1 ser/de ---
def serialize_json(value: GroupAdmins) -> list:
    return list(value)


def deserialize_json(data: list) -> GroupAdmins:
    return list(data)
