"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcEndpointServicePayerResponsibilityRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.payer_responsibility
    import aws_sdk_ec2.types.vpc_endpoint_service_id


class ModifyVpcEndpointServicePayerResponsibilityRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    service_id: NotRequired[
        "aws_sdk_ec2.types.vpc_endpoint_service_id.VpcEndpointServiceId"
    ]
    """<p>The ID of the service.</p>"""
    payer_responsibility: NotRequired[
        "aws_sdk_ec2.types.payer_responsibility.PayerResponsibility"
    ]
    """<p>The entity that is responsible for the endpoint costs. The default is the endpoint owner. If you set the payer responsibility to the service owner, you cannot set it back to the endpoint owner.</p>"""
