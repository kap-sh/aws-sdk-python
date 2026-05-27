"""Generated from Smithy shape ``com.amazonaws.ec2#IpamScope``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ipam_scope_external_authority_configuration
    import aws_sdk_ec2.types.ipam_scope_id
    import aws_sdk_ec2.types.ipam_scope_state
    import aws_sdk_ec2.types.ipam_scope_type
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class IpamScope(TypedDict):
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the scope.</p>"""
    ipam_scope_id: NotRequired["aws_sdk_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The ID of the scope.</p>"""
    ipam_scope_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the scope.</p>"""
    ipam_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the IPAM.</p>"""
    ipam_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services Region of the IPAM scope.</p>"""
    ipam_scope_type: NotRequired["aws_sdk_ec2.types.ipam_scope_type.IpamScopeType"]
    """<p>The type of the scope.</p>"""
    is_default: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Defines if the scope is the default scope or not.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the scope.</p>"""
    pool_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of pools in the scope.</p>"""
    state: NotRequired["aws_sdk_ec2.types.ipam_scope_state.IpamScopeState"]
    """<p>The state of the IPAM scope.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p>"""
    external_authority_configuration: NotRequired[
        "aws_sdk_ec2.types.ipam_scope_external_authority_configuration.IpamScopeExternalAuthorityConfiguration"
    ]
    """<p>The external authority configuration for this IPAM scope, if configured.</p> <p>The configuration that links an Amazon VPC IPAM scope to an external authority system. It specifies the type of external system and the external resource identifier that identifies your account or instance in that system.</p> <p>In IPAM, an external authority is a third-party IP address management system that provides CIDR blocks when you provision address space for top-level IPAM pools. This allows you to use your existing IP management system to control which address ranges are allocated to Amazon Web Services while using Amazon VPC IPAM to manage subnets within those ranges.</p>"""
