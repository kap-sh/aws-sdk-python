"""Generated from Smithy shape ``com.amazonaws.kms#KeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.key_list_entry

KeyList: TypeAlias = list["aws_sdk_kms.types.key_list_entry.KeyListEntry"]
