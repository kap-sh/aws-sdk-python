"""Generated from Smithy shape ``com.amazonaws.ec2#ExportVerifiedAccessInstanceClientConfigurationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.device_trust_provider_type_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_instance_open_vpn_client_configuration_list
    import aws_sdk_ec2.types.verified_access_instance_user_trust_provider_client_configuration


class ExportVerifiedAccessInstanceClientConfigurationResult(TypedDict):
    version: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The version.</p>"""
    verified_access_instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Verified Access instance.</p>"""
    region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region.</p>"""
    device_trust_providers: NotRequired[
        "aws_sdk_ec2.types.device_trust_provider_type_list.DeviceTrustProviderTypeList"
    ]
    """<p>The device trust providers.</p>"""
    user_trust_provider: NotRequired[
        "aws_sdk_ec2.types.verified_access_instance_user_trust_provider_client_configuration.VerifiedAccessInstanceUserTrustProviderClientConfiguration"
    ]
    """<p>The user identity trust provider.</p>"""
    open_vpn_configurations: NotRequired[
        "aws_sdk_ec2.types.verified_access_instance_open_vpn_client_configuration_list.VerifiedAccessInstanceOpenVpnClientConfigurationList"
    ]
    """<p>The Open VPN configuration.</p>"""
