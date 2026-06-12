"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsGuardDutyDetectorDataSourcesKubernetesDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_kubernetes_audit_logs_details


class AwsGuardDutyDetectorDataSourcesKubernetesDetails(TypedDict):
    audit_logs: NotRequired[
        "aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_kubernetes_audit_logs_details.AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetails"
    ]
    """<p> Describes whether Kubernetes audit logs are activated as a data source for the detector. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsGuardDutyDetectorDataSourcesKubernetesDetails) -> dict:
    out: dict = {}
    if "audit_logs" in value:
        import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_kubernetes_audit_logs_details

        out["AuditLogs"] = (
            aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_kubernetes_audit_logs_details.serialize_json(
                value["audit_logs"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsGuardDutyDetectorDataSourcesKubernetesDetails:
    out: AwsGuardDutyDetectorDataSourcesKubernetesDetails = {}  # type: ignore[typeddict-item]
    if "AuditLogs" in data:
        import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_kubernetes_audit_logs_details

        out["audit_logs"] = (
            aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_kubernetes_audit_logs_details.deserialize_json(
                data["AuditLogs"]
            )
        )
    return out
