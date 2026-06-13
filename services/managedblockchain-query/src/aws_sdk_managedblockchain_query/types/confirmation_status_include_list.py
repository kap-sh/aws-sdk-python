"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ConfirmationStatusIncludeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.confirmation_status

ConfirmationStatusIncludeList: TypeAlias = list[
    "aws_sdk_managedblockchain_query.types.confirmation_status.ConfirmationStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfirmationStatusIncludeList) -> list:
    return list(value)


def deserialize_json(data: list) -> ConfirmationStatusIncludeList:
    return list(data)
