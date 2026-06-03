"""Generated from Smithy shape ``com.amazonaws.kms#KeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import awd_sdk_kms.types.key_list_entry

KeyList: TypeAlias = list["awd_sdk_kms.types.key_list_entry.KeyListEntry"]
