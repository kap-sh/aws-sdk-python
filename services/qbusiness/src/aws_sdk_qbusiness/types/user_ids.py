"""Generated from Smithy shape ``com.amazonaws.qbusiness#UserIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.string

UserIds: TypeAlias = list["aws_sdk_qbusiness.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: UserIds) -> list:
    return list(value)


def deserialize_json(data: list) -> UserIds:
    return list(data)
