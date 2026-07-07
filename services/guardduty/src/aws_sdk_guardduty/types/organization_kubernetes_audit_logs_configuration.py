"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationKubernetesAuditLogsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.boolean


class OrganizationKubernetesAuditLogsConfiguration(TypedDict, closed=True):
    auto_enable: NotRequired["aws_sdk_guardduty.types.boolean.Boolean"]
    """<p>A value that contains information on whether Kubernetes audit logs should be enabled automatically as a data source for the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationKubernetesAuditLogsConfiguration) -> dict:
    out: dict = {}
    if "auto_enable" in value:
        out["autoEnable"] = value["auto_enable"]
    return out


def deserialize_json(data: dict) -> OrganizationKubernetesAuditLogsConfiguration:
    out: OrganizationKubernetesAuditLogsConfiguration = {}  # type: ignore[typeddict-item]
    if "autoEnable" in data:
        out["auto_enable"] = data["autoEnable"]
    return out
