"""Generated from Smithy shape ``com.amazonaws.lambda#ExecutionStartedDetails``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.duration_seconds
    import aws_sdk_lambda.types.event_input


class ExecutionStartedDetails(TypedDict):
    input: "aws_sdk_lambda.types.event_input.EventInput"
    """<p>The input payload provided for the durable execution.</p>"""
    execution_timeout: "aws_sdk_lambda.types.duration_seconds.DurationSeconds"
    """<p>The maximum amount of time that the durable execution is allowed to run, in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionStartedDetails) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.event_input

    out["Input"] = aws_sdk_lambda.types.event_input.serialize_json(value["input"])
    out["ExecutionTimeout"] = value["execution_timeout"]
    return out


def deserialize_json(data: dict) -> ExecutionStartedDetails:
    out: ExecutionStartedDetails = {}  # type: ignore[typeddict-item]
    if "Input" in data:
        import aws_sdk_lambda.types.event_input

        out["input"] = aws_sdk_lambda.types.event_input.deserialize_json(data["Input"])
    else:
        raise DeserializationError("ExecutionStartedDetails.input required")
    if "ExecutionTimeout" in data:
        out["execution_timeout"] = data["ExecutionTimeout"]
    else:
        raise DeserializationError("ExecutionStartedDetails.execution_timeout required")
    return out
