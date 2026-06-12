"""Generated from Smithy shape ``com.amazonaws.connect#AllowedUserActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.allowed_user_action

AllowedUserActions: TypeAlias = list[
    "aws_sdk_connect.types.allowed_user_action.AllowedUserAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedUserActions) -> list:
    import aws_sdk_connect.types.allowed_user_action

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.allowed_user_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> AllowedUserActions:
    import aws_sdk_connect.types.allowed_user_action

    out: AllowedUserActions = []
    for item in data:
        out.append(aws_sdk_connect.types.allowed_user_action.deserialize_json(item))
    return out
