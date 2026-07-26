"""Generated from Smithy shape ``com.amazonaws.iot#DescribeJobExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.job_execution


class DescribeJobExecutionResponse(TypedDict, closed=True):
    execution: NotRequired["capo_iot.types.job_execution.JobExecution"]
    """<p>Information about the job execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobExecutionResponse) -> dict:
    out: dict = {}
    if "execution" in value:
        import capo_iot.types.job_execution

        out["execution"] = capo_iot.types.job_execution.serialize_json(
            value["execution"]
        )
    return out


def deserialize_json(data: dict) -> DescribeJobExecutionResponse:
    out: DescribeJobExecutionResponse = {}  # type: ignore[typeddict-item]
    if "execution" in data:
        import capo_iot.types.job_execution

        out["execution"] = capo_iot.types.job_execution.deserialize_json(
            data["execution"]
        )
    return out
