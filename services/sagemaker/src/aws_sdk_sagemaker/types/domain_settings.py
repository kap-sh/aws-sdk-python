"""Generated from Smithy shape ``com.amazonaws.sagemaker#DomainSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.amazon_q_settings
    import aws_sdk_sagemaker.types.docker_settings
    import aws_sdk_sagemaker.types.domain_security_group_ids
    import aws_sdk_sagemaker.types.execution_role_identity_config
    import aws_sdk_sagemaker.types.ip_address_type
    import aws_sdk_sagemaker.types.r_studio_server_pro_domain_settings
    import aws_sdk_sagemaker.types.trusted_identity_propagation_settings
    import aws_sdk_sagemaker.types.unified_studio_settings


class DomainSettings(TypedDict):
    security_group_ids: NotRequired[
        "aws_sdk_sagemaker.types.domain_security_group_ids.DomainSecurityGroupIds"
    ]
    """<p>The security groups for the Amazon Virtual Private Cloud that the <code>Domain</code> uses for communication between Domain-level apps and user apps.</p>"""
    r_studio_server_pro_domain_settings: NotRequired[
        "aws_sdk_sagemaker.types.r_studio_server_pro_domain_settings.RStudioServerProDomainSettings"
    ]
    """<p>A collection of settings that configure the <code>RStudioServerPro</code> Domain-level app.</p>"""
    execution_role_identity_config: NotRequired[
        "aws_sdk_sagemaker.types.execution_role_identity_config.ExecutionRoleIdentityConfig"
    ]
    """<p>The configuration for attaching a SageMaker AI user profile name to the execution role as a <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html\">sts:SourceIdentity key</a>.</p>"""
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
    """<p>A collection of settings that configure the Amazon Q experience within the domain. The <code>AuthMode</code> that you use to create the domain must be <code>SSO</code>.</p>"""
    unified_studio_settings: NotRequired[
        "aws_sdk_sagemaker.types.unified_studio_settings.UnifiedStudioSettings"
    ]
    """<p>The settings that apply to an SageMaker AI domain when you use it in Amazon SageMaker Unified Studio.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_sagemaker.types.ip_address_type.IPAddressType"
    ]
    """<p>The IP address type for the domain. Specify <code>ipv4</code> for IPv4-only connectivity or <code>dualstack</code> for both IPv4 and IPv6 connectivity. When you specify <code>dualstack</code>, the subnet must support IPv6 CIDR blocks. If not specified, defaults to <code>ipv4</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainSettings) -> dict:
    out: dict = {}
    if "security_group_ids" in value:
        import aws_sdk_sagemaker.types.domain_security_group_ids

        out["SecurityGroupIds"] = (
            aws_sdk_sagemaker.types.domain_security_group_ids.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    if "r_studio_server_pro_domain_settings" in value:
        import aws_sdk_sagemaker.types.r_studio_server_pro_domain_settings

        out["RStudioServerProDomainSettings"] = (
            aws_sdk_sagemaker.types.r_studio_server_pro_domain_settings.serialize_aws_json_1_1(
                value["r_studio_server_pro_domain_settings"]
            )
        )
    if "execution_role_identity_config" in value:
        import aws_sdk_sagemaker.types.execution_role_identity_config

        out["ExecutionRoleIdentityConfig"] = (
            aws_sdk_sagemaker.types.execution_role_identity_config.serialize_aws_json_1_1(
                value["execution_role_identity_config"]
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


def deserialize_aws_json_1_1(data: dict) -> DomainSettings:
    out: DomainSettings = {}  # type: ignore[typeddict-item]
    if "SecurityGroupIds" in data:
        import aws_sdk_sagemaker.types.domain_security_group_ids

        out["security_group_ids"] = (
            aws_sdk_sagemaker.types.domain_security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    if "RStudioServerProDomainSettings" in data:
        import aws_sdk_sagemaker.types.r_studio_server_pro_domain_settings

        out["r_studio_server_pro_domain_settings"] = (
            aws_sdk_sagemaker.types.r_studio_server_pro_domain_settings.deserialize_aws_json_1_1(
                data["RStudioServerProDomainSettings"]
            )
        )
    if "ExecutionRoleIdentityConfig" in data:
        import aws_sdk_sagemaker.types.execution_role_identity_config

        out["execution_role_identity_config"] = (
            aws_sdk_sagemaker.types.execution_role_identity_config.deserialize_aws_json_1_1(
                data["ExecutionRoleIdentityConfig"]
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
