"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointServiceConfigurationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.service_configuration_set
    import aws_sdk_ec2.types.string


class DescribeVpcEndpointServiceConfigurationsResult(TypedDict):
    service_configurations: NotRequired[
        "aws_sdk_ec2.types.service_configuration_set.ServiceConfigurationSet"
    ]
    """<p>Information about the services.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
