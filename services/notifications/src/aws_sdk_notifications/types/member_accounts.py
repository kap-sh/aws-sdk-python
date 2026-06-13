"""Generated from Smithy shape ``com.amazonaws.notifications#MemberAccounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_notifications.types.member_account

MemberAccounts: TypeAlias = list[
    "aws_sdk_notifications.types.member_account.MemberAccount"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemberAccounts) -> list:
    import aws_sdk_notifications.types.member_account

    out: list = []
    for item in value:
        out.append(aws_sdk_notifications.types.member_account.serialize_json(item))
    return out


def deserialize_json(data: list) -> MemberAccounts:
    import aws_sdk_notifications.types.member_account

    out: MemberAccounts = []
    for item in data:
        out.append(aws_sdk_notifications.types.member_account.deserialize_json(item))
    return out
