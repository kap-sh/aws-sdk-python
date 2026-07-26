"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfAdminAccount``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.admin_account

__listOfAdminAccount: TypeAlias = list["capo_macie2.types.admin_account.AdminAccount"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAdminAccount) -> list:
    import capo_macie2.types.admin_account

    out: list = []
    for item in value:
        out.append(capo_macie2.types.admin_account.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAdminAccount:
    import capo_macie2.types.admin_account

    out: __listOfAdminAccount = []
    for item in data:
        out.append(capo_macie2.types.admin_account.deserialize_json(item))
    return out
