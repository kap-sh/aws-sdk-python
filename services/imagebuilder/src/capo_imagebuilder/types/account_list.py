"""Generated from Smithy shape ``com.amazonaws.imagebuilder#AccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.account_id

AccountList: TypeAlias = list["capo_imagebuilder.types.account_id.AccountId"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountList) -> list:
    return list(value)


def deserialize_json(data: list) -> AccountList:
    return list(data)
