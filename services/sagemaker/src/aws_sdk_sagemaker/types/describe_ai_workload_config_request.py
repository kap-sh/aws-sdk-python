"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeAIWorkloadConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_entity_name


class DescribeAIWorkloadConfigRequest(TypedDict, closed=True):
    ai_workload_config_name: NotRequired[
        "aws_sdk_sagemaker.types.ai_entity_name.AIEntityName"
    ]
    """<p>The name of the AI workload configuration to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAIWorkloadConfigRequest) -> dict:
    out: dict = {}
    if "ai_workload_config_name" in value:
        out["AIWorkloadConfigName"] = value["ai_workload_config_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAIWorkloadConfigRequest:
    out: DescribeAIWorkloadConfigRequest = {}  # type: ignore[typeddict-item]
    if "AIWorkloadConfigName" in data:
        out["ai_workload_config_name"] = data["AIWorkloadConfigName"]
    return out
