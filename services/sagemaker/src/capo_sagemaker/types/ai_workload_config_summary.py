"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIWorkloadConfigSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_entity_name
    import capo_sagemaker.types.ai_workload_config_arn
    import capo_sagemaker.types.timestamp


class AIWorkloadConfigSummary(TypedDict, closed=True):
    ai_workload_config_name: NotRequired[
        "capo_sagemaker.types.ai_entity_name.AIEntityName"
    ]
    """<p>The name of the AI workload configuration.</p>"""
    ai_workload_config_arn: NotRequired[
        "capo_sagemaker.types.ai_workload_config_arn.AIWorkloadConfigArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the AI workload configuration.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the configuration was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIWorkloadConfigSummary) -> dict:
    out: dict = {}
    if "ai_workload_config_name" in value:
        out["AIWorkloadConfigName"] = value["ai_workload_config_name"]
    if "ai_workload_config_arn" in value:
        out["AIWorkloadConfigArn"] = value["ai_workload_config_arn"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AIWorkloadConfigSummary:
    out: AIWorkloadConfigSummary = {}  # type: ignore[typeddict-item]
    if "AIWorkloadConfigName" in data:
        out["ai_workload_config_name"] = data["AIWorkloadConfigName"]
    if "AIWorkloadConfigArn" in data:
        out["ai_workload_config_arn"] = data["AIWorkloadConfigArn"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out
