"""Generated from Smithy shape ``com.amazonaws.inspector2#DelegatedAdminAccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.delegated_admin_account

DelegatedAdminAccountList: TypeAlias = list[
    "aws_sdk_inspector2.types.delegated_admin_account.DelegatedAdminAccount"
]


# --- restJson1 ser/de ---
def serialize_json(value: DelegatedAdminAccountList) -> list:
    import aws_sdk_inspector2.types.delegated_admin_account

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector2.types.delegated_admin_account.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DelegatedAdminAccountList:
    import aws_sdk_inspector2.types.delegated_admin_account

    out: DelegatedAdminAccountList = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.delegated_admin_account.deserialize_json(item)
        )
    return out
