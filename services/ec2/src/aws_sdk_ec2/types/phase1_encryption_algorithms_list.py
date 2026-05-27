"""Generated from Smithy shape ``com.amazonaws.ec2#Phase1EncryptionAlgorithmsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.phase1_encryption_algorithms_list_value

Phase1EncryptionAlgorithmsList: TypeAlias = list[
    "aws_sdk_ec2.types.phase1_encryption_algorithms_list_value.Phase1EncryptionAlgorithmsListValue"
]
