"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsGuardDutyDetectorDataSourcesKubernetesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_guard_duty_detector_data_sources_kubernetes_audit_logs_details


class AwsGuardDutyDetectorDataSourcesKubernetesDetails(TypedDict, closed=True):
    audit_logs: NotRequired[
        "capo_securityhub.types.aws_guard_duty_detector_data_sources_kubernetes_audit_logs_details.AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetails"
    ]
    """<p> Describes whether Kubernetes audit logs are activated as a data source for the detector. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsGuardDutyDetectorDataSourcesKubernetesDetails) -> dict:
    out: dict = {}
    if "audit_logs" in value:
        import capo_securityhub.types.aws_guard_duty_detector_data_sources_kubernetes_audit_logs_details

        out["AuditLogs"] = (
            capo_securityhub.types.aws_guard_duty_detector_data_sources_kubernetes_audit_logs_details.serialize_json(
                value["audit_logs"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsGuardDutyDetectorDataSourcesKubernetesDetails:
    out: AwsGuardDutyDetectorDataSourcesKubernetesDetails = {}  # type: ignore[typeddict-item]
    if "AuditLogs" in data:
        import capo_securityhub.types.aws_guard_duty_detector_data_sources_kubernetes_audit_logs_details

        out["audit_logs"] = (
            capo_securityhub.types.aws_guard_duty_detector_data_sources_kubernetes_audit_logs_details.deserialize_json(
                data["AuditLogs"]
            )
        )
    return out
