"""Generated from Smithy shape ``com.amazonaws.detective#AccountIdExtendedList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_detective.types.account_id

AccountIdExtendedList: TypeAlias = list["aws_sdk_detective.types.account_id.AccountId"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountIdExtendedList) -> list:
    return list(value)


def deserialize_json(data: list) -> AccountIdExtendedList:
    return list(data)
