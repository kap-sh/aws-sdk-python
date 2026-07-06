"""Generated from Smithy shape ``com.amazonaws.swf#ActivityTaskStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_swf.types.canceled


class ActivityTaskStatus(TypedDict, closed=True):
    cancel_requested: "aws_sdk_swf.types.canceled.Canceled"
    """<p>Set to <code>true</code> if cancellation of the task is requested.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityTaskStatus) -> dict:
    out: dict = {}
    out["cancelRequested"] = value.get("cancel_requested", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> ActivityTaskStatus:
    out: ActivityTaskStatus = {}  # type: ignore[typeddict-item]
    if "cancelRequested" in data:
        out["cancel_requested"] = data["cancelRequested"]
    else:
        out["cancel_requested"] = False
    return out
