"""Generated from Smithy shape ``com.amazonaws.guardduty#DataSourceConfigurationsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.cloud_trail_configuration_result
    import aws_sdk_guardduty.types.dns_logs_configuration_result
    import aws_sdk_guardduty.types.flow_logs_configuration_result
    import aws_sdk_guardduty.types.kubernetes_configuration_result
    import aws_sdk_guardduty.types.malware_protection_configuration_result
    import aws_sdk_guardduty.types.s3_logs_configuration_result


class DataSourceConfigurationsResult(TypedDict):
    cloud_trail: NotRequired[
        "aws_sdk_guardduty.types.cloud_trail_configuration_result.CloudTrailConfigurationResult"
    ]
    """<p>An object that contains information on the status of CloudTrail as a data source.</p>"""
    dns_logs: NotRequired[
        "aws_sdk_guardduty.types.dns_logs_configuration_result.DNSLogsConfigurationResult"
    ]
    """<p>An object that contains information on the status of DNS logs as a data source.</p>"""
    flow_logs: NotRequired[
        "aws_sdk_guardduty.types.flow_logs_configuration_result.FlowLogsConfigurationResult"
    ]
    """<p>An object that contains information on the status of VPC flow logs as a data source.</p>"""
    s3_logs: NotRequired[
        "aws_sdk_guardduty.types.s3_logs_configuration_result.S3LogsConfigurationResult"
    ]
    """<p>An object that contains information on the status of S3 Data event logs as a data source.</p>"""
    kubernetes: NotRequired[
        "aws_sdk_guardduty.types.kubernetes_configuration_result.KubernetesConfigurationResult"
    ]
    """<p>An object that contains information on the status of all Kubernetes data sources.</p>"""
    malware_protection: NotRequired[
        "aws_sdk_guardduty.types.malware_protection_configuration_result.MalwareProtectionConfigurationResult"
    ]
    """<p>Describes the configuration of Malware Protection data sources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceConfigurationsResult) -> dict:
    out: dict = {}
    if "cloud_trail" in value:
        import aws_sdk_guardduty.types.cloud_trail_configuration_result

        out["cloudTrail"] = (
            aws_sdk_guardduty.types.cloud_trail_configuration_result.serialize_json(
                value["cloud_trail"]
            )
        )
    if "dns_logs" in value:
        import aws_sdk_guardduty.types.dns_logs_configuration_result

        out["dnsLogs"] = (
            aws_sdk_guardduty.types.dns_logs_configuration_result.serialize_json(
                value["dns_logs"]
            )
        )
    if "flow_logs" in value:
        import aws_sdk_guardduty.types.flow_logs_configuration_result

        out["flowLogs"] = (
            aws_sdk_guardduty.types.flow_logs_configuration_result.serialize_json(
                value["flow_logs"]
            )
        )
    if "s3_logs" in value:
        import aws_sdk_guardduty.types.s3_logs_configuration_result

        out["s3Logs"] = (
            aws_sdk_guardduty.types.s3_logs_configuration_result.serialize_json(
                value["s3_logs"]
            )
        )
    if "kubernetes" in value:
        import aws_sdk_guardduty.types.kubernetes_configuration_result

        out["kubernetes"] = (
            aws_sdk_guardduty.types.kubernetes_configuration_result.serialize_json(
                value["kubernetes"]
            )
        )
    if "malware_protection" in value:
        import aws_sdk_guardduty.types.malware_protection_configuration_result

        out["malwareProtection"] = (
            aws_sdk_guardduty.types.malware_protection_configuration_result.serialize_json(
                value["malware_protection"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSourceConfigurationsResult:
    out: DataSourceConfigurationsResult = {}  # type: ignore[typeddict-item]
    if "cloudTrail" in data:
        import aws_sdk_guardduty.types.cloud_trail_configuration_result

        out["cloud_trail"] = (
            aws_sdk_guardduty.types.cloud_trail_configuration_result.deserialize_json(
                data["cloudTrail"]
            )
        )
    if "dnsLogs" in data:
        import aws_sdk_guardduty.types.dns_logs_configuration_result

        out["dns_logs"] = (
            aws_sdk_guardduty.types.dns_logs_configuration_result.deserialize_json(
                data["dnsLogs"]
            )
        )
    if "flowLogs" in data:
        import aws_sdk_guardduty.types.flow_logs_configuration_result

        out["flow_logs"] = (
            aws_sdk_guardduty.types.flow_logs_configuration_result.deserialize_json(
                data["flowLogs"]
            )
        )
    if "s3Logs" in data:
        import aws_sdk_guardduty.types.s3_logs_configuration_result

        out["s3_logs"] = (
            aws_sdk_guardduty.types.s3_logs_configuration_result.deserialize_json(
                data["s3Logs"]
            )
        )
    if "kubernetes" in data:
        import aws_sdk_guardduty.types.kubernetes_configuration_result

        out["kubernetes"] = (
            aws_sdk_guardduty.types.kubernetes_configuration_result.deserialize_json(
                data["kubernetes"]
            )
        )
    if "malwareProtection" in data:
        import aws_sdk_guardduty.types.malware_protection_configuration_result

        out["malware_protection"] = (
            aws_sdk_guardduty.types.malware_protection_configuration_result.deserialize_json(
                data["malwareProtection"]
            )
        )
    return out
