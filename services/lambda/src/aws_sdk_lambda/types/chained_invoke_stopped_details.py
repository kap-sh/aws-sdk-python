"""Generated from Smithy shape ``com.amazonaws.lambda#ChainedInvokeStoppedDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.event_error


class ChainedInvokeStoppedDetails(TypedDict):
    error: "aws_sdk_lambda.types.event_error.EventError"
    """<p>Details about why the chained invocation stopped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChainedInvokeStoppedDetails) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.event_error

    out["Error"] = aws_sdk_lambda.types.event_error.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> ChainedInvokeStoppedDetails:
    out: ChainedInvokeStoppedDetails = {}  # type: ignore[typeddict-item]
    if "Error" in data:
        import aws_sdk_lambda.types.event_error

        out["error"] = aws_sdk_lambda.types.event_error.deserialize_json(data["Error"])
    else:
        raise DeserializationError("ChainedInvokeStoppedDetails.error required")
    return out
