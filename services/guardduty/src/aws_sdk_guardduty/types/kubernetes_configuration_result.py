"""Generated from Smithy shape ``com.amazonaws.guardduty#KubernetesConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.kubernetes_audit_logs_configuration_result


class KubernetesConfigurationResult(TypedDict, closed=True):
    audit_logs: NotRequired[
        "aws_sdk_guardduty.types.kubernetes_audit_logs_configuration_result.KubernetesAuditLogsConfigurationResult"
    ]
    """<p>Describes whether Kubernetes audit logs are enabled as a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesConfigurationResult) -> dict:
    out: dict = {}
    if "audit_logs" in value:
        import aws_sdk_guardduty.types.kubernetes_audit_logs_configuration_result

        out["auditLogs"] = (
            aws_sdk_guardduty.types.kubernetes_audit_logs_configuration_result.serialize_json(
                value["audit_logs"]
            )
        )
    return out


def deserialize_json(data: dict) -> KubernetesConfigurationResult:
    out: KubernetesConfigurationResult = {}  # type: ignore[typeddict-item]
    if "auditLogs" in data:
        import aws_sdk_guardduty.types.kubernetes_audit_logs_configuration_result

        out["audit_logs"] = (
            aws_sdk_guardduty.types.kubernetes_audit_logs_configuration_result.deserialize_json(
                data["auditLogs"]
            )
        )
    return out
