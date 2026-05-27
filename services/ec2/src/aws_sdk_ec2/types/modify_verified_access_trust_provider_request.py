"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessTrustProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.modify_verified_access_native_application_oidc_options
    import aws_sdk_ec2.types.modify_verified_access_trust_provider_device_options
    import aws_sdk_ec2.types.modify_verified_access_trust_provider_oidc_options
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_sse_specification_request
    import aws_sdk_ec2.types.verified_access_trust_provider_id


class ModifyVerifiedAccessTrustProviderRequest(TypedDict):
    verified_access_trust_provider_id: NotRequired[
        "aws_sdk_ec2.types.verified_access_trust_provider_id.VerifiedAccessTrustProviderId"
    ]
    """<p>The ID of the Verified Access trust provider.</p>"""
    oidc_options: NotRequired[
        "aws_sdk_ec2.types.modify_verified_access_trust_provider_oidc_options.ModifyVerifiedAccessTrustProviderOidcOptions"
    ]
    """<p>The options for an OpenID Connect-compatible user-identity trust provider.</p>"""
    device_options: NotRequired[
        "aws_sdk_ec2.types.modify_verified_access_trust_provider_device_options.ModifyVerifiedAccessTrustProviderDeviceOptions"
    ]
    """<p>The options for a device-based trust provider. This parameter is required when the provider type is <code>device</code>.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the Verified Access trust provider.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
    sse_specification: NotRequired[
        "aws_sdk_ec2.types.verified_access_sse_specification_request.VerifiedAccessSseSpecificationRequest"
    ]
    """<p>The options for server side encryption.</p>"""
    native_application_oidc_options: NotRequired[
        "aws_sdk_ec2.types.modify_verified_access_native_application_oidc_options.ModifyVerifiedAccessNativeApplicationOidcOptions"
    ]
    """<p>The OpenID Connect (OIDC) options.</p>"""
