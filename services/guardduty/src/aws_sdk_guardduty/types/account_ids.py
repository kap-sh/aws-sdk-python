"""Generated from Smithy shape ``com.amazonaws.guardduty#AccountIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.account_id

AccountIds: TypeAlias = list["aws_sdk_guardduty.types.account_id.AccountId"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountIds) -> list:
    return list(value)


def deserialize_json(data: list) -> AccountIds:
    return list(data)
