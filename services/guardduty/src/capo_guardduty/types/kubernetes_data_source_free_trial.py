"""Generated from Smithy shape ``com.amazonaws.guardduty#KubernetesDataSourceFreeTrial``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.data_source_free_trial


class KubernetesDataSourceFreeTrial(TypedDict, closed=True):
    audit_logs: NotRequired[
        "capo_guardduty.types.data_source_free_trial.DataSourceFreeTrial"
    ]
    """<p>Describes whether Kubernetes audit logs are enabled as a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesDataSourceFreeTrial) -> dict:
    out: dict = {}
    if "audit_logs" in value:
        import capo_guardduty.types.data_source_free_trial

        out["auditLogs"] = capo_guardduty.types.data_source_free_trial.serialize_json(
            value["audit_logs"]
        )
    return out


def deserialize_json(data: dict) -> KubernetesDataSourceFreeTrial:
    out: KubernetesDataSourceFreeTrial = {}  # type: ignore[typeddict-item]
    if "auditLogs" in data:
        import capo_guardduty.types.data_source_free_trial

        out["audit_logs"] = (
            capo_guardduty.types.data_source_free_trial.deserialize_json(
                data["auditLogs"]
            )
        )
    return out
