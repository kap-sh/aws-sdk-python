"""Generated from Smithy shape ``com.amazonaws.detective#AccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_detective.types.account_id

AccountIdList: TypeAlias = list["capo_detective.types.account_id.AccountId"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AccountIdList:
    return list(data)
