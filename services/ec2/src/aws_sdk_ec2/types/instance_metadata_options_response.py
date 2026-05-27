"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceMetadataOptionsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.http_tokens_state
    import aws_sdk_ec2.types.instance_metadata_endpoint_state
    import aws_sdk_ec2.types.instance_metadata_options_state
    import aws_sdk_ec2.types.instance_metadata_protocol_state
    import aws_sdk_ec2.types.instance_metadata_tags_state
    import aws_sdk_ec2.types.integer


class InstanceMetadataOptionsResponse(TypedDict):
    state: NotRequired[
        "aws_sdk_ec2.types.instance_metadata_options_state.InstanceMetadataOptionsState"
    ]
    """<p>The state of the metadata option changes.</p> <p> <code>pending</code> - The metadata options are being updated and the instance is not ready to process metadata traffic with the new selection.</p> <p> <code>applied</code> - The metadata options have been successfully applied on the instance.</p>"""
    http_tokens: NotRequired["aws_sdk_ec2.types.http_tokens_state.HttpTokensState"]
    """<p>Indicates whether IMDSv2 is required.</p> <ul> <li> <p> <code>optional</code> - IMDSv2 is optional, which means that you can use either IMDSv2 or IMDSv1.</p> </li> <li> <p> <code>required</code> - IMDSv2 is required, which means that IMDSv1 is disabled, and you must use IMDSv2.</p> </li> </ul>"""
    http_put_response_hop_limit: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of hops that the metadata token can travel.</p> <p>Possible values: Integers from <code>1</code> to <code>64</code> </p>"""
    http_endpoint: NotRequired[
        "aws_sdk_ec2.types.instance_metadata_endpoint_state.InstanceMetadataEndpointState"
    ]
    """<p>Indicates whether the HTTP metadata endpoint on your instances is enabled or disabled.</p> <p>If the value is <code>disabled</code>, you cannot access your instance metadata.</p>"""
    http_protocol_ipv6: NotRequired[
        "aws_sdk_ec2.types.instance_metadata_protocol_state.InstanceMetadataProtocolState"
    ]
    """<p>Indicates whether the IPv6 endpoint for the instance metadata service is enabled or disabled.</p> <p>Default: <code>disabled</code> </p>"""
    instance_metadata_tags: NotRequired[
        "aws_sdk_ec2.types.instance_metadata_tags_state.InstanceMetadataTagsState"
    ]
    """<p>Indicates whether access to instance tags from the instance metadata is enabled or disabled. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html\">View tags for your EC2 instances using instance metadata</a>.</p>"""
