"""Generated from Smithy shape ``com.amazonaws.inspector2#UsageAccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.usage_account_id

UsageAccountIdList: TypeAlias = list[
    "capo_inspector2.types.usage_account_id.UsageAccountId"
]


# --- restJson1 ser/de ---
def serialize_json(value: UsageAccountIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> UsageAccountIdList:
    return list(data)
