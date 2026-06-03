"""Generated from Smithy shape ``com.amazonaws.kms#EncryptionContextType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.encryption_context_key
    import aws_sdk_kms.types.encryption_context_value

EncryptionContextType: TypeAlias = dict[
    "aws_sdk_kms.types.encryption_context_key.EncryptionContextKey",
    "aws_sdk_kms.types.encryption_context_value.EncryptionContextValue",
]
