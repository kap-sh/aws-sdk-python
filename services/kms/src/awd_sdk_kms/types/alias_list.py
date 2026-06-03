"""Generated from Smithy shape ``com.amazonaws.kms#AliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import awd_sdk_kms.types.alias_list_entry

AliasList: TypeAlias = list["awd_sdk_kms.types.alias_list_entry.AliasListEntry"]
