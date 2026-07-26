"""Generated from Smithy shape ``com.amazonaws.networkmanager#AccountStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.account_status

AccountStatusList: TypeAlias = list[
    "capo_networkmanager.types.account_status.AccountStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountStatusList) -> list:
    import capo_networkmanager.types.account_status

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.account_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountStatusList:
    import capo_networkmanager.types.account_status

    out: AccountStatusList = []
    for item in data:
        out.append(capo_networkmanager.types.account_status.deserialize_json(item))
    return out
