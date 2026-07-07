"""Generated from Smithy shape ``com.amazonaws.lambda#ChainedInvokeSucceededDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.event_result


class ChainedInvokeSucceededDetails(TypedDict, closed=True):
    result: "aws_sdk_lambda.types.event_result.EventResult"
    """<p>The response payload from the successful operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChainedInvokeSucceededDetails) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.event_result

    out["Result"] = aws_sdk_lambda.types.event_result.serialize_json(value["result"])
    return out


def deserialize_json(data: dict) -> ChainedInvokeSucceededDetails:
    out: ChainedInvokeSucceededDetails = {}  # type: ignore[typeddict-item]
    if "Result" in data:
        import aws_sdk_lambda.types.event_result

        out["result"] = aws_sdk_lambda.types.event_result.deserialize_json(
            data["Result"]
        )
    else:
        raise DeserializationError("ChainedInvokeSucceededDetails.result required")
    return out
