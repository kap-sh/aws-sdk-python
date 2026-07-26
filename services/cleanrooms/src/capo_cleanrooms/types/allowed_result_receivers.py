"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AllowedResultReceivers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.account_id

AllowedResultReceivers: TypeAlias = list["capo_cleanrooms.types.account_id.AccountId"]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedResultReceivers) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedResultReceivers:
    return list(data)
