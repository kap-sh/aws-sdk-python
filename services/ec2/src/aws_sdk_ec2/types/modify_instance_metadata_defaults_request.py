"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceMetadataDefaultsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.boxed_integer
    import aws_sdk_ec2.types.default_http_tokens_enforced_state
    import aws_sdk_ec2.types.default_instance_metadata_endpoint_state
    import aws_sdk_ec2.types.default_instance_metadata_tags_state
    import aws_sdk_ec2.types.metadata_default_http_tokens_state


class ModifyInstanceMetadataDefaultsRequest(TypedDict):
    http_tokens: NotRequired[
        "aws_sdk_ec2.types.metadata_default_http_tokens_state.MetadataDefaultHttpTokensState"
    ]
    """<p>Indicates whether IMDSv2 is required.</p> <ul> <li> <p> <code>optional</code> – IMDSv2 is optional, which means that you can use either IMDSv2 or IMDSv1.</p> </li> <li> <p> <code>required</code> – IMDSv2 is required, which means that IMDSv1 is disabled, and you must use IMDSv2.</p> </li> </ul>"""
    http_put_response_hop_limit: NotRequired[
        "aws_sdk_ec2.types.boxed_integer.BoxedInteger"
    ]
    """<p>The maximum number of hops that the metadata token can travel. To indicate no preference, specify <code>-1</code>.</p> <p>Possible values: Integers from <code>1</code> to <code>64</code>, and <code>-1</code> to indicate no preference</p>"""
    http_endpoint: NotRequired[
        "aws_sdk_ec2.types.default_instance_metadata_endpoint_state.DefaultInstanceMetadataEndpointState"
    ]
    """<p>Enables or disables the IMDS endpoint on an instance. When disabled, the instance metadata can't be accessed.</p>"""
    instance_metadata_tags: NotRequired[
        "aws_sdk_ec2.types.default_instance_metadata_tags_state.DefaultInstanceMetadataTagsState"
    ]
    """<p>Enables or disables access to an instance's tags from the instance metadata. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html\">View tags for your EC2 instances using instance metadata</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    http_tokens_enforced: NotRequired[
        "aws_sdk_ec2.types.default_http_tokens_enforced_state.DefaultHttpTokensEnforcedState"
    ]
    """<p>Specifies whether to enforce the requirement of IMDSv2 on an instance at the time of launch. When enforcement is enabled, the instance can't launch unless IMDSv2 (<code>HttpTokens</code>) is set to <code>required</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#enforce-imdsv2-at-the-account-level\">Enforce IMDSv2 at the account level</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
