"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamScopeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.external_authority_configuration
    import aws_sdk_ec2.types.ipam_scope_id
    import aws_sdk_ec2.types.string


class ModifyIpamScopeRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_scope_id: NotRequired["aws_sdk_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The ID of the scope you want to modify.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the scope you want to modify.</p>"""
    external_authority_configuration: NotRequired[
        "aws_sdk_ec2.types.external_authority_configuration.ExternalAuthorityConfiguration"
    ]
    """<p>The configuration that links an Amazon VPC IPAM scope to an external authority system. It specifies the type of external system and the external resource identifier that identifies your account or instance in that system.</p> <p>In IPAM, an external authority is a third-party IP address management system that provides CIDR blocks when you provision address space for top-level IPAM pools. This allows you to use your existing IP management system to control which address ranges are allocated to Amazon Web Services while using Amazon VPC IPAM to manage subnets within those ranges.</p>"""
    remove_external_authority_configuration: NotRequired[
        "aws_sdk_ec2.types.boolean.Boolean"
    ]
    """<p>Remove the external authority configuration. <code>true</code> to remove.</p>"""
