"""Generated from Smithy shape ``com.amazonaws.billingconductor#AccountIdFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.account_id

AccountIdFilterList: TypeAlias = list[
    "capo_billingconductor.types.account_id.AccountId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountIdFilterList) -> list:
    return list(value)


def deserialize_json(data: list) -> AccountIdFilterList:
    return list(data)
