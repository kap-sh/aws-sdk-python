"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ConnectorOperationStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.connector_operation_step_state
    import capo_kafkaconnect.types.connector_operation_step_type


class ConnectorOperationStep(TypedDict, closed=True):
    step_type: NotRequired[
        "capo_kafkaconnect.types.connector_operation_step_type.ConnectorOperationStepType"
    ]
    """<p>The step type of the operation.</p>"""
    step_state: NotRequired[
        "capo_kafkaconnect.types.connector_operation_step_state.ConnectorOperationStepState"
    ]
    """<p>The step state of the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorOperationStep) -> dict:
    out: dict = {}
    if "step_type" in value:
        out["stepType"] = value["step_type"]
    if "step_state" in value:
        out["stepState"] = value["step_state"]
    return out


def deserialize_json(data: dict) -> ConnectorOperationStep:
    out: ConnectorOperationStep = {}  # type: ignore[typeddict-item]
    if "stepType" in data:
        out["step_type"] = data["stepType"]
    if "stepState" in data:
        out["step_state"] = data["stepState"]
    return out
