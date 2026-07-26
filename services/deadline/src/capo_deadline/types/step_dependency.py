"""Generated from Smithy shape ``com.amazonaws.deadline#StepDependency``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.dependency_consumer_resolution_status
    import capo_deadline.types.step_id


class StepDependency(TypedDict, closed=True):
    step_id: "capo_deadline.types.step_id.StepId"
    """<p>The step ID.</p>"""
    status: "capo_deadline.types.dependency_consumer_resolution_status.DependencyConsumerResolutionStatus"
    """<p>The step dependency status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepDependency) -> dict:
    out: dict = {}
    out["stepId"] = value["step_id"]
    import capo_deadline.types.dependency_consumer_resolution_status

    out["status"] = (
        capo_deadline.types.dependency_consumer_resolution_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> StepDependency:
    out: StepDependency = {}  # type: ignore[typeddict-item]
    if "stepId" in data:
        out["step_id"] = data["stepId"]
    else:
        raise DeserializationError("StepDependency.step_id required")
    if "status" in data:
        import capo_deadline.types.dependency_consumer_resolution_status

        out["status"] = (
            capo_deadline.types.dependency_consumer_resolution_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("StepDependency.status required")
    return out
