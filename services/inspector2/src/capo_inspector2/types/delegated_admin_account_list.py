"""Generated from Smithy shape ``com.amazonaws.inspector2#DelegatedAdminAccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.delegated_admin_account

DelegatedAdminAccountList: TypeAlias = list[
    "capo_inspector2.types.delegated_admin_account.DelegatedAdminAccount"
]


# --- restJson1 ser/de ---
def serialize_json(value: DelegatedAdminAccountList) -> list:
    import capo_inspector2.types.delegated_admin_account

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.delegated_admin_account.serialize_json(item))
    return out


def deserialize_json(data: list) -> DelegatedAdminAccountList:
    import capo_inspector2.types.delegated_admin_account

    out: DelegatedAdminAccountList = []
    for item in data:
        out.append(capo_inspector2.types.delegated_admin_account.deserialize_json(item))
    return out
