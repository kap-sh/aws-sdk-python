"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateClusterSchedulerConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_arn
    import aws_sdk_sagemaker.types.entity_description
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.scheduler_config
    import aws_sdk_sagemaker.types.tag_list


class CreateClusterSchedulerConfigRequest(TypedDict):
    name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>Name for the cluster policy.</p>"""
    cluster_arn: NotRequired["aws_sdk_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>ARN of the cluster.</p>"""
    scheduler_config: NotRequired[
        "aws_sdk_sagemaker.types.scheduler_config.SchedulerConfig"
    ]
    """<p>Configuration about the monitoring schedule.</p>"""
    description: NotRequired[
        "aws_sdk_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>Description of the cluster policy.</p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    """<p>Tags of the cluster policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateClusterSchedulerConfigRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "scheduler_config" in value:
        import aws_sdk_sagemaker.types.scheduler_config

        out["SchedulerConfig"] = (
            aws_sdk_sagemaker.types.scheduler_config.serialize_aws_json_1_1(
                value["scheduler_config"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateClusterSchedulerConfigRequest:
    out: CreateClusterSchedulerConfigRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    if "SchedulerConfig" in data:
        import aws_sdk_sagemaker.types.scheduler_config

        out["scheduler_config"] = (
            aws_sdk_sagemaker.types.scheduler_config.deserialize_aws_json_1_1(
                data["SchedulerConfig"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
