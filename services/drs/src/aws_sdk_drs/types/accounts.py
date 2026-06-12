"""Generated from Smithy shape ``com.amazonaws.drs#Accounts``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_drs.types.account

Accounts: TypeAlias = list["aws_sdk_drs.types.account.Account"]


# --- restJson1 ser/de ---
def serialize_json(value: Accounts) -> list:
    import aws_sdk_drs.types.account
    out: list = []
    for item in value:
        out.append(aws_sdk_drs.types.account.serialize_json(item))
    return out


def deserialize_json(data: list) -> Accounts:
    import aws_sdk_drs.types.account
    out: Accounts = []
    for item in data:
        out.append(aws_sdk_drs.types.account.deserialize_json(item))
    return out