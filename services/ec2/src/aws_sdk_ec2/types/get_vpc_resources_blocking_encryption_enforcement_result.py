"""Generated from Smithy shape ``com.amazonaws.ec2#GetVpcResourcesBlockingEncryptionEnforcementResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_encryption_non_compliant_resource_list


class GetVpcResourcesBlockingEncryptionEnforcementResult(TypedDict):
    non_compliant_resources: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_non_compliant_resource_list.VpcEncryptionNonCompliantResourceList"
    ]
    """<p>Information about resources that are blocking encryption enforcement.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
