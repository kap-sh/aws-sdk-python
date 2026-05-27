"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateInstanceMetadataOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.launch_template_http_tokens_state
    import aws_sdk_ec2.types.launch_template_instance_metadata_endpoint_state
    import aws_sdk_ec2.types.launch_template_instance_metadata_protocol_ipv6
    import aws_sdk_ec2.types.launch_template_instance_metadata_tags_state


class LaunchTemplateInstanceMetadataOptionsRequest(TypedDict):
    http_tokens: NotRequired[
        "aws_sdk_ec2.types.launch_template_http_tokens_state.LaunchTemplateHttpTokensState"
    ]
    """<p>Indicates whether IMDSv2 is required.</p> <ul> <li> <p> <code>optional</code> - IMDSv2 is optional. You can choose whether to send a session token in your instance metadata retrieval requests. If you retrieve IAM role credentials without a session token, you receive the IMDSv1 role credentials. If you retrieve IAM role credentials using a valid session token, you receive the IMDSv2 role credentials.</p> </li> <li> <p> <code>required</code> - IMDSv2 is required. You must send a session token in your instance metadata retrieval requests. With this option, retrieving the IAM role credentials always returns IMDSv2 credentials; IMDSv1 credentials are not available.</p> </li> </ul> <p>Default: If the value of <code>ImdsSupport</code> for the Amazon Machine Image (AMI) for your instance is <code>v2.0</code>, the default is <code>required</code>.</p>"""
    http_put_response_hop_limit: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The desired HTTP PUT response hop limit for instance metadata requests. The larger the number, the further instance metadata requests can travel.</p> <p>Default: <code>1</code> </p> <p>Possible values: Integers from 1 to 64</p>"""
    http_endpoint: NotRequired[
        "aws_sdk_ec2.types.launch_template_instance_metadata_endpoint_state.LaunchTemplateInstanceMetadataEndpointState"
    ]
    """<p>Enables or disables the HTTP metadata endpoint on your instances. If the parameter is not specified, the default state is <code>enabled</code>.</p> <note> <p>If you specify a value of <code>disabled</code>, you will not be able to access your instance metadata. </p> </note>"""
    http_protocol_ipv6: NotRequired[
        "aws_sdk_ec2.types.launch_template_instance_metadata_protocol_ipv6.LaunchTemplateInstanceMetadataProtocolIpv6"
    ]
    """<p>Enables or disables the IPv6 endpoint for the instance metadata service.</p> <p>Default: <code>disabled</code> </p>"""
    instance_metadata_tags: NotRequired[
        "aws_sdk_ec2.types.launch_template_instance_metadata_tags_state.LaunchTemplateInstanceMetadataTagsState"
    ]
    """<p>Set to <code>enabled</code> to allow access to instance tags from the instance metadata. Set to <code>disabled</code> to turn off access to instance tags from the instance metadata. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html\">View tags for your EC2 instances using instance metadata</a>.</p> <p>Default: <code>disabled</code> </p>"""
