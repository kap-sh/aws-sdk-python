"""Generated from Smithy shape ``com.amazonaws.lambda#ExecutionSucceededDetails``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.event_result


class ExecutionSucceededDetails(TypedDict):
    result: "aws_sdk_lambda.types.event_result.EventResult"
    """<p>The response payload from the successful operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionSucceededDetails) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.event_result

    out["Result"] = aws_sdk_lambda.types.event_result.serialize_json(value["result"])
    return out


def deserialize_json(data: dict) -> ExecutionSucceededDetails:
    out: ExecutionSucceededDetails = {}  # type: ignore[typeddict-item]
    if "Result" in data:
        import aws_sdk_lambda.types.event_result

        out["result"] = aws_sdk_lambda.types.event_result.deserialize_json(
            data["Result"]
        )
    else:
        raise DeserializationError("ExecutionSucceededDetails.result required")
    return out
