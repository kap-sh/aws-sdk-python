"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetWorkloadOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.workload


class GetWorkloadOutput(TypedDict, closed=True):
    workload: NotRequired["aws_sdk_wellarchitected.types.workload.Workload"]


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkloadOutput) -> dict:
    out: dict = {}
    if "workload" in value:
        import aws_sdk_wellarchitected.types.workload

        out["Workload"] = aws_sdk_wellarchitected.types.workload.serialize_json(
            value["workload"]
        )
    return out


def deserialize_json(data: dict) -> GetWorkloadOutput:
    out: GetWorkloadOutput = {}  # type: ignore[typeddict-item]
    if "Workload" in data:
        import aws_sdk_wellarchitected.types.workload

        out["workload"] = aws_sdk_wellarchitected.types.workload.deserialize_json(
            data["Workload"]
        )
    return out
