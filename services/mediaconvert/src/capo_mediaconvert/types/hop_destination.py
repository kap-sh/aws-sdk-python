"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HopDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer
    import capo_mediaconvert.types.__integer_min_negative50_max50
    import capo_mediaconvert.types.__string


class HopDestination(TypedDict, closed=True):
    priority: NotRequired[
        "capo_mediaconvert.types.__integer_min_negative50_max50.__integerMinNegative50Max50"
    ]
    """Optional. When you set up a job to use queue hopping, you can specify a different relative priority for the job in the destination queue. If you don't specify, the relative priority will remain the same as in the previous queue."""
    queue: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Optional unless the job is submitted on the default queue. When you set up a job to use queue hopping, you can specify a destination queue. This queue cannot be the original queue to which the job is submitted. If the original queue isn't the default queue and you don't specify the destination queue, the job will move to the default queue."""
    wait_minutes: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """Required for setting up a job to use queue hopping. Minimum wait time in minutes until the job can hop to the destination queue. Valid range is 1 to 4320 minutes, inclusive."""


# --- restJson1 ser/de ---
def serialize_json(value: HopDestination) -> dict:
    out: dict = {}
    if "priority" in value:
        out["priority"] = value["priority"]
    if "queue" in value:
        out["queue"] = value["queue"]
    if "wait_minutes" in value:
        out["waitMinutes"] = value["wait_minutes"]
    return out


def deserialize_json(data: dict) -> HopDestination:
    out: HopDestination = {}  # type: ignore[typeddict-item]
    if "priority" in data:
        out["priority"] = data["priority"]
    if "queue" in data:
        out["queue"] = data["queue"]
    if "waitMinutes" in data:
        out["wait_minutes"] = data["waitMinutes"]
    return out
