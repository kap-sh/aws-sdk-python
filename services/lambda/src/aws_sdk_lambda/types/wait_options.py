"""Generated from Smithy shape ``com.amazonaws.lambda#WaitOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.duration_seconds


class WaitOptions(TypedDict):
    wait_seconds: NotRequired["aws_sdk_lambda.types.duration_seconds.DurationSeconds"]
    """<p>The duration to wait, in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaitOptions) -> dict:
    out: dict = {}
    if "wait_seconds" in value:
        out["WaitSeconds"] = value["wait_seconds"]
    return out


def deserialize_json(data: dict) -> WaitOptions:
    out: WaitOptions = {}  # type: ignore[typeddict-item]
    if "WaitSeconds" in data:
        out["wait_seconds"] = data["WaitSeconds"]
    return out
