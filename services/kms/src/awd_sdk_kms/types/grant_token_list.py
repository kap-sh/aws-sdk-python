"""Generated from Smithy shape ``com.amazonaws.kms#GrantTokenList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import awd_sdk_kms.types.grant_token_type

GrantTokenList: TypeAlias = list["awd_sdk_kms.types.grant_token_type.GrantTokenType"]
