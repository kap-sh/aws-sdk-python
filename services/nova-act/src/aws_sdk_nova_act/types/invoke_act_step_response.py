"""Generated from Smithy shape ``com.amazonaws.novaact#InvokeActStepResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.calls
    import aws_sdk_nova_act.types.uuid_string


class InvokeActStepResponse(TypedDict, closed=True):
    calls: "aws_sdk_nova_act.types.calls.Calls"
    """<p>A list of tool calls that the act wants to execute in this step.</p>"""
    step_id: "aws_sdk_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier for this execution step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeActStepResponse) -> dict:
    out: dict = {}
    import aws_sdk_nova_act.types.calls

    out["calls"] = aws_sdk_nova_act.types.calls.serialize_json(value["calls"])
    out["stepId"] = value["step_id"]
    return out


def deserialize_json(data: dict) -> InvokeActStepResponse:
    out: InvokeActStepResponse = {}  # type: ignore[typeddict-item]
    if "calls" in data:
        import aws_sdk_nova_act.types.calls

        out["calls"] = aws_sdk_nova_act.types.calls.deserialize_json(data["calls"])
    else:
        raise DeserializationError("InvokeActStepResponse.calls required")
    if "stepId" in data:
        out["step_id"] = data["stepId"]
    else:
        raise DeserializationError("InvokeActStepResponse.step_id required")
    return out
