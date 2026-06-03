"""Generated from Smithy shape ``com.amazonaws.kms#AliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.alias_list_entry

AliasList: TypeAlias = list["aws_sdk_kms.types.alias_list_entry.AliasListEntry"]
