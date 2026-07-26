"""Generated from Smithy shape ``com.amazonaws.sso#AccountListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sso.types.account_info

AccountListType: TypeAlias = list["capo_sso.types.account_info.AccountInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountListType) -> list:
    import capo_sso.types.account_info

    out: list = []
    for item in value:
        out.append(capo_sso.types.account_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountListType:
    import capo_sso.types.account_info

    out: AccountListType = []
    for item in data:
        out.append(capo_sso.types.account_info.deserialize_json(item))
    return out
