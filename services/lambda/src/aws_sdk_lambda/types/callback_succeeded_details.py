"""Generated from Smithy shape ``com.amazonaws.lambda#CallbackSucceededDetails``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.event_result


class CallbackSucceededDetails(TypedDict):
    result: "aws_sdk_lambda.types.event_result.EventResult"
    """<p>The response payload from the successful operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CallbackSucceededDetails) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.event_result

    out["Result"] = aws_sdk_lambda.types.event_result.serialize_json(value["result"])
    return out


def deserialize_json(data: dict) -> CallbackSucceededDetails:
    out: CallbackSucceededDetails = {}  # type: ignore[typeddict-item]
    if "Result" in data:
        import aws_sdk_lambda.types.event_result

        out["result"] = aws_sdk_lambda.types.event_result.deserialize_json(
            data["Result"]
        )
    else:
        raise DeserializationError("CallbackSucceededDetails.result required")
    return out
