"""Generated from Smithy shape ``com.amazonaws.guardduty#KubernetesAuditLogsConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.data_source_status


class KubernetesAuditLogsConfigurationResult(TypedDict, closed=True):
    status: NotRequired["aws_sdk_guardduty.types.data_source_status.DataSourceStatus"]
    """<p>A value that describes whether Kubernetes audit logs are enabled as a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesAuditLogsConfigurationResult) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_guardduty.types.data_source_status

        out["status"] = aws_sdk_guardduty.types.data_source_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> KubernetesAuditLogsConfigurationResult:
    out: KubernetesAuditLogsConfigurationResult = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_guardduty.types.data_source_status

        out["status"] = aws_sdk_guardduty.types.data_source_status.deserialize_json(
            data["status"]
        )
    return out
