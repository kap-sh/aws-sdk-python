"""Generated from Smithy shape ``com.amazonaws.chime#UserEmailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime.types.email_address

UserEmailList: TypeAlias = list["aws_sdk_chime.types.email_address.EmailAddress"]


# --- restJson1 ser/de ---
def serialize_json(value: UserEmailList) -> list:
    return list(value)


def deserialize_json(data: list) -> UserEmailList:
    return list(data)
