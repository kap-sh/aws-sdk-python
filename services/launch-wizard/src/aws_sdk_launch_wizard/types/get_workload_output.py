"""Generated from Smithy shape ``com.amazonaws.launchwizard#GetWorkloadOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.workload_data


class GetWorkloadOutput(TypedDict, closed=True):
    workload: NotRequired["aws_sdk_launch_wizard.types.workload_data.WorkloadData"]
    """<p>Information about the workload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkloadOutput) -> dict:
    out: dict = {}
    if "workload" in value:
        import aws_sdk_launch_wizard.types.workload_data

        out["workload"] = aws_sdk_launch_wizard.types.workload_data.serialize_json(
            value["workload"]
        )
    return out


def deserialize_json(data: dict) -> GetWorkloadOutput:
    out: GetWorkloadOutput = {}  # type: ignore[typeddict-item]
    if "workload" in data:
        import aws_sdk_launch_wizard.types.workload_data

        out["workload"] = aws_sdk_launch_wizard.types.workload_data.deserialize_json(
            data["workload"]
        )
    return out
