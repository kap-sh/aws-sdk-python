"""Generated from Smithy shape ``com.amazonaws.kafka#ClusterOperationStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.cluster_operation_step_info


class ClusterOperationStep(TypedDict, closed=True):
    step_info: NotRequired[
        "capo_kafka.types.cluster_operation_step_info.ClusterOperationStepInfo"
    ]
    """<p>Information about the step and its status.</p>"""
    step_name: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The name of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterOperationStep) -> dict:
    out: dict = {}
    if "step_info" in value:
        import capo_kafka.types.cluster_operation_step_info

        out["stepInfo"] = capo_kafka.types.cluster_operation_step_info.serialize_json(
            value["step_info"]
        )
    if "step_name" in value:
        out["stepName"] = value["step_name"]
    return out


def deserialize_json(data: dict) -> ClusterOperationStep:
    out: ClusterOperationStep = {}  # type: ignore[typeddict-item]
    if "stepInfo" in data:
        import capo_kafka.types.cluster_operation_step_info

        out["step_info"] = (
            capo_kafka.types.cluster_operation_step_info.deserialize_json(
                data["stepInfo"]
            )
        )
    if "stepName" in data:
        out["step_name"] = data["stepName"]
    return out
