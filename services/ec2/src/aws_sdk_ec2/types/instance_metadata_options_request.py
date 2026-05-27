"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceMetadataOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.http_tokens_state
    import aws_sdk_ec2.types.instance_metadata_endpoint_state
    import aws_sdk_ec2.types.instance_metadata_protocol_state
    import aws_sdk_ec2.types.instance_metadata_tags_state
    import aws_sdk_ec2.types.integer


class InstanceMetadataOptionsRequest(TypedDict):
    http_tokens: NotRequired["aws_sdk_ec2.types.http_tokens_state.HttpTokensState"]
    """<p>Indicates whether IMDSv2 is required.</p> <ul> <li> <p> <code>optional</code> - IMDSv2 is optional, which means that you can use either IMDSv2 or IMDSv1.</p> </li> <li> <p> <code>required</code> - IMDSv2 is required, which means that IMDSv1 is disabled, and you must use IMDSv2.</p> </li> </ul> <p>Default:</p> <ul> <li> <p>If the value of <code>ImdsSupport</code> for the Amazon Machine Image (AMI) for your instance is <code>v2.0</code> and the account level default is set to <code>no-preference</code>, the default is <code>required</code>.</p> </li> <li> <p>If the value of <code>ImdsSupport</code> for the Amazon Machine Image (AMI) for your instance is <code>v2.0</code>, but the account level default is set to <code>V1 or V2</code>, the default is <code>optional</code>.</p> </li> </ul> <p>The default value can also be affected by other combinations of parameters. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html#instance-metadata-options-order-of-precedence\">Order of precedence for instance metadata options</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    http_put_response_hop_limit: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of hops that the metadata token can travel.</p> <p>Possible values: Integers from 1 to 64</p>"""
    http_endpoint: NotRequired[
        "aws_sdk_ec2.types.instance_metadata_endpoint_state.InstanceMetadataEndpointState"
    ]
    """<p>Enables or disables the HTTP metadata endpoint on your instances.</p> <p>If you specify a value of <code>disabled</code>, you cannot access your instance metadata.</p> <p>Default: <code>enabled</code> </p>"""
    http_protocol_ipv6: NotRequired[
        "aws_sdk_ec2.types.instance_metadata_protocol_state.InstanceMetadataProtocolState"
    ]
    """<p>Enables or disables the IPv6 endpoint for the instance metadata service.</p> <p>Default: <code>disabled</code> </p>"""
    instance_metadata_tags: NotRequired[
        "aws_sdk_ec2.types.instance_metadata_tags_state.InstanceMetadataTagsState"
    ]
    """<p>Set to <code>enabled</code> to allow access to instance tags from the instance metadata. Set to <code>disabled</code> to turn off access to instance tags from the instance metadata. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html\">View tags for your EC2 instances using instance metadata</a>.</p> <p>Default: <code>disabled</code> </p>"""
