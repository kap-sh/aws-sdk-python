"""Generated from Smithy shape ``com.amazonaws.sagemaker#StopAIBenchmarkJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_entity_name


class StopAIBenchmarkJobRequest(TypedDict, closed=True):
    ai_benchmark_job_name: NotRequired[
        "aws_sdk_sagemaker.types.ai_entity_name.AIEntityName"
    ]
    """<p>The name of the AI benchmark job to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopAIBenchmarkJobRequest) -> dict:
    out: dict = {}
    if "ai_benchmark_job_name" in value:
        out["AIBenchmarkJobName"] = value["ai_benchmark_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopAIBenchmarkJobRequest:
    out: StopAIBenchmarkJobRequest = {}  # type: ignore[typeddict-item]
    if "AIBenchmarkJobName" in data:
        out["ai_benchmark_job_name"] = data["AIBenchmarkJobName"]
    return out
