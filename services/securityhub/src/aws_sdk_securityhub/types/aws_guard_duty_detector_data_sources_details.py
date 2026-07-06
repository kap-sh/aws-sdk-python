"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsGuardDutyDetectorDataSourcesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_cloud_trail_details
    import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_dns_logs_details
    import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_flow_logs_details
    import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_kubernetes_details
    import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_malware_protection_details
    import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_s3_logs_details


class AwsGuardDutyDetectorDataSourcesDetails(TypedDict, closed=True):
    cloud_trail: NotRequired[
        "aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_cloud_trail_details.AwsGuardDutyDetectorDataSourcesCloudTrailDetails"
    ]
    """<p> An object that contains information on the status of CloudTrail as a data source for the detector. </p>"""
    dns_logs: NotRequired[
        "aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_dns_logs_details.AwsGuardDutyDetectorDataSourcesDnsLogsDetails"
    ]
    """<p> An object that contains information on the status of DNS logs as a data source for the detector. </p>"""
    flow_logs: NotRequired[
        "aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_flow_logs_details.AwsGuardDutyDetectorDataSourcesFlowLogsDetails"
    ]
    """<p> An object that contains information on the status of VPC Flow Logs as a data source for the detector. </p>"""
    kubernetes: NotRequired[
        "aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_kubernetes_details.AwsGuardDutyDetectorDataSourcesKubernetesDetails"
    ]
    """<p> An object that contains information on the status of Kubernetes data sources for the detector. </p>"""
    malware_protection: NotRequired[
        "aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_malware_protection_details.AwsGuardDutyDetectorDataSourcesMalwareProtectionDetails"
    ]
    """<p> An object that contains information on the status of Malware Protection as a data source for the detector. </p>"""
    s3_logs: NotRequired[
        "aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_s3_logs_details.AwsGuardDutyDetectorDataSourcesS3LogsDetails"
    ]
    """<p> An object that contains information on the status of S3 Data event logs as a data source for the detector. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsGuardDutyDetectorDataSourcesDetails) -> dict:
    out: dict = {}
    if "cloud_trail" in value:
        import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_cloud_trail_details

        out["CloudTrail"] = (
            aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_cloud_trail_details.serialize_json(
                value["cloud_trail"]
            )
        )
    if "dns_logs" in value:
        import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_dns_logs_details

        out["DnsLogs"] = (
            aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_dns_logs_details.serialize_json(
                value["dns_logs"]
            )
        )
    if "flow_logs" in value:
        import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_flow_logs_details

        out["FlowLogs"] = (
            aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_flow_logs_details.serialize_json(
                value["flow_logs"]
            )
        )
    if "kubernetes" in value:
        import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_kubernetes_details

        out["Kubernetes"] = (
            aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_kubernetes_details.serialize_json(
                value["kubernetes"]
            )
        )
    if "malware_protection" in value:
        import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_malware_protection_details

        out["MalwareProtection"] = (
            aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_malware_protection_details.serialize_json(
                value["malware_protection"]
            )
        )
    if "s3_logs" in value:
        import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_s3_logs_details

        out["S3Logs"] = (
            aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_s3_logs_details.serialize_json(
                value["s3_logs"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsGuardDutyDetectorDataSourcesDetails:
    out: AwsGuardDutyDetectorDataSourcesDetails = {}  # type: ignore[typeddict-item]
    if "CloudTrail" in data:
        import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_cloud_trail_details

        out["cloud_trail"] = (
            aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_cloud_trail_details.deserialize_json(
                data["CloudTrail"]
            )
        )
    if "DnsLogs" in data:
        import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_dns_logs_details

        out["dns_logs"] = (
            aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_dns_logs_details.deserialize_json(
                data["DnsLogs"]
            )
        )
    if "FlowLogs" in data:
        import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_flow_logs_details

        out["flow_logs"] = (
            aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_flow_logs_details.deserialize_json(
                data["FlowLogs"]
            )
        )
    if "Kubernetes" in data:
        import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_kubernetes_details

        out["kubernetes"] = (
            aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_kubernetes_details.deserialize_json(
                data["Kubernetes"]
            )
        )
    if "MalwareProtection" in data:
        import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_malware_protection_details

        out["malware_protection"] = (
            aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_malware_protection_details.deserialize_json(
                data["MalwareProtection"]
            )
        )
    if "S3Logs" in data:
        import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_s3_logs_details

        out["s3_logs"] = (
            aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_s3_logs_details.deserialize_json(
                data["S3Logs"]
            )
        )
    return out
