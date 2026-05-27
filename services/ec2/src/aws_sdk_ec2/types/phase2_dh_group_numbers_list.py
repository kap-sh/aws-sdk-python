"""Generated from Smithy shape ``com.amazonaws.ec2#Phase2DHGroupNumbersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.phase2_dh_group_numbers_list_value

Phase2DHGroupNumbersList: TypeAlias = list[
    "aws_sdk_ec2.types.phase2_dh_group_numbers_list_value.Phase2DHGroupNumbersListValue"
]
