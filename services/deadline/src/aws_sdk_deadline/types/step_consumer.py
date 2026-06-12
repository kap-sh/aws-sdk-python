"""Generated from Smithy shape ``com.amazonaws.deadline#StepConsumer``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.dependency_consumer_resolution_status
    import aws_sdk_deadline.types.step_id


class StepConsumer(TypedDict):
    step_id: "aws_sdk_deadline.types.step_id.StepId"
    """<p>The step ID.</p>"""
    status: "aws_sdk_deadline.types.dependency_consumer_resolution_status.DependencyConsumerResolutionStatus"
    """<p>The step consumer status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepConsumer) -> dict:
    out: dict = {}
    out["stepId"] = value["step_id"]
    import aws_sdk_deadline.types.dependency_consumer_resolution_status

    out["status"] = (
        aws_sdk_deadline.types.dependency_consumer_resolution_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> StepConsumer:
    out: StepConsumer = {}  # type: ignore[typeddict-item]
    if "stepId" in data:
        out["step_id"] = data["stepId"]
    else:
        raise DeserializationError("StepConsumer.step_id required")
    if "status" in data:
        import aws_sdk_deadline.types.dependency_consumer_resolution_status

        out["status"] = (
            aws_sdk_deadline.types.dependency_consumer_resolution_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("StepConsumer.status required")
    return out
