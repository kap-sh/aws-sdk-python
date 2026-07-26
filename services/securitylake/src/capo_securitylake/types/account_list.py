"""Generated from Smithy shape ``com.amazonaws.securitylake#AccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securitylake.types.aws_account_id

AccountList: TypeAlias = list["capo_securitylake.types.aws_account_id.AwsAccountId"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountList) -> list:
    return list(value)


def deserialize_json(data: list) -> AccountList:
    return list(data)
