"""Generated from Smithy shape ``com.amazonaws.kms#KeyUsageType``."""

from typing import Literal, TypeAlias

KeyUsageType: TypeAlias = Literal[
    "SIGN_VERIFY",
    "ENCRYPT_DECRYPT",
    "GENERATE_VERIFY_MAC",
    "KEY_AGREEMENT",
]
