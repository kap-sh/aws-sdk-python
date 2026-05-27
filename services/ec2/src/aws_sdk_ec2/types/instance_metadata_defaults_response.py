"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceMetadataDefaultsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boxed_integer
    import aws_sdk_ec2.types.http_tokens_enforced_state
    import aws_sdk_ec2.types.http_tokens_state
    import aws_sdk_ec2.types.instance_metadata_endpoint_state
    import aws_sdk_ec2.types.instance_metadata_tags_state
    import aws_sdk_ec2.types.managed_by
    import aws_sdk_ec2.types.string


class InstanceMetadataDefaultsResponse(TypedDict):
    http_tokens: NotRequired["aws_sdk_ec2.types.http_tokens_state.HttpTokensState"]
    """<p>Indicates whether IMDSv2 is required.</p> <ul> <li> <p> <code>optional</code> – IMDSv2 is optional, which means that you can use either IMDSv2 or IMDSv1.</p> </li> <li> <p> <code>required</code> – IMDSv2 is required, which means that IMDSv1 is disabled, and you must use IMDSv2.</p> </li> </ul>"""
    http_put_response_hop_limit: NotRequired[
        "aws_sdk_ec2.types.boxed_integer.BoxedInteger"
    ]
    """<p>The maximum number of hops that the metadata token can travel.</p>"""
    http_endpoint: NotRequired[
        "aws_sdk_ec2.types.instance_metadata_endpoint_state.InstanceMetadataEndpointState"
    ]
    """<p>Indicates whether the IMDS endpoint for an instance is enabled or disabled. When disabled, the instance metadata can't be accessed.</p>"""
    instance_metadata_tags: NotRequired[
        "aws_sdk_ec2.types.instance_metadata_tags_state.InstanceMetadataTagsState"
    ]
    """<p>Indicates whether access to instance tags from the instance metadata is enabled or disabled. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html\">View tags for your EC2 instances using instance metadata</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    managed_by: NotRequired["aws_sdk_ec2.types.managed_by.ManagedBy"]
    """<p>The entity that manages the IMDS default settings. Possible values include:</p> <ul> <li> <p> <code>account</code> - The IMDS default settings are managed by the account.</p> </li> <li> <p> <code>declarative-policy</code> - The IMDS default settings are managed by a declarative policy and can't be modified by the account.</p> </li> </ul>"""
    managed_exception_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The customized exception message that is specified in the declarative policy.</p>"""
    http_tokens_enforced: NotRequired[
        "aws_sdk_ec2.types.http_tokens_enforced_state.HttpTokensEnforcedState"
    ]
    """<p>Indicates whether to enforce the requirement of IMDSv2 on an instance at the time of launch. When enforcement is enabled, the instance can't launch unless IMDSv2 (<code>HttpTokens</code>) is set to <code>required</code>.</p>"""
