"""Generated from Smithy shape ``com.amazonaws.chime#AccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime.types.account

AccountList: TypeAlias = list["aws_sdk_chime.types.account.Account"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountList) -> list:
    import aws_sdk_chime.types.account

    out: list = []
    for item in value:
        out.append(aws_sdk_chime.types.account.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountList:
    import aws_sdk_chime.types.account

    out: AccountList = []
    for item in data:
        out.append(aws_sdk_chime.types.account.deserialize_json(item))
    return out
