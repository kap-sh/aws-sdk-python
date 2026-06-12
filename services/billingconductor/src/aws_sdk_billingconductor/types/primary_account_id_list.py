"""Generated from Smithy shape ``com.amazonaws.billingconductor#PrimaryAccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.account_id

PrimaryAccountIdList: TypeAlias = list[
    "aws_sdk_billingconductor.types.account_id.AccountId"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrimaryAccountIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> PrimaryAccountIdList:
    return list(data)
