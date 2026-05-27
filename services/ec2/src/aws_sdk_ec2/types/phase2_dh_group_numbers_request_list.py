"""Generated from Smithy shape ``com.amazonaws.ec2#Phase2DHGroupNumbersRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.phase2_dh_group_numbers_request_list_value

Phase2DHGroupNumbersRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.phase2_dh_group_numbers_request_list_value.Phase2DHGroupNumbersRequestListValue"
]
