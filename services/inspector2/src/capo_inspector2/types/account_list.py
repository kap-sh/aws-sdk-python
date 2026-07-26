"""Generated from Smithy shape ``com.amazonaws.inspector2#AccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.account

AccountList: TypeAlias = list["capo_inspector2.types.account.Account"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountList) -> list:
    import capo_inspector2.types.account

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.account.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountList:
    import capo_inspector2.types.account

    out: AccountList = []
    for item in data:
        out.append(capo_inspector2.types.account.deserialize_json(item))
    return out
