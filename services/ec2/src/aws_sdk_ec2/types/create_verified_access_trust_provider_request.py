"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVerifiedAccessTrustProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.create_verified_access_native_application_oidc_options
    import aws_sdk_ec2.types.create_verified_access_trust_provider_device_options
    import aws_sdk_ec2.types.create_verified_access_trust_provider_oidc_options
    import aws_sdk_ec2.types.device_trust_provider_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.trust_provider_type
    import aws_sdk_ec2.types.user_trust_provider_type
    import aws_sdk_ec2.types.verified_access_sse_specification_request


class CreateVerifiedAccessTrustProviderRequest(TypedDict):
    trust_provider_type: NotRequired[
        "aws_sdk_ec2.types.trust_provider_type.TrustProviderType"
    ]
    """<p>The type of trust provider.</p>"""
    user_trust_provider_type: NotRequired[
        "aws_sdk_ec2.types.user_trust_provider_type.UserTrustProviderType"
    ]
    """<p>The type of user-based trust provider. This parameter is required when the provider type is <code>user</code>.</p>"""
    device_trust_provider_type: NotRequired[
        "aws_sdk_ec2.types.device_trust_provider_type.DeviceTrustProviderType"
    ]
    """<p>The type of device-based trust provider. This parameter is required when the provider type is <code>device</code>.</p>"""
    oidc_options: NotRequired[
        "aws_sdk_ec2.types.create_verified_access_trust_provider_oidc_options.CreateVerifiedAccessTrustProviderOidcOptions"
    ]
    """<p>The options for a OpenID Connect-compatible user-identity trust provider. This parameter is required when the provider type is <code>user</code>.</p>"""
    device_options: NotRequired[
        "aws_sdk_ec2.types.create_verified_access_trust_provider_device_options.CreateVerifiedAccessTrustProviderDeviceOptions"
    ]
    """<p>The options for a device-based trust provider. This parameter is required when the provider type is <code>device</code>.</p>"""
    policy_reference_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The identifier to be used when working with policy rules.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the Verified Access trust provider.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the Verified Access trust provider.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    sse_specification: NotRequired[
        "aws_sdk_ec2.types.verified_access_sse_specification_request.VerifiedAccessSseSpecificationRequest"
    ]
    """<p>The options for server side encryption.</p>"""
    native_application_oidc_options: NotRequired[
        "aws_sdk_ec2.types.create_verified_access_native_application_oidc_options.CreateVerifiedAccessNativeApplicationOidcOptions"
    ]
    """<p>The OpenID Connect (OIDC) options.</p>"""
