"""Generated from Smithy shape ``com.amazonaws.sfn#ActivityStartedEventDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.identity


class ActivityStartedEventDetails(TypedDict, closed=True):
    worker_name: NotRequired["capo_sfn.types.identity.Identity"]
    """<p>The name of the worker that the task is assigned to. These names are provided by the workers when calling <a>GetActivityTask</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityStartedEventDetails) -> dict:
    out: dict = {}
    if "worker_name" in value:
        out["workerName"] = value["worker_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ActivityStartedEventDetails:
    out: ActivityStartedEventDetails = {}  # type: ignore[typeddict-item]
    if "workerName" in data:
        out["worker_name"] = data["workerName"]
    return out
