"""Generated from Smithy shape ``com.amazonaws.lambda#WaitOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.duration_seconds


class WaitOptions(TypedDict, closed=True):
    wait_seconds: NotRequired["capo_lambda.types.duration_seconds.DurationSeconds"]
    """<p>The duration to wait, in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaitOptions) -> dict:
    out: dict = {}
    if "wait_seconds" in value:
        out["WaitSeconds"] = value["wait_seconds"]
    return out


def deserialize_json(data: dict) -> WaitOptions:
    out: WaitOptions = {}  # type: ignore[typeddict-item]
    if data.get("WaitSeconds") is not None:
        out["wait_seconds"] = data["WaitSeconds"]
    return out
