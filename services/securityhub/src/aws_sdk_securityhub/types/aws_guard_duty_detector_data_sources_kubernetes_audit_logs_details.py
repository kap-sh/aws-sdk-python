"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetails(TypedDict):
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Describes whether Kubernetes audit logs are activated as a data source for the detector. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetails,
) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(
    data: dict,
) -> AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetails:
    out: AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetails = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
