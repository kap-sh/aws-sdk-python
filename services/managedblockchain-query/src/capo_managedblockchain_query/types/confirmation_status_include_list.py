"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ConfirmationStatusIncludeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.confirmation_status

ConfirmationStatusIncludeList: TypeAlias = list[
    "capo_managedblockchain_query.types.confirmation_status.ConfirmationStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfirmationStatusIncludeList) -> list:
    return list(value)


def deserialize_json(data: list) -> ConfirmationStatusIncludeList:
    return list(data)
