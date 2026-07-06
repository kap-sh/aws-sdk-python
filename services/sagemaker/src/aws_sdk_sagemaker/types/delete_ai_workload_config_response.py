"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteAIWorkloadConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_workload_config_arn


class DeleteAIWorkloadConfigResponse(TypedDict, closed=True):
    ai_workload_config_arn: NotRequired[
        "aws_sdk_sagemaker.types.ai_workload_config_arn.AIWorkloadConfigArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the deleted AI workload configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAIWorkloadConfigResponse) -> dict:
    out: dict = {}
    if "ai_workload_config_arn" in value:
        out["AIWorkloadConfigArn"] = value["ai_workload_config_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAIWorkloadConfigResponse:
    out: DeleteAIWorkloadConfigResponse = {}  # type: ignore[typeddict-item]
    if "AIWorkloadConfigArn" in data:
        out["ai_workload_config_arn"] = data["AIWorkloadConfigArn"]
    return out
