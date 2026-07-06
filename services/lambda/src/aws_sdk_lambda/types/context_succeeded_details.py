"""Generated from Smithy shape ``com.amazonaws.lambda#ContextSucceededDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.event_result


class ContextSucceededDetails(TypedDict, closed=True):
    result: "aws_sdk_lambda.types.event_result.EventResult"
    """<p>The JSON response payload from the successful context.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContextSucceededDetails) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.event_result

    out["Result"] = aws_sdk_lambda.types.event_result.serialize_json(value["result"])
    return out


def deserialize_json(data: dict) -> ContextSucceededDetails:
    out: ContextSucceededDetails = {}  # type: ignore[typeddict-item]
    if "Result" in data:
        import aws_sdk_lambda.types.event_result

        out["result"] = aws_sdk_lambda.types.event_result.deserialize_json(
            data["Result"]
        )
    else:
        raise DeserializationError("ContextSucceededDetails.result required")
    return out
