"""Generated from Smithy shape ``com.amazonaws.devopsguru#AccountHealths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.account_health

AccountHealths: TypeAlias = list["capo_devops_guru.types.account_health.AccountHealth"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountHealths) -> list:
    import capo_devops_guru.types.account_health

    out: list = []
    for item in value:
        out.append(capo_devops_guru.types.account_health.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountHealths:
    import capo_devops_guru.types.account_health

    out: AccountHealths = []
    for item in data:
        out.append(capo_devops_guru.types.account_health.deserialize_json(item))
    return out
