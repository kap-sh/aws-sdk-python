"""Generated from Smithy shape ``com.amazonaws.lambda#StopDurableExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.execution_timestamp


class StopDurableExecutionResponse(TypedDict, closed=True):
    stop_timestamp: "aws_sdk_lambda.types.execution_timestamp.ExecutionTimestamp"
    """<p>The timestamp when the execution was stopped (ISO 8601 format).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopDurableExecutionResponse) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.execution_timestamp

    out["StopTimestamp"] = aws_sdk_lambda.types.execution_timestamp.serialize_json(
        value["stop_timestamp"]
    )
    return out


def deserialize_json(data: dict) -> StopDurableExecutionResponse:
    out: StopDurableExecutionResponse = {}  # type: ignore[typeddict-item]
    if "StopTimestamp" in data:
        import aws_sdk_lambda.types.execution_timestamp

        out["stop_timestamp"] = (
            aws_sdk_lambda.types.execution_timestamp.deserialize_json(
                data["StopTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "StopDurableExecutionResponse.stop_timestamp required"
        )
    return out
