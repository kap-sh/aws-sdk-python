"""Generated from Smithy shape ``com.amazonaws.qbusiness#UserAliases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.user_alias

UserAliases: TypeAlias = list["aws_sdk_qbusiness.types.user_alias.UserAlias"]


# --- restJson1 ser/de ---
def serialize_json(value: UserAliases) -> list:
    import aws_sdk_qbusiness.types.user_alias

    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.user_alias.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserAliases:
    import aws_sdk_qbusiness.types.user_alias

    out: UserAliases = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.user_alias.deserialize_json(item))
    return out
