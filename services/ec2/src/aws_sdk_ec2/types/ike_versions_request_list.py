"""Generated from Smithy shape ``com.amazonaws.ec2#IKEVersionsRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ike_versions_request_list_value

IKEVersionsRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.ike_versions_request_list_value.IKEVersionsRequestListValue"
]
