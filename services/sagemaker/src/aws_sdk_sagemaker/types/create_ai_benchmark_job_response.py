"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateAIBenchmarkJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_benchmark_job_arn


class CreateAIBenchmarkJobResponse(TypedDict, closed=True):
    ai_benchmark_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.ai_benchmark_job_arn.AIBenchmarkJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the created benchmark job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAIBenchmarkJobResponse) -> dict:
    out: dict = {}
    if "ai_benchmark_job_arn" in value:
        out["AIBenchmarkJobArn"] = value["ai_benchmark_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAIBenchmarkJobResponse:
    out: CreateAIBenchmarkJobResponse = {}  # type: ignore[typeddict-item]
    if "AIBenchmarkJobArn" in data:
        out["ai_benchmark_job_arn"] = data["AIBenchmarkJobArn"]
    return out
