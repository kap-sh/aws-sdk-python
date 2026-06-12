"""Generated from Smithy shape ``com.amazonaws.batch#JobTimeout``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.integer


class JobTimeout(TypedDict):
    attempt_duration_seconds: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The job timeout time (in seconds) that's measured from the job attempt's <code>startedAt</code> timestamp. After this time passes, Batch terminates your jobs if they aren't finished. The minimum value for the timeout is 60 seconds.</p> <p>For array jobs, the timeout applies to the child jobs, not to the parent array job.</p> <p>For multi-node parallel (MNP) jobs, the timeout applies to the whole job, not to the individual nodes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobTimeout) -> dict:
    out: dict = {}
    if "attempt_duration_seconds" in value:
        out["attemptDurationSeconds"] = value["attempt_duration_seconds"]
    return out


def deserialize_json(data: dict) -> JobTimeout:
    out: JobTimeout = {}  # type: ignore[typeddict-item]
    if "attemptDurationSeconds" in data:
        out["attempt_duration_seconds"] = data["attemptDurationSeconds"]
    return out
