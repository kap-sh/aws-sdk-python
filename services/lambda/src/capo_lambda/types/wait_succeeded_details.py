"""Generated from Smithy shape ``com.amazonaws.lambda#WaitSucceededDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.duration_seconds


class WaitSucceededDetails(TypedDict, closed=True):
    duration: NotRequired["capo_lambda.types.duration_seconds.DurationSeconds"]
    """<p>The wait duration, in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaitSucceededDetails) -> dict:
    out: dict = {}
    if "duration" in value:
        out["Duration"] = value["duration"]
    return out


def deserialize_json(data: dict) -> WaitSucceededDetails:
    out: WaitSucceededDetails = {}  # type: ignore[typeddict-item]
    if "Duration" in data:
        out["duration"] = data["Duration"]
    return out
