"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#AccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.account_id

AccountIdList: TypeAlias = list["capo_resource_explorer_2.types.account_id.AccountId"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AccountIdList:
    return list(data)
