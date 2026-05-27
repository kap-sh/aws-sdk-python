"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessTrustProvider``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.device_options
    import aws_sdk_ec2.types.device_trust_provider_type
    import aws_sdk_ec2.types.native_application_oidc_options
    import aws_sdk_ec2.types.oidc_options
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.trust_provider_type
    import aws_sdk_ec2.types.user_trust_provider_type
    import aws_sdk_ec2.types.verified_access_sse_specification_response


class VerifiedAccessTrustProvider(TypedDict):
    verified_access_trust_provider_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services Verified Access trust provider.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the Amazon Web Services Verified Access trust provider.</p>"""
    trust_provider_type: NotRequired[
        "aws_sdk_ec2.types.trust_provider_type.TrustProviderType"
    ]
    """<p>The type of Verified Access trust provider.</p>"""
    user_trust_provider_type: NotRequired[
        "aws_sdk_ec2.types.user_trust_provider_type.UserTrustProviderType"
    ]
    """<p>The type of user-based trust provider.</p>"""
    device_trust_provider_type: NotRequired[
        "aws_sdk_ec2.types.device_trust_provider_type.DeviceTrustProviderType"
    ]
    """<p>The type of device-based trust provider.</p>"""
    oidc_options: NotRequired["aws_sdk_ec2.types.oidc_options.OidcOptions"]
    """<p>The options for an OpenID Connect-compatible user-identity trust provider.</p>"""
    device_options: NotRequired["aws_sdk_ec2.types.device_options.DeviceOptions"]
    """<p>The options for device-identity trust provider.</p>"""
    policy_reference_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The identifier to be used when working with policy rules.</p>"""
    creation_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The creation time.</p>"""
    last_updated_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The last updated time.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""
    sse_specification: NotRequired[
        "aws_sdk_ec2.types.verified_access_sse_specification_response.VerifiedAccessSseSpecificationResponse"
    ]
    """<p>The options in use for server side encryption.</p>"""
    native_application_oidc_options: NotRequired[
        "aws_sdk_ec2.types.native_application_oidc_options.NativeApplicationOidcOptions"
    ]
    """<p>The OpenID Connect (OIDC) options.</p>"""
