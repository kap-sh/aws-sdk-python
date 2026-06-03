"""Generated from Smithy shape ``com.amazonaws.kms#EncryptionAlgorithmSpecList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.encryption_algorithm_spec

EncryptionAlgorithmSpecList: TypeAlias = list[
    "aws_sdk_kms.types.encryption_algorithm_spec.EncryptionAlgorithmSpec"
]
