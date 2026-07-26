"""Generated from Smithy shape ``com.amazonaws.inspector2#AccountIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.account_id

AccountIdSet: TypeAlias = list["capo_inspector2.types.account_id.AccountId"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountIdSet) -> list:
    return list(value)


def deserialize_json(data: list) -> AccountIdSet:
    return list(data)
