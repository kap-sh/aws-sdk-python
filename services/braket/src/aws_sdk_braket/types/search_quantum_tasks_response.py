"""Generated from Smithy shape ``com.amazonaws.braket#SearchQuantumTasksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.quantum_task_summary_list


class SearchQuantumTasksResponse(TypedDict, closed=True):
    quantum_tasks: (
        "aws_sdk_braket.types.quantum_task_summary_list.QuantumTaskSummaryList"
    )
    """<p>An array of <code>QuantumTaskSummary</code> objects for quantum tasks that match the specified filters.</p>"""
    next_token: NotRequired["str"]
    """<p>A token used for pagination of results, or null if there are no additional results. Use the token value in a subsequent request to continue search where the previous request ended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchQuantumTasksResponse) -> dict:
    out: dict = {}
    import aws_sdk_braket.types.quantum_task_summary_list

    out["quantumTasks"] = aws_sdk_braket.types.quantum_task_summary_list.serialize_json(
        value["quantum_tasks"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchQuantumTasksResponse:
    out: SearchQuantumTasksResponse = {}  # type: ignore[typeddict-item]
    if "quantumTasks" in data:
        import aws_sdk_braket.types.quantum_task_summary_list

        out["quantum_tasks"] = (
            aws_sdk_braket.types.quantum_task_summary_list.deserialize_json(
                data["quantumTasks"]
            )
        )
    else:
        raise DeserializationError("SearchQuantumTasksResponse.quantum_tasks required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
