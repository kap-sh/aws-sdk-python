"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#MemorySizeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.nullable_memory
    import aws_sdk_compute_optimizer.types.nullable_memory_reservation


class MemorySizeConfiguration(TypedDict):
    memory: NotRequired[
        "aws_sdk_compute_optimizer.types.nullable_memory.NullableMemory"
    ]
    """<p> The amount of memory in the container. </p>"""
    memory_reservation: NotRequired[
        "aws_sdk_compute_optimizer.types.nullable_memory_reservation.NullableMemoryReservation"
    ]
    """<p> The limit of memory reserve for the container. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MemorySizeConfiguration) -> dict:
    out: dict = {}
    if "memory" in value:
        out["memory"] = value["memory"]
    if "memory_reservation" in value:
        out["memoryReservation"] = value["memory_reservation"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MemorySizeConfiguration:
    out: MemorySizeConfiguration = {}  # type: ignore[typeddict-item]
    if "memory" in data:
        out["memory"] = data["memory"]
    if "memoryReservation" in data:
        out["memory_reservation"] = data["memoryReservation"]
    return out
