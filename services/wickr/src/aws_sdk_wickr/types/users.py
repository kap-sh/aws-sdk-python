"""Generated from Smithy shape ``com.amazonaws.wickr#Users``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wickr.types.user

Users: TypeAlias = list["aws_sdk_wickr.types.user.User"]


# --- restJson1 ser/de ---
def serialize_json(value: Users) -> list:
    import aws_sdk_wickr.types.user

    out: list = []
    for item in value:
        out.append(aws_sdk_wickr.types.user.serialize_json(item))
    return out


def deserialize_json(data: list) -> Users:
    import aws_sdk_wickr.types.user

    out: Users = []
    for item in data:
        out.append(aws_sdk_wickr.types.user.deserialize_json(item))
    return out
