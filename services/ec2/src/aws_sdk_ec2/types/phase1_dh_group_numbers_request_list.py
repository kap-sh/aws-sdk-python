"""Generated from Smithy shape ``com.amazonaws.ec2#Phase1DHGroupNumbersRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.phase1_dh_group_numbers_request_list_value

Phase1DHGroupNumbersRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.phase1_dh_group_numbers_request_list_value.Phase1DHGroupNumbersRequestListValue"
]
