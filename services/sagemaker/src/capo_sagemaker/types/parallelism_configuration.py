"""Generated from Smithy shape ``com.amazonaws.sagemaker#ParallelismConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.max_parallel_execution_steps


class ParallelismConfiguration(TypedDict, closed=True):
    max_parallel_execution_steps: NotRequired[
        "capo_sagemaker.types.max_parallel_execution_steps.MaxParallelExecutionSteps"
    ]
    """<p>The max number of steps that can be executed in parallel. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParallelismConfiguration) -> dict:
    out: dict = {}
    if "max_parallel_execution_steps" in value:
        out["MaxParallelExecutionSteps"] = value["max_parallel_execution_steps"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParallelismConfiguration:
    out: ParallelismConfiguration = {}  # type: ignore[typeddict-item]
    if "MaxParallelExecutionSteps" in data:
        out["max_parallel_execution_steps"] = data["MaxParallelExecutionSteps"]
    return out
