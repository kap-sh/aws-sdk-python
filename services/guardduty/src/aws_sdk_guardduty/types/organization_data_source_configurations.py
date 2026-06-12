"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationDataSourceConfigurations``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.organization_kubernetes_configuration
    import aws_sdk_guardduty.types.organization_malware_protection_configuration
    import aws_sdk_guardduty.types.organization_s3_logs_configuration


class OrganizationDataSourceConfigurations(TypedDict):
    s3_logs: NotRequired[
        "aws_sdk_guardduty.types.organization_s3_logs_configuration.OrganizationS3LogsConfiguration"
    ]
    """<p>Describes whether S3 data event logs are enabled for new members of the organization.</p>"""
    kubernetes: NotRequired[
        "aws_sdk_guardduty.types.organization_kubernetes_configuration.OrganizationKubernetesConfiguration"
    ]
    """<p>Describes the configuration of Kubernetes data sources for new members of the organization.</p>"""
    malware_protection: NotRequired[
        "aws_sdk_guardduty.types.organization_malware_protection_configuration.OrganizationMalwareProtectionConfiguration"
    ]
    """<p>Describes the configuration of Malware Protection for new members of the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationDataSourceConfigurations) -> dict:
    out: dict = {}
    if "s3_logs" in value:
        import aws_sdk_guardduty.types.organization_s3_logs_configuration

        out["s3Logs"] = (
            aws_sdk_guardduty.types.organization_s3_logs_configuration.serialize_json(
                value["s3_logs"]
            )
        )
    if "kubernetes" in value:
        import aws_sdk_guardduty.types.organization_kubernetes_configuration

        out["kubernetes"] = (
            aws_sdk_guardduty.types.organization_kubernetes_configuration.serialize_json(
                value["kubernetes"]
            )
        )
    if "malware_protection" in value:
        import aws_sdk_guardduty.types.organization_malware_protection_configuration

        out["malwareProtection"] = (
            aws_sdk_guardduty.types.organization_malware_protection_configuration.serialize_json(
                value["malware_protection"]
            )
        )
    return out


def deserialize_json(data: dict) -> OrganizationDataSourceConfigurations:
    out: OrganizationDataSourceConfigurations = {}  # type: ignore[typeddict-item]
    if "s3Logs" in data:
        import aws_sdk_guardduty.types.organization_s3_logs_configuration

        out["s3_logs"] = (
            aws_sdk_guardduty.types.organization_s3_logs_configuration.deserialize_json(
                data["s3Logs"]
            )
        )
    if "kubernetes" in data:
        import aws_sdk_guardduty.types.organization_kubernetes_configuration

        out["kubernetes"] = (
            aws_sdk_guardduty.types.organization_kubernetes_configuration.deserialize_json(
                data["kubernetes"]
            )
        )
    if "malwareProtection" in data:
        import aws_sdk_guardduty.types.organization_malware_protection_configuration

        out["malware_protection"] = (
            aws_sdk_guardduty.types.organization_malware_protection_configuration.deserialize_json(
                data["malwareProtection"]
            )
        )
    return out
