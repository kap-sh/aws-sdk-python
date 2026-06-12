"""Generated from Smithy shape ``com.amazonaws.wickr#GuestUserList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wickr.types.guest_user

GuestUserList: TypeAlias = list["aws_sdk_wickr.types.guest_user.GuestUser"]


# --- restJson1 ser/de ---
def serialize_json(value: GuestUserList) -> list:
    import aws_sdk_wickr.types.guest_user

    out: list = []
    for item in value:
        out.append(aws_sdk_wickr.types.guest_user.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuestUserList:
    import aws_sdk_wickr.types.guest_user

    out: GuestUserList = []
    for item in data:
        out.append(aws_sdk_wickr.types.guest_user.deserialize_json(item))
    return out
