"""Generated from Smithy shape ``com.amazonaws.kafka#ClusterOperationStepInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class ClusterOperationStepInfo(TypedDict):
    step_status: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The steps current status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterOperationStepInfo) -> dict:
    out: dict = {}
    if "step_status" in value:
        out["stepStatus"] = value["step_status"]
    return out


def deserialize_json(data: dict) -> ClusterOperationStepInfo:
    out: ClusterOperationStepInfo = {}  # type: ignore[typeddict-item]
    if "stepStatus" in data:
        out["step_status"] = data["stepStatus"]
    return out
