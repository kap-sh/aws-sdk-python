"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationKubernetesConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.organization_kubernetes_audit_logs_configuration


class OrganizationKubernetesConfiguration(TypedDict, closed=True):
    audit_logs: NotRequired[
        "capo_guardduty.types.organization_kubernetes_audit_logs_configuration.OrganizationKubernetesAuditLogsConfiguration"
    ]
    """<p>Whether Kubernetes audit logs data source should be auto-enabled for new members joining the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationKubernetesConfiguration) -> dict:
    out: dict = {}
    if "audit_logs" in value:
        import capo_guardduty.types.organization_kubernetes_audit_logs_configuration

        out["auditLogs"] = (
            capo_guardduty.types.organization_kubernetes_audit_logs_configuration.serialize_json(
                value["audit_logs"]
            )
        )
    return out


def deserialize_json(data: dict) -> OrganizationKubernetesConfiguration:
    out: OrganizationKubernetesConfiguration = {}  # type: ignore[typeddict-item]
    if "auditLogs" in data:
        import capo_guardduty.types.organization_kubernetes_audit_logs_configuration

        out["audit_logs"] = (
            capo_guardduty.types.organization_kubernetes_audit_logs_configuration.deserialize_json(
                data["auditLogs"]
            )
        )
    return out
