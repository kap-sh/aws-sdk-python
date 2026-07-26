"""Generated from Smithy shape ``com.amazonaws.launchwizard#WorkloadDataSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_launch_wizard.types.workload_name
    import capo_launch_wizard.types.workload_status


class WorkloadDataSummary(TypedDict, closed=True):
    workload_name: NotRequired["capo_launch_wizard.types.workload_name.WorkloadName"]
    """<p>The name of the workload.</p>"""
    display_name: NotRequired["str"]
    """<p>The display name of the workload data.</p>"""
    status: NotRequired["capo_launch_wizard.types.workload_status.WorkloadStatus"]
    """<p>The status of the workload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadDataSummary) -> dict:
    out: dict = {}
    if "workload_name" in value:
        out["workloadName"] = value["workload_name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import capo_launch_wizard.types.workload_status

        out["status"] = capo_launch_wizard.types.workload_status.serialize_json(
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
        import capo_launch_wizard.types.workload_status

        out["status"] = capo_launch_wizard.types.workload_status.deserialize_json(
            data["status"]
        )
    return out
