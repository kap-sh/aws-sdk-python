"""Generated from Smithy shape ``com.amazonaws.kms#GrantList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.grant_list_entry

GrantList: TypeAlias = list["aws_sdk_kms.types.grant_list_entry.GrantListEntry"]
