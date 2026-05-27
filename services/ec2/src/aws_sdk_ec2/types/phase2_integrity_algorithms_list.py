"""Generated from Smithy shape ``com.amazonaws.ec2#Phase2IntegrityAlgorithmsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.phase2_integrity_algorithms_list_value

Phase2IntegrityAlgorithmsList: TypeAlias = list[
    "aws_sdk_ec2.types.phase2_integrity_algorithms_list_value.Phase2IntegrityAlgorithmsListValue"
]
