"""Generated from Smithy shape ``com.amazonaws.sagemaker#DomainSettingsForUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.amazon_q_settings
    import aws_sdk_sagemaker.types.docker_settings
    import aws_sdk_sagemaker.types.domain_security_group_ids
    import aws_sdk_sagemaker.types.execution_role_identity_config
    import aws_sdk_sagemaker.types.ip_address_type
    import aws_sdk_sagemaker.types.r_studio_server_pro_domain_settings_for_update
    import aws_sdk_sagemaker.types.trusted_identity_propagation_settings
    import aws_sdk_sagemaker.types.unified_studio_settings


class DomainSettingsForUpdate(TypedDict):
    r_studio_server_pro_domain_settings_for_update: NotRequired[
        "aws_sdk_sagemaker.types.r_studio_server_pro_domain_settings_for_update.RStudioServerProDomainSettingsForUpdate"
    ]
    """<p>A collection of <code>RStudioServerPro</code> Domain-level app settings to update. A single <code>RStudioServerPro</code> application is created for a domain.</p>"""
    execution_role_identity_config: NotRequired[
        "aws_sdk_sagemaker.types.execution_role_identity_config.ExecutionRoleIdentityConfig"
    ]
    """<p>The configuration for attaching a SageMaker AI user profile name to the execution role as a <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html\">sts:SourceIdentity key</a>. This configuration can only be modified if there are no apps in the <code>InService</code> or <code>Pending</code> state.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_sagemaker.types.domain_security_group_ids.DomainSecurityGroupIds"
    ]
    """<p>The security groups for the Amazon Virtual Private Cloud that the <code>Domain</code> uses for communication between Domain-level apps and user apps.</p>"""
    trusted_identity_propagation_settings: NotRequired[
        "aws_sdk_sagemaker.types.trusted_identity_propagation_settings.TrustedIdentityPropagationSettings"
    ]
    """<p>The Trusted Identity Propagation (TIP) settings for the SageMaker domain. These settings determine how user identities from IAM Identity Center are propagated through the domain to TIP enabled Amazon Web Services services.</p>"""
    docker_settings: NotRequired[
        "aws_sdk_sagemaker.types.docker_settings.DockerSettings"
    ]
    """<p>A collection of settings that configure the domain's Docker interaction.</p>"""
    amazon_q_settings: NotRequired[
        "aws_sdk_sagemaker.types.amazon_q_settings.AmazonQSettings"
    ]
    """<p>A collection of settings that configure the Amazon Q experience within the domain.</p>"""
    unified_studio_settings: NotRequired[
        "aws_sdk_sagemaker.types.unified_studio_settings.UnifiedStudioSettings"
    ]
    """<p>The settings that apply to an SageMaker AI domain when you use it in Amazon SageMaker Unified Studio.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_sagemaker.types.ip_address_type.IPAddressType"
    ]
    """<p>The IP address type for the domain. Specify <code>ipv4</code> for IPv4-only connectivity or <code>dualstack</code> for both IPv4 and IPv6 connectivity. When you specify <code>dualstack</code>, the subnet must support IPv6 CIDR blocks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainSettingsForUpdate) -> dict:
    out: dict = {}
    if "r_studio_server_pro_domain_settings_for_update" in value:
        import aws_sdk_sagemaker.types.r_studio_server_pro_domain_settings_for_update

        out["RStudioServerProDomainSettingsForUpdate"] = (
            aws_sdk_sagemaker.types.r_studio_server_pro_domain_settings_for_update.serialize_aws_json_1_1(
                value["r_studio_server_pro_domain_settings_for_update"]
            )
        )
    if "execution_role_identity_config" in value:
        import aws_sdk_sagemaker.types.execution_role_identity_config

        out["ExecutionRoleIdentityConfig"] = (
            aws_sdk_sagemaker.types.execution_role_identity_config.serialize_aws_json_1_1(
                value["execution_role_identity_config"]
            )
        )
    if "security_group_ids" in value:
        import aws_sdk_sagemaker.types.domain_security_group_ids

        out["SecurityGroupIds"] = (
            aws_sdk_sagemaker.types.domain_security_group_ids.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    if "trusted_identity_propagation_settings" in value:
        import aws_sdk_sagemaker.types.trusted_identity_propagation_settings

        out["TrustedIdentityPropagationSettings"] = (
            aws_sdk_sagemaker.types.trusted_identity_propagation_settings.serialize_aws_json_1_1(
                value["trusted_identity_propagation_settings"]
            )
        )
    if "docker_settings" in value:
        import aws_sdk_sagemaker.types.docker_settings

        out["DockerSettings"] = (
            aws_sdk_sagemaker.types.docker_settings.serialize_aws_json_1_1(
                value["docker_settings"]
            )
        )
    if "amazon_q_settings" in value:
        import aws_sdk_sagemaker.types.amazon_q_settings

        out["AmazonQSettings"] = (
            aws_sdk_sagemaker.types.amazon_q_settings.serialize_aws_json_1_1(
                value["amazon_q_settings"]
            )
        )
    if "unified_studio_settings" in value:
        import aws_sdk_sagemaker.types.unified_studio_settings

        out["UnifiedStudioSettings"] = (
            aws_sdk_sagemaker.types.unified_studio_settings.serialize_aws_json_1_1(
                value["unified_studio_settings"]
            )
        )
    if "ip_address_type" in value:
        import aws_sdk_sagemaker.types.ip_address_type

        out["IpAddressType"] = (
            aws_sdk_sagemaker.types.ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DomainSettingsForUpdate:
    out: DomainSettingsForUpdate = {}  # type: ignore[typeddict-item]
    if "RStudioServerProDomainSettingsForUpdate" in data:
        import aws_sdk_sagemaker.types.r_studio_server_pro_domain_settings_for_update

        out["r_studio_server_pro_domain_settings_for_update"] = (
            aws_sdk_sagemaker.types.r_studio_server_pro_domain_settings_for_update.deserialize_aws_json_1_1(
                data["RStudioServerProDomainSettingsForUpdate"]
            )
        )
    if "ExecutionRoleIdentityConfig" in data:
        import aws_sdk_sagemaker.types.execution_role_identity_config

        out["execution_role_identity_config"] = (
            aws_sdk_sagemaker.types.execution_role_identity_config.deserialize_aws_json_1_1(
                data["ExecutionRoleIdentityConfig"]
            )
        )
    if "SecurityGroupIds" in data:
        import aws_sdk_sagemaker.types.domain_security_group_ids

        out["security_group_ids"] = (
            aws_sdk_sagemaker.types.domain_security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    if "TrustedIdentityPropagationSettings" in data:
        import aws_sdk_sagemaker.types.trusted_identity_propagation_settings

        out["trusted_identity_propagation_settings"] = (
            aws_sdk_sagemaker.types.trusted_identity_propagation_settings.deserialize_aws_json_1_1(
                data["TrustedIdentityPropagationSettings"]
            )
        )
    if "DockerSettings" in data:
        import aws_sdk_sagemaker.types.docker_settings

        out["docker_settings"] = (
            aws_sdk_sagemaker.types.docker_settings.deserialize_aws_json_1_1(
                data["DockerSettings"]
            )
        )
    if "AmazonQSettings" in data:
        import aws_sdk_sagemaker.types.amazon_q_settings

        out["amazon_q_settings"] = (
            aws_sdk_sagemaker.types.amazon_q_settings.deserialize_aws_json_1_1(
                data["AmazonQSettings"]
            )
        )
    if "UnifiedStudioSettings" in data:
        import aws_sdk_sagemaker.types.unified_studio_settings

        out["unified_studio_settings"] = (
            aws_sdk_sagemaker.types.unified_studio_settings.deserialize_aws_json_1_1(
                data["UnifiedStudioSettings"]
            )
        )
    if "IpAddressType" in data:
        import aws_sdk_sagemaker.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_sagemaker.types.ip_address_type.deserialize_aws_json_1_1(
                data["IpAddressType"]
            )
        )
    return out
