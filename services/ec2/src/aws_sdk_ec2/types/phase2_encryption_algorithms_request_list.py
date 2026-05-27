"""Generated from Smithy shape ``com.amazonaws.ec2#Phase2EncryptionAlgorithmsRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.phase2_encryption_algorithms_request_list_value

Phase2EncryptionAlgorithmsRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.phase2_encryption_algorithms_request_list_value.Phase2EncryptionAlgorithmsRequestListValue"
]
