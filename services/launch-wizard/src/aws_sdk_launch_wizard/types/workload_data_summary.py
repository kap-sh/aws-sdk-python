"""Generated from Smithy shape ``com.amazonaws.launchwizard#WorkloadDataSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.workload_name
    import aws_sdk_launch_wizard.types.workload_status


class WorkloadDataSummary(TypedDict):
    workload_name: NotRequired["aws_sdk_launch_wizard.types.workload_name.WorkloadName"]
    """<p>The name of the workload.</p>"""
    display_name: NotRequired["str"]
    """<p>The display name of the workload data.</p>"""
    status: NotRequired["aws_sdk_launch_wizard.types.workload_status.WorkloadStatus"]
    """<p>The status of the workload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadDataSummary) -> dict:
    out: dict = {}
    if "workload_name" in value:
        out["workloadName"] = value["workload_name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import aws_sdk_launch_wizard.types.workload_status

        out["status"] = aws_sdk_launch_wizard.types.workload_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> WorkloadDataSummary:
    out: WorkloadDataSummary = {}  # type: ignore[typeddict-item]
    if "workloadName" in data:
        out["workload_name"] = data["workloadName"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "status" in data:
        import aws_sdk_launch_wizard.types.workload_status

        out["status"] = aws_sdk_launch_wizard.types.workload_status.deserialize_json(
            data["status"]
        )
    return out
