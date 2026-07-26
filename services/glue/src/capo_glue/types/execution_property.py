"""Generated from Smithy shape ``com.amazonaws.glue#ExecutionProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.max_concurrent_runs


class ExecutionProperty(TypedDict, closed=True):
    max_concurrent_runs: "capo_glue.types.max_concurrent_runs.MaxConcurrentRuns"
    """<p>The maximum number of concurrent runs allowed for the job. The default is 1. An error is returned when this threshold is reached. The maximum value you can specify is controlled by a service limit.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionProperty) -> dict:
    out: dict = {}
    out["MaxConcurrentRuns"] = value.get("max_concurrent_runs", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecutionProperty:
    out: ExecutionProperty = {}  # type: ignore[typeddict-item]
    if "MaxConcurrentRuns" in data:
        out["max_concurrent_runs"] = data["MaxConcurrentRuns"]
    else:
        out["max_concurrent_runs"] = 0
    return out
