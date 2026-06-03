"""Generated from Smithy shape ``com.amazonaws.kms#GrantTokenList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.grant_token_type

GrantTokenList: TypeAlias = list["aws_sdk_kms.types.grant_token_type.GrantTokenType"]
