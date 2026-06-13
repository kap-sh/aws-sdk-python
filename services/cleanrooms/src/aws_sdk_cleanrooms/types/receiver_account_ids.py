"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ReceiverAccountIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.account_id

ReceiverAccountIds: TypeAlias = list["aws_sdk_cleanrooms.types.account_id.AccountId"]


# --- restJson1 ser/de ---
def serialize_json(value: ReceiverAccountIds) -> list:
    return list(value)


def deserialize_json(data: list) -> ReceiverAccountIds:
    return list(data)
