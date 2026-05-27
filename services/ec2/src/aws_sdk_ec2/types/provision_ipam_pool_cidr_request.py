"""Generated from Smithy shape ``com.amazonaws.ec2#ProvisionIpamPoolCidrRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ipam_cidr_authorization_context
    import aws_sdk_ec2.types.ipam_external_resource_verification_token_id
    import aws_sdk_ec2.types.ipam_pool_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verification_method


class ProvisionIpamPoolCidrRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the IPAM pool to which you want to assign a CIDR.</p>"""
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR you want to assign to the IPAM pool. Either \"NetmaskLength\" or \"Cidr\" is required. This value will be null if you specify \"NetmaskLength\" and will be filled in during the provisioning process.</p>"""
    cidr_authorization_context: NotRequired[
        "aws_sdk_ec2.types.ipam_cidr_authorization_context.IpamCidrAuthorizationContext"
    ]
    """<p>A signed document that proves that you are authorized to bring a specified IP address range to Amazon using BYOIP. This option only applies to IPv4 and IPv6 pools in the public scope.</p>"""
    netmask_length: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The netmask length of the CIDR you'd like to provision to a pool. Can be used for provisioning Amazon-provided IPv6 CIDRs to top-level pools and for provisioning CIDRs to pools with source pools. Cannot be used to provision BYOIP CIDRs to top-level pools. Either \"NetmaskLength\" or \"Cidr\" is required.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
    verification_method: NotRequired[
        "aws_sdk_ec2.types.verification_method.VerificationMethod"
    ]
    """<p>The method for verifying control of a public IP address range. Defaults to <code>remarks-x509</code> if not specified. This option only applies to IPv4 and IPv6 pools in the public scope.</p>"""
    ipam_external_resource_verification_token_id: NotRequired[
        "aws_sdk_ec2.types.ipam_external_resource_verification_token_id.IpamExternalResourceVerificationTokenId"
    ]
    """<p>Verification token ID. This option only applies to IPv4 and IPv6 pools in the public scope.</p>"""
