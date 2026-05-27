"""Generated from Smithy shape ``com.amazonaws.ec2#ExternalAuthorityConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_scope_external_authority_type
    import aws_sdk_ec2.types.string


class ExternalAuthorityConfiguration(TypedDict):
    type: NotRequired[
        "aws_sdk_ec2.types.ipam_scope_external_authority_type.IpamScopeExternalAuthorityType"
    ]
    """<p>The type of external authority.</p>"""
    external_resource_identifier: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The identifier for the external resource managing this scope. For Infoblox integrations, this is the Infoblox resource identifier in the format <code><version>.identity.account.<entity_realm>.<entity_id></code>.</p>"""
