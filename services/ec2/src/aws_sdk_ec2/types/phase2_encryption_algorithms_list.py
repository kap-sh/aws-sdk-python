"""Generated from Smithy shape ``com.amazonaws.ec2#Phase2EncryptionAlgorithmsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.phase2_encryption_algorithms_list_value

Phase2EncryptionAlgorithmsList: TypeAlias = list[
    "aws_sdk_ec2.types.phase2_encryption_algorithms_list_value.Phase2EncryptionAlgorithmsListValue"
]
