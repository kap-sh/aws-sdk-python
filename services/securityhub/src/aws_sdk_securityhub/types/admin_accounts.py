"""Generated from Smithy shape ``com.amazonaws.securityhub#AdminAccounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.admin_account

AdminAccounts: TypeAlias = list["aws_sdk_securityhub.types.admin_account.AdminAccount"]


# --- restJson1 ser/de ---
def serialize_json(value: AdminAccounts) -> list:
    import aws_sdk_securityhub.types.admin_account

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.admin_account.serialize_json(item))
    return out


def deserialize_json(data: list) -> AdminAccounts:
    import aws_sdk_securityhub.types.admin_account

    out: AdminAccounts = []
    for item in data:
        out.append(aws_sdk_securityhub.types.admin_account.deserialize_json(item))
    return out
