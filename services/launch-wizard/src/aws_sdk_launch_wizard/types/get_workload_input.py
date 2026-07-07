"""Generated from Smithy shape ``com.amazonaws.launchwizard#GetWorkloadInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_launch_wizard.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.workload_name


class GetWorkloadInput(TypedDict, closed=True):
    workload_name: "aws_sdk_launch_wizard.types.workload_name.WorkloadName"
    """<p>The name of the workload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkloadInput) -> dict:
    out: dict = {}
    out["workloadName"] = value["workload_name"]
    return out


def deserialize_json(data: dict) -> GetWorkloadInput:
    out: GetWorkloadInput = {}  # type: ignore[typeddict-item]
    if "workloadName" in data:
        out["workload_name"] = data["workloadName"]
    else:
        raise DeserializationError("GetWorkloadInput.workload_name required")
    return out
