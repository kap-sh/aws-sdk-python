"""Generated from Smithy shape ``com.amazonaws.lambda#ChainedInvokeFailedDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.event_error


class ChainedInvokeFailedDetails(TypedDict, closed=True):
    error: "capo_lambda.types.event_error.EventError"
    """<p>Details about the chained invocation failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChainedInvokeFailedDetails) -> dict:
    out: dict = {}
    import capo_lambda.types.event_error

    out["Error"] = capo_lambda.types.event_error.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> ChainedInvokeFailedDetails:
    out: ChainedInvokeFailedDetails = {}  # type: ignore[typeddict-item]
    if "Error" in data:
        import capo_lambda.types.event_error

        out["error"] = capo_lambda.types.event_error.deserialize_json(data["Error"])
    else:
        raise DeserializationError("ChainedInvokeFailedDetails.error required")
    return out
