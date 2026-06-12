"""Generated from Smithy shape ``com.amazonaws.signer#EncryptionAlgorithms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_signer.types.encryption_algorithm

EncryptionAlgorithms: TypeAlias = list[
    "aws_sdk_signer.types.encryption_algorithm.EncryptionAlgorithm"
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionAlgorithms) -> list:
    import aws_sdk_signer.types.encryption_algorithm

    out: list = []
    for item in value:
        out.append(aws_sdk_signer.types.encryption_algorithm.serialize_json(item))
    return out


def deserialize_json(data: list) -> EncryptionAlgorithms:
    import aws_sdk_signer.types.encryption_algorithm

    out: EncryptionAlgorithms = []
    for item in data:
        out.append(aws_sdk_signer.types.encryption_algorithm.deserialize_json(item))
    return out
