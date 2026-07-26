"""Generated from Smithy shape ``com.amazonaws.auditmanager#AWSAccounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.aws_account

AWSAccounts: TypeAlias = list["capo_auditmanager.types.aws_account.AWSAccount"]


# --- restJson1 ser/de ---
def serialize_json(value: AWSAccounts) -> list:
    import capo_auditmanager.types.aws_account

    out: list = []
    for item in value:
        out.append(capo_auditmanager.types.aws_account.serialize_json(item))
    return out


def deserialize_json(data: list) -> AWSAccounts:
    import capo_auditmanager.types.aws_account

    out: AWSAccounts = []
    for item in data:
        out.append(capo_auditmanager.types.aws_account.deserialize_json(item))
    return out
