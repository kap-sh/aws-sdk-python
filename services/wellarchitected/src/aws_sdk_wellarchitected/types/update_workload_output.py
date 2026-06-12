"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateWorkloadOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.workload


class UpdateWorkloadOutput(TypedDict):
    workload: NotRequired["aws_sdk_wellarchitected.types.workload.Workload"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkloadOutput) -> dict:
    out: dict = {}
    if "workload" in value:
        import aws_sdk_wellarchitected.types.workload

        out["Workload"] = aws_sdk_wellarchitected.types.workload.serialize_json(
            value["workload"]
        )
    return out


def deserialize_json(data: dict) -> UpdateWorkloadOutput:
    out: UpdateWorkloadOutput = {}  # type: ignore[typeddict-item]
    if "Workload" in data:
        import aws_sdk_wellarchitected.types.workload

        out["workload"] = aws_sdk_wellarchitected.types.workload.deserialize_json(
            data["Workload"]
        )
    return out
