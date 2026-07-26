"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetWorkloadInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.workload_id


class GetWorkloadInput(TypedDict, closed=True):
    workload_id: "capo_wellarchitected.types.workload_id.WorkloadId"


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkloadInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWorkloadInput:
    out: GetWorkloadInput = {}  # type: ignore[typeddict-item]
    return out
