"""Generated from Smithy shape ``com.amazonaws.auditmanager#AWSAccounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.aws_account

AWSAccounts: TypeAlias = list["aws_sdk_auditmanager.types.aws_account.AWSAccount"]


# --- restJson1 ser/de ---
def serialize_json(value: AWSAccounts) -> list:
    import aws_sdk_auditmanager.types.aws_account

    out: list = []
    for item in value:
        out.append(aws_sdk_auditmanager.types.aws_account.serialize_json(item))
    return out


def deserialize_json(data: list) -> AWSAccounts:
    import aws_sdk_auditmanager.types.aws_account

    out: AWSAccounts = []
    for item in data:
        out.append(aws_sdk_auditmanager.types.aws_account.deserialize_json(item))
    return out
