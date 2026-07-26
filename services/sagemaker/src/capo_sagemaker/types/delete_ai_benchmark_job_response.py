"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteAIBenchmarkJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_benchmark_job_arn


class DeleteAIBenchmarkJobResponse(TypedDict, closed=True):
    ai_benchmark_job_arn: NotRequired[
        "capo_sagemaker.types.ai_benchmark_job_arn.AIBenchmarkJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the deleted benchmark job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAIBenchmarkJobResponse) -> dict:
    out: dict = {}
    if "ai_benchmark_job_arn" in value:
        out["AIBenchmarkJobArn"] = value["ai_benchmark_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAIBenchmarkJobResponse:
    out: DeleteAIBenchmarkJobResponse = {}  # type: ignore[typeddict-item]
    if "AIBenchmarkJobArn" in data:
        out["ai_benchmark_job_arn"] = data["AIBenchmarkJobArn"]
    return out
