"""Generated from Smithy shape ``com.amazonaws.kms#CustomKeyStoresList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.custom_key_stores_list_entry

CustomKeyStoresList: TypeAlias = list[
    "aws_sdk_kms.types.custom_key_stores_list_entry.CustomKeyStoresListEntry"
]
