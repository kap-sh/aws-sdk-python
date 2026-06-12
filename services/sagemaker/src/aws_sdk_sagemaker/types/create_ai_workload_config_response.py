"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateAIWorkloadConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_workload_config_arn


class CreateAIWorkloadConfigResponse(TypedDict):
    ai_workload_config_arn: NotRequired[
        "aws_sdk_sagemaker.types.ai_workload_config_arn.AIWorkloadConfigArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the created AI workload configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAIWorkloadConfigResponse) -> dict:
    out: dict = {}
    if "ai_workload_config_arn" in value:
        out["AIWorkloadConfigArn"] = value["ai_workload_config_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAIWorkloadConfigResponse:
    out: CreateAIWorkloadConfigResponse = {}  # type: ignore[typeddict-item]
    if "AIWorkloadConfigArn" in data:
        out["ai_workload_config_arn"] = data["AIWorkloadConfigArn"]
    return out
