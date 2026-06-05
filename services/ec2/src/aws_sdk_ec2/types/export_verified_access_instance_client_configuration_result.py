"""Generated from Smithy shape ``com.amazonaws.ec2#ExportVerifiedAccessInstanceClientConfigurationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ExportVerifiedAccessInstanceClientConfigurationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "version" in value:
        pairs.append((f"{prefix}.Version", str(value["version"])))
    if "verified_access_instance_id" in value:
        pairs.append(
            (
                f"{prefix}.VerifiedAccessInstanceId",
                str(value["verified_access_instance_id"]),
            )
        )
    if "region" in value:
        pairs.append((f"{prefix}.Region", str(value["region"])))
    if "device_trust_providers" in value:
        import aws_sdk_ec2.types.device_trust_provider_type_list

        aws_sdk_ec2.types.device_trust_provider_type_list.serialize_ec2_query(
            value["device_trust_providers"], pairs, f"{prefix}.DeviceTrustProviderSet"
        )
    if "user_trust_provider" in value:
        import aws_sdk_ec2.types.verified_access_instance_user_trust_provider_client_configuration

        aws_sdk_ec2.types.verified_access_instance_user_trust_provider_client_configuration.serialize_ec2_query(
            value["user_trust_provider"], pairs, f"{prefix}.UserTrustProvider"
        )
    if "open_vpn_configurations" in value:
        import aws_sdk_ec2.types.verified_access_instance_open_vpn_client_configuration_list

        aws_sdk_ec2.types.verified_access_instance_open_vpn_client_configuration_list.serialize_ec2_query(
            value["open_vpn_configurations"], pairs, f"{prefix}.OpenVpnConfigurationSet"
        )


def deserialize_ec2_query(
    el: Element,
) -> ExportVerifiedAccessInstanceClientConfigurationResult:
    out: ExportVerifiedAccessInstanceClientConfigurationResult = {}  # type: ignore[typeddict-item]
    child_version = el.find("Version")
    if child_version is not None:
        out["version"] = str(child_version.text or "")
    child_verified_access_instance_id = el.find("VerifiedAccessInstanceId")
    if child_verified_access_instance_id is not None:
        out["verified_access_instance_id"] = str(
            child_verified_access_instance_id.text or ""
        )
    child_region = el.find("Region")
    if child_region is not None:
        out["region"] = str(child_region.text or "")
    if el.find("DeviceTrustProviderSet") is not None:
        import aws_sdk_ec2.types.device_trust_provider_type_list

        out["device_trust_providers"] = (
            aws_sdk_ec2.types.device_trust_provider_type_list.deserialize_ec2_query(
                el, "DeviceTrustProviderSet"
            )
        )
    child_user_trust_provider = el.find("UserTrustProvider")
    if child_user_trust_provider is not None:
        import aws_sdk_ec2.types.verified_access_instance_user_trust_provider_client_configuration

        out["user_trust_provider"] = (
            aws_sdk_ec2.types.verified_access_instance_user_trust_provider_client_configuration.deserialize_ec2_query(
                child_user_trust_provider
            )
        )
    if el.find("OpenVpnConfigurationSet") is not None:
        import aws_sdk_ec2.types.verified_access_instance_open_vpn_client_configuration_list

        out["open_vpn_configurations"] = (
            aws_sdk_ec2.types.verified_access_instance_open_vpn_client_configuration_list.deserialize_ec2_query(
                el, "OpenVpnConfigurationSet"
            )
        )
    return out
