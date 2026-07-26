"""Generated from Smithy shape ``com.amazonaws.inspector2#AccountStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.account_state

AccountStateList: TypeAlias = list["capo_inspector2.types.account_state.AccountState"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountStateList) -> list:
    import capo_inspector2.types.account_state

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.account_state.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountStateList:
    import capo_inspector2.types.account_state

    out: AccountStateList = []
    for item in data:
        out.append(capo_inspector2.types.account_state.deserialize_json(item))
    return out
