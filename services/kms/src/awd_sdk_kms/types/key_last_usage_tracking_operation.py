"""Generated from Smithy shape ``com.amazonaws.kms#KeyLastUsageTrackingOperation``."""

from typing import Literal, TypeAlias

KeyLastUsageTrackingOperation: TypeAlias = Literal[
    "Decrypt",
    "DeriveSharedSecret",
    "Encrypt",
    "GenerateDataKey",
    "GenerateDataKeyPair",
    "GenerateDataKeyPairWithoutPlaintext",
    "GenerateDataKeyWithoutPlaintext",
    "GenerateMac",
    "ReEncrypt",
    "Sign",
    "Verify",
    "VerifyMac",
]
