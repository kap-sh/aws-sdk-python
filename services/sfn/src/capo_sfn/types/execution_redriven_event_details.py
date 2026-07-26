"""Generated from Smithy shape ``com.amazonaws.sfn#ExecutionRedrivenEventDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.redrive_count


class ExecutionRedrivenEventDetails(TypedDict, closed=True):
    redrive_count: NotRequired["capo_sfn.types.redrive_count.RedriveCount"]
    """<p>The number of times you've redriven an execution. If you have not yet redriven an execution, the <code>redriveCount</code> is 0. This count is not updated for redrives that failed to start or are pending to be redriven.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionRedrivenEventDetails) -> dict:
    out: dict = {}
    if "redrive_count" in value:
        out["redriveCount"] = value["redrive_count"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExecutionRedrivenEventDetails:
    out: ExecutionRedrivenEventDetails = {}  # type: ignore[typeddict-item]
    if "redriveCount" in data:
        out["redrive_count"] = data["redriveCount"]
    return out
