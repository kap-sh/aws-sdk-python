"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationKubernetesConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.organization_kubernetes_audit_logs_configuration_result


class OrganizationKubernetesConfigurationResult(TypedDict, closed=True):
    audit_logs: NotRequired[
        "aws_sdk_guardduty.types.organization_kubernetes_audit_logs_configuration_result.OrganizationKubernetesAuditLogsConfigurationResult"
    ]
    """<p>The current configuration of Kubernetes audit logs as a data source for the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationKubernetesConfigurationResult) -> dict:
    out: dict = {}
    if "audit_logs" in value:
        import aws_sdk_guardduty.types.organization_kubernetes_audit_logs_configuration_result

        out["auditLogs"] = (
            aws_sdk_guardduty.types.organization_kubernetes_audit_logs_configuration_result.serialize_json(
                value["audit_logs"]
            )
        )
    return out


def deserialize_json(data: dict) -> OrganizationKubernetesConfigurationResult:
    out: OrganizationKubernetesConfigurationResult = {}  # type: ignore[typeddict-item]
    if "auditLogs" in data:
        import aws_sdk_guardduty.types.organization_kubernetes_audit_logs_configuration_result

        out["audit_logs"] = (
            aws_sdk_guardduty.types.organization_kubernetes_audit_logs_configuration_result.deserialize_json(
                data["auditLogs"]
            )
        )
    return out
