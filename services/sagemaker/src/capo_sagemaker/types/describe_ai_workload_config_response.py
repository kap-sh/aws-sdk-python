"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeAIWorkloadConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_dataset_config
    import capo_sagemaker.types.ai_entity_name
    import capo_sagemaker.types.ai_workload_config_arn
    import capo_sagemaker.types.ai_workload_configs
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.timestamp


class DescribeAIWorkloadConfigResponse(TypedDict, closed=True):
    ai_workload_config_name: NotRequired[
        "capo_sagemaker.types.ai_entity_name.AIEntityName"
    ]
    """<p>The name of the AI workload configuration.</p>"""
    ai_workload_config_arn: NotRequired[
        "capo_sagemaker.types.ai_workload_config_arn.AIWorkloadConfigArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the AI workload configuration.</p>"""
    dataset_config: NotRequired[
        "capo_sagemaker.types.ai_dataset_config.AIDatasetConfig"
    ]
    """<p>The dataset configuration for the workload.</p>"""
    ai_workload_configs: NotRequired[
        "capo_sagemaker.types.ai_workload_configs.AIWorkloadConfigs"
    ]
    """<p>The benchmark tool configuration and workload specification.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>The tags associated with the AI workload configuration.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the AI workload configuration was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAIWorkloadConfigResponse) -> dict:
    out: dict = {}
    if "ai_workload_config_name" in value:
        out["AIWorkloadConfigName"] = value["ai_workload_config_name"]
    if "ai_workload_config_arn" in value:
        out["AIWorkloadConfigArn"] = value["ai_workload_config_arn"]
    if "dataset_config" in value:
        import capo_sagemaker.types.ai_dataset_config

        out["DatasetConfig"] = (
            capo_sagemaker.types.ai_dataset_config.serialize_aws_json_1_1(
                value["dataset_config"]
            )
        )
    if "ai_workload_configs" in value:
        import capo_sagemaker.types.ai_workload_configs

        out["AIWorkloadConfigs"] = (
            capo_sagemaker.types.ai_workload_configs.serialize_aws_json_1_1(
                value["ai_workload_configs"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAIWorkloadConfigResponse:
    out: DescribeAIWorkloadConfigResponse = {}  # type: ignore[typeddict-item]
    if "AIWorkloadConfigName" in data:
        out["ai_workload_config_name"] = data["AIWorkloadConfigName"]
    if "AIWorkloadConfigArn" in data:
        out["ai_workload_config_arn"] = data["AIWorkloadConfigArn"]
    if "DatasetConfig" in data:
        import capo_sagemaker.types.ai_dataset_config

        out["dataset_config"] = (
            capo_sagemaker.types.ai_dataset_config.deserialize_aws_json_1_1(
                data["DatasetConfig"]
            )
        )
    if "AIWorkloadConfigs" in data:
        import capo_sagemaker.types.ai_workload_configs

        out["ai_workload_configs"] = (
            capo_sagemaker.types.ai_workload_configs.deserialize_aws_json_1_1(
                data["AIWorkloadConfigs"]
            )
        )
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out
