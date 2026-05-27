"""Generated from Smithy shape ``com.amazonaws.ec2#Phase1DHGroupNumbersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.phase1_dh_group_numbers_list_value

Phase1DHGroupNumbersList: TypeAlias = list[
    "aws_sdk_ec2.types.phase1_dh_group_numbers_list_value.Phase1DHGroupNumbersListValue"
]
