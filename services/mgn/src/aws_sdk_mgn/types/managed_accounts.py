"""Generated from Smithy shape ``com.amazonaws.mgn#ManagedAccounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.managed_account

ManagedAccounts: TypeAlias = list["aws_sdk_mgn.types.managed_account.ManagedAccount"]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedAccounts) -> list:
    import aws_sdk_mgn.types.managed_account

    out: list = []
    for item in value:
        out.append(aws_sdk_mgn.types.managed_account.serialize_json(item))
    return out


def deserialize_json(data: list) -> ManagedAccounts:
    import aws_sdk_mgn.types.managed_account

    out: ManagedAccounts = []
    for item in data:
        out.append(aws_sdk_mgn.types.managed_account.deserialize_json(item))
    return out
