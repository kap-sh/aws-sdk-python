"""Generated from Smithy shape ``com.amazonaws.lambda#WaitCancelledDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.event_error


class WaitCancelledDetails(TypedDict, closed=True):
    error: NotRequired["aws_sdk_lambda.types.event_error.EventError"]
    """<p>Details about why the wait operation was cancelled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaitCancelledDetails) -> dict:
    out: dict = {}
    if "error" in value:
        import aws_sdk_lambda.types.event_error

        out["Error"] = aws_sdk_lambda.types.event_error.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> WaitCancelledDetails:
    out: WaitCancelledDetails = {}  # type: ignore[typeddict-item]
    if "Error" in data:
        import aws_sdk_lambda.types.event_error

        out["error"] = aws_sdk_lambda.types.event_error.deserialize_json(data["Error"])
    return out
