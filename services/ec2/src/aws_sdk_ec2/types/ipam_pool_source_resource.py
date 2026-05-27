"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolSourceResource``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool_source_resource_type
    import aws_sdk_ec2.types.string


class IpamPoolSourceResource(TypedDict):
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source resource ID.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.ipam_pool_source_resource_type.IpamPoolSourceResourceType"
    ]
    """<p>The source resource type.</p>"""
    resource_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source resource Region.</p>"""
    resource_owner: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source resource owner.</p>"""
