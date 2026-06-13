"""Generated from Smithy shape ``com.amazonaws.drs#AccountIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.account_id

AccountIDs: TypeAlias = list["aws_sdk_drs.types.account_id.AccountID"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> AccountIDs:
    return list(data)
