"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointServicesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.service_detail_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class DescribeVpcEndpointServicesResult(TypedDict):
    service_names: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The supported services.</p>"""
    service_details: NotRequired[
        "aws_sdk_ec2.types.service_detail_set.ServiceDetailSet"
    ]
    """<p>Information about the service.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""
