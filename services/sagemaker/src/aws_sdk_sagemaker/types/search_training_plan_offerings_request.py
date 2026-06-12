"""Generated from Smithy shape ``com.amazonaws.sagemaker#SearchTrainingPlanOfferingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.reserved_capacity_instance_count
    import aws_sdk_sagemaker.types.reserved_capacity_instance_type
    import aws_sdk_sagemaker.types.sage_maker_resource_names
    import aws_sdk_sagemaker.types.string
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.training_plan_duration_hours_input
    import aws_sdk_sagemaker.types.ultra_server_count
    import aws_sdk_sagemaker.types.ultra_server_type


class SearchTrainingPlanOfferingsRequest(TypedDict):
    instance_type: NotRequired[
        "aws_sdk_sagemaker.types.reserved_capacity_instance_type.ReservedCapacityInstanceType"
    ]
    """<p>The type of instance you want to search for in the available training plan offerings. This field allows you to filter the search results based on the specific compute resources you require for your SageMaker training jobs or SageMaker HyperPod clusters. When searching for training plan offerings, specifying the instance type helps you find Reserved Instances that match your computational needs.</p>"""
    instance_count: NotRequired[
        "aws_sdk_sagemaker.types.reserved_capacity_instance_count.ReservedCapacityInstanceCount"
    ]
    """<p>The number of instances you want to reserve in the training plan offerings. This allows you to specify the quantity of compute resources needed for your SageMaker training jobs or SageMaker HyperPod clusters, helping you find reserved capacity offerings that match your requirements.</p>"""
    ultra_server_type: NotRequired[
        "aws_sdk_sagemaker.types.ultra_server_type.UltraServerType"
    ]
    """<p>The type of UltraServer to search for, such as ml.u-p6e-gb200x72.</p>"""
    ultra_server_count: NotRequired[
        "aws_sdk_sagemaker.types.ultra_server_count.UltraServerCount"
    ]
    """<p>The number of UltraServers to search for.</p>"""
    start_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter to search for training plan offerings with a start time after a specified date.</p>"""
    end_time_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter to search for reserved capacity offerings with an end time before a specified date.</p>"""
    duration_hours: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_duration_hours_input.TrainingPlanDurationHoursInput"
    ]
    """<p>The desired duration in hours for the training plan offerings.</p>"""
    target_resources: NotRequired[
        "aws_sdk_sagemaker.types.sage_maker_resource_names.SageMakerResourceNames"
    ]
    """<p>The target resources (e.g., SageMaker Training Jobs, SageMaker HyperPod, SageMaker Endpoints, Studio apps) to search for in the offerings.</p> <p>Training plans are specific to their target resource.</p> <ul> <li> <p>A training plan designed for SageMaker training jobs can only be used to schedule and run training jobs.</p> </li> <li> <p>A training plan for HyperPod clusters can be used exclusively to provide compute resources to a cluster's instance group.</p> </li> <li> <p>A training plan for SageMaker endpoints can be used exclusively to provide compute resources to SageMaker endpoints for model deployment.</p> </li> <li> <p>A training plan for Studio apps can be used to launch JupyterLab and Code Editor apps on reserved training plan capacity.</p> </li> </ul>"""
    training_plan_arn: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The Amazon Resource Name (ARN); of an existing training plan to search for extension offerings. When specified, the API returns extension offerings that can be used to extend the specified training plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchTrainingPlanOfferingsRequest) -> dict:
    out: dict = {}
    if "instance_type" in value:
        import aws_sdk_sagemaker.types.reserved_capacity_instance_type

        out["InstanceType"] = (
            aws_sdk_sagemaker.types.reserved_capacity_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "ultra_server_type" in value:
        out["UltraServerType"] = value["ultra_server_type"]
    if "ultra_server_count" in value:
        out["UltraServerCount"] = value["ultra_server_count"]
    if "start_time_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["StartTimeAfter"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["start_time_after"]
            )
        )
    if "end_time_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["EndTimeBefore"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time_before"]
        )
    if "duration_hours" in value:
        out["DurationHours"] = value["duration_hours"]
    if "target_resources" in value:
        import aws_sdk_sagemaker.types.sage_maker_resource_names

        out["TargetResources"] = (
            aws_sdk_sagemaker.types.sage_maker_resource_names.serialize_aws_json_1_1(
                value["target_resources"]
            )
        )
    if "training_plan_arn" in value:
        out["TrainingPlanArn"] = value["training_plan_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchTrainingPlanOfferingsRequest:
    out: SearchTrainingPlanOfferingsRequest = {}  # type: ignore[typeddict-item]
    if "InstanceType" in data:
        import aws_sdk_sagemaker.types.reserved_capacity_instance_type

        out["instance_type"] = (
            aws_sdk_sagemaker.types.reserved_capacity_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
    if "UltraServerType" in data:
        out["ultra_server_type"] = data["UltraServerType"]
    if "UltraServerCount" in data:
        out["ultra_server_count"] = data["UltraServerCount"]
    if "StartTimeAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["start_time_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["StartTimeAfter"]
            )
        )
    if "EndTimeBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["end_time_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["EndTimeBefore"]
            )
        )
    if "DurationHours" in data:
        out["duration_hours"] = data["DurationHours"]
    if "TargetResources" in data:
        import aws_sdk_sagemaker.types.sage_maker_resource_names

        out["target_resources"] = (
            aws_sdk_sagemaker.types.sage_maker_resource_names.deserialize_aws_json_1_1(
                data["TargetResources"]
            )
        )
    if "TrainingPlanArn" in data:
        out["training_plan_arn"] = data["TrainingPlanArn"]
    return out
