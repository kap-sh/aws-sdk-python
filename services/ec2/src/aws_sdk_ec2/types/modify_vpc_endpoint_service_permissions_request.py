"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcEndpointServicePermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.value_string_list
    import aws_sdk_ec2.types.vpc_endpoint_service_id


class ModifyVpcEndpointServicePermissionsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    service_id: NotRequired[
        "aws_sdk_ec2.types.vpc_endpoint_service_id.VpcEndpointServiceId"
    ]
    """<p>The ID of the service.</p>"""
    add_allowed_principals: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARN) of the principals. Permissions are granted to the principals in this list. To grant permissions to all principals, specify an asterisk (*).</p>"""
    remove_allowed_principals: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARN) of the principals. Permissions are revoked for principals in this list.</p>"""
