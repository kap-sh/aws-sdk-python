"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceMetadataOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.http_tokens_state
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.instance_metadata_endpoint_state
    import aws_sdk_ec2.types.instance_metadata_protocol_state
    import aws_sdk_ec2.types.instance_metadata_tags_state
    import aws_sdk_ec2.types.integer


class ModifyInstanceMetadataOptionsRequest(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    http_tokens: NotRequired["aws_sdk_ec2.types.http_tokens_state.HttpTokensState"]
    """<p>Indicates whether IMDSv2 is required.</p> <ul> <li> <p> <code>optional</code> - IMDSv2 is optional. You can choose whether to send a session token in your instance metadata retrieval requests. If you retrieve IAM role credentials without a session token, you receive the IMDSv1 role credentials. If you retrieve IAM role credentials using a valid session token, you receive the IMDSv2 role credentials.</p> </li> <li> <p> <code>required</code> - IMDSv2 is required. You must send a session token in your instance metadata retrieval requests. With this option, retrieving the IAM role credentials always returns IMDSv2 credentials; IMDSv1 credentials are not available.</p> </li> </ul> <p>Default:</p> <ul> <li> <p>If the value of <code>ImdsSupport</code> for the Amazon Machine Image (AMI) for your instance is <code>v2.0</code> and the account level default is set to <code>no-preference</code>, the default is <code>required</code>.</p> </li> <li> <p>If the value of <code>ImdsSupport</code> for the Amazon Machine Image (AMI) for your instance is <code>v2.0</code>, but the account level default is set to <code>V1 or V2</code>, the default is <code>optional</code>.</p> </li> </ul> <p>The default value can also be affected by other combinations of parameters. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html#instance-metadata-options-order-of-precedence\">Order of precedence for instance metadata options</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    http_put_response_hop_limit: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The desired HTTP PUT response hop limit for instance metadata requests. The larger the number, the further instance metadata requests can travel. If no parameter is specified, the existing state is maintained.</p> <p>Possible values: Integers from 1 to 64</p>"""
    http_endpoint: NotRequired[
        "aws_sdk_ec2.types.instance_metadata_endpoint_state.InstanceMetadataEndpointState"
    ]
    """<p>Enables or disables the HTTP metadata endpoint on your instances. If this parameter is not specified, the existing state is maintained.</p> <p>If you specify a value of <code>disabled</code>, you cannot access your instance metadata.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    http_protocol_ipv6: NotRequired[
        "aws_sdk_ec2.types.instance_metadata_protocol_state.InstanceMetadataProtocolState"
    ]
    """<p>Enables or disables the IPv6 endpoint for the instance metadata service. Applies only if you enabled the HTTP metadata endpoint.</p>"""
    instance_metadata_tags: NotRequired[
        "aws_sdk_ec2.types.instance_metadata_tags_state.InstanceMetadataTagsState"
    ]
    """<p>Set to <code>enabled</code> to allow access to instance tags from the instance metadata. Set to <code>disabled</code> to turn off access to instance tags from the instance metadata. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html\">View tags for your EC2 instances using instance metadata</a>.</p>"""
