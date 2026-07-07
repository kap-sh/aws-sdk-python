"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationDataSourceConfigurationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.organization_kubernetes_configuration_result
    import aws_sdk_guardduty.types.organization_malware_protection_configuration_result
    import aws_sdk_guardduty.types.organization_s3_logs_configuration_result


class OrganizationDataSourceConfigurationsResult(TypedDict, closed=True):
    s3_logs: NotRequired[
        "aws_sdk_guardduty.types.organization_s3_logs_configuration_result.OrganizationS3LogsConfigurationResult"
    ]
    """<p>Describes whether S3 data event logs are enabled as a data source.</p>"""
    kubernetes: NotRequired[
        "aws_sdk_guardduty.types.organization_kubernetes_configuration_result.OrganizationKubernetesConfigurationResult"
    ]
    """<p>Describes the configuration of Kubernetes data sources.</p>"""
    malware_protection: NotRequired[
        "aws_sdk_guardduty.types.organization_malware_protection_configuration_result.OrganizationMalwareProtectionConfigurationResult"
    ]
    """<p>Describes the configuration of Malware Protection data source for an organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationDataSourceConfigurationsResult) -> dict:
    out: dict = {}
    if "s3_logs" in value:
        import aws_sdk_guardduty.types.organization_s3_logs_configuration_result

        out["s3Logs"] = (
            aws_sdk_guardduty.types.organization_s3_logs_configuration_result.serialize_json(
                value["s3_logs"]
            )
        )
    if "kubernetes" in value:
        import aws_sdk_guardduty.types.organization_kubernetes_configuration_result

        out["kubernetes"] = (
            aws_sdk_guardduty.types.organization_kubernetes_configuration_result.serialize_json(
                value["kubernetes"]
            )
        )
    if "malware_protection" in value:
        import aws_sdk_guardduty.types.organization_malware_protection_configuration_result

        out["malwareProtection"] = (
            aws_sdk_guardduty.types.organization_malware_protection_configuration_result.serialize_json(
                value["malware_protection"]
            )
        )
    return out


def deserialize_json(data: dict) -> OrganizationDataSourceConfigurationsResult:
    out: OrganizationDataSourceConfigurationsResult = {}  # type: ignore[typeddict-item]
    if "s3Logs" in data:
        import aws_sdk_guardduty.types.organization_s3_logs_configuration_result

        out["s3_logs"] = (
            aws_sdk_guardduty.types.organization_s3_logs_configuration_result.deserialize_json(
                data["s3Logs"]
            )
        )
    if "kubernetes" in data:
        import aws_sdk_guardduty.types.organization_kubernetes_configuration_result

        out["kubernetes"] = (
            aws_sdk_guardduty.types.organization_kubernetes_configuration_result.deserialize_json(
                data["kubernetes"]
            )
        )
    if "malwareProtection" in data:
        import aws_sdk_guardduty.types.organization_malware_protection_configuration_result

        out["malware_protection"] = (
            aws_sdk_guardduty.types.organization_malware_protection_configuration_result.deserialize_json(
                data["malwareProtection"]
            )
        )
    return out
