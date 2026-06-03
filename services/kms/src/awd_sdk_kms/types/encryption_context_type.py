"""Generated from Smithy shape ``com.amazonaws.kms#EncryptionContextType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import awd_sdk_kms.types.encryption_context_key
    import awd_sdk_kms.types.encryption_context_value

EncryptionContextType: TypeAlias = dict[
    "awd_sdk_kms.types.encryption_context_key.EncryptionContextKey",
    "awd_sdk_kms.types.encryption_context_value.EncryptionContextValue",
]
