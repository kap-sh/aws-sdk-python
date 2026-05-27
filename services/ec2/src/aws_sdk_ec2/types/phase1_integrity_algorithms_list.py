"""Generated from Smithy shape ``com.amazonaws.ec2#Phase1IntegrityAlgorithmsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.phase1_integrity_algorithms_list_value

Phase1IntegrityAlgorithmsList: TypeAlias = list[
    "aws_sdk_ec2.types.phase1_integrity_algorithms_list_value.Phase1IntegrityAlgorithmsListValue"
]
