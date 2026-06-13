"""Generated from Smithy shape ``com.amazonaws.qbusiness#UserGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.string

UserGroups: TypeAlias = list["aws_sdk_qbusiness.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: UserGroups) -> list:
    return list(value)


def deserialize_json(data: list) -> UserGroups:
    return list(data)
