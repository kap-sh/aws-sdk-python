"""Generated from Smithy shape ``com.amazonaws.kms#EncryptionAlgorithmSpec``."""

from typing import Literal, TypeAlias

EncryptionAlgorithmSpec: TypeAlias = Literal[
    "SYMMETRIC_DEFAULT",
    "RSAES_OAEP_SHA_1",
    "RSAES_OAEP_SHA_256",
    "SM2PKE",
]
