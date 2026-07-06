"""Generated from Smithy shape ``com.amazonaws.guardduty#KubernetesConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.kubernetes_audit_logs_configuration


class KubernetesConfiguration(TypedDict, closed=True):
    audit_logs: NotRequired[
        "aws_sdk_guardduty.types.kubernetes_audit_logs_configuration.KubernetesAuditLogsConfiguration"
    ]
    """<p>The status of Kubernetes audit logs as a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesConfiguration) -> dict:
    out: dict = {}
    if "audit_logs" in value:
        import aws_sdk_guardduty.types.kubernetes_audit_logs_configuration

        out["auditLogs"] = (
            aws_sdk_guardduty.types.kubernetes_audit_logs_configuration.serialize_json(
                value["audit_logs"]
            )
        )
    return out


def deserialize_json(data: dict) -> KubernetesConfiguration:
    out: KubernetesConfiguration = {}  # type: ignore[typeddict-item]
    if "auditLogs" in data:
        import aws_sdk_guardduty.types.kubernetes_audit_logs_configuration

        out["audit_logs"] = (
            aws_sdk_guardduty.types.kubernetes_audit_logs_configuration.deserialize_json(
                data["auditLogs"]
            )
        )
    return out
