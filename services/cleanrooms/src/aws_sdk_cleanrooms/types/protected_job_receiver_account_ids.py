"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobReceiverAccountIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.account_id

ProtectedJobReceiverAccountIds: TypeAlias = list[
    "aws_sdk_cleanrooms.types.account_id.AccountId"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobReceiverAccountIds) -> list:
    return list(value)


def deserialize_json(data: list) -> ProtectedJobReceiverAccountIds:
    return list(data)
