"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeTrainingPlanResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.available_instance_count
    import aws_sdk_sagemaker.types.available_spare_instance_count
    import aws_sdk_sagemaker.types.currency_code
    import aws_sdk_sagemaker.types.in_use_instance_count
    import aws_sdk_sagemaker.types.reserved_capacity_summaries
    import aws_sdk_sagemaker.types.sage_maker_resource_names
    import aws_sdk_sagemaker.types.string256
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.total_instance_count
    import aws_sdk_sagemaker.types.training_plan_arn
    import aws_sdk_sagemaker.types.training_plan_duration_hours
    import aws_sdk_sagemaker.types.training_plan_duration_minutes
    import aws_sdk_sagemaker.types.training_plan_name
    import aws_sdk_sagemaker.types.training_plan_status
    import aws_sdk_sagemaker.types.training_plan_status_message
    import aws_sdk_sagemaker.types.ultra_server_count
    import aws_sdk_sagemaker.types.unhealthy_instance_count


class DescribeTrainingPlanResponse(TypedDict, closed=True):
    training_plan_arn: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_arn.TrainingPlanArn"
    ]
    """<p>The Amazon Resource Name (ARN); of the training plan.</p>"""
    training_plan_name: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_name.TrainingPlanName"
    ]
    """<p>The name of the training plan.</p>"""
    status: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_status.TrainingPlanStatus"
    ]
    r"""<p>The current status of the training plan (e.g., Pending, Active, Expired). To see the complete list of status values available for a training plan, refer to the <code>Status</code> attribute within the <code> <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingPlanSummary.html\">TrainingPlanSummary</a> </code> object.</p>"""
    status_message: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_status_message.TrainingPlanStatusMessage"
    ]
    """<p>A message providing additional information about the current status of the training plan.</p>"""
    duration_hours: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_duration_hours.TrainingPlanDurationHours"
    ]
    """<p>The number of whole hours in the total duration for this training plan.</p>"""
    duration_minutes: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_duration_minutes.TrainingPlanDurationMinutes"
    ]
    """<p>The additional minutes beyond whole hours in the total duration for this training plan.</p>"""
    start_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The start time of the training plan.</p>"""
    end_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The end time of the training plan.</p>"""
    upfront_fee: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The upfront fee for the training plan.</p>"""
    currency_code: NotRequired["aws_sdk_sagemaker.types.currency_code.CurrencyCode"]
    """<p>The currency code for the upfront fee (e.g., USD).</p>"""
    total_instance_count: NotRequired[
        "aws_sdk_sagemaker.types.total_instance_count.TotalInstanceCount"
    ]
    """<p>The total number of instances reserved in this training plan.</p>"""
    available_instance_count: NotRequired[
        "aws_sdk_sagemaker.types.available_instance_count.AvailableInstanceCount"
    ]
    """<p>The number of instances currently available for use in this training plan.</p>"""
    in_use_instance_count: NotRequired[
        "aws_sdk_sagemaker.types.in_use_instance_count.InUseInstanceCount"
    ]
    """<p>The number of instances currently in use from this training plan.</p>"""
    unhealthy_instance_count: NotRequired[
        "aws_sdk_sagemaker.types.unhealthy_instance_count.UnhealthyInstanceCount"
    ]
    """<p>The number of instances in the training plan that are currently in an unhealthy state.</p>"""
    available_spare_instance_count: NotRequired[
        "aws_sdk_sagemaker.types.available_spare_instance_count.AvailableSpareInstanceCount"
    ]
    """<p>The number of available spare instances in the training plan.</p>"""
    total_ultra_server_count: NotRequired[
        "aws_sdk_sagemaker.types.ultra_server_count.UltraServerCount"
    ]
    """<p>The total number of UltraServers reserved to this training plan.</p>"""
    target_resources: NotRequired[
        "aws_sdk_sagemaker.types.sage_maker_resource_names.SageMakerResourceNames"
    ]
    """<p>The target resources (e.g., SageMaker Training Jobs, SageMaker HyperPod, SageMaker Endpoints, Studio apps) that can use this training plan.</p> <p>Training plans are specific to their target resource.</p> <ul> <li> <p>A training plan designed for SageMaker training jobs can only be used to schedule and run training jobs.</p> </li> <li> <p>A training plan for HyperPod clusters can be used exclusively to provide compute resources to a cluster's instance group.</p> </li> <li> <p>A training plan for SageMaker endpoints can be used exclusively to provide compute resources to SageMaker endpoints for model deployment.</p> </li> <li> <p>A training plan for Studio apps can be used to launch JupyterLab and Code Editor apps on reserved training plan capacity.</p> </li> </ul>"""
    reserved_capacity_summaries: NotRequired[
        "aws_sdk_sagemaker.types.reserved_capacity_summaries.ReservedCapacitySummaries"
    ]
    """<p>The list of Reserved Capacity providing the underlying compute resources of the plan. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrainingPlanResponse) -> dict:
    out: dict = {}
    if "training_plan_arn" in value:
        out["TrainingPlanArn"] = value["training_plan_arn"]
    if "training_plan_name" in value:
        out["TrainingPlanName"] = value["training_plan_name"]
    if "status" in value:
        import aws_sdk_sagemaker.types.training_plan_status

        out["Status"] = (
            aws_sdk_sagemaker.types.training_plan_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "duration_hours" in value:
        out["DurationHours"] = value["duration_hours"]
    if "duration_minutes" in value:
        out["DurationMinutes"] = value["duration_minutes"]
    if "start_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["StartTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["EndTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "upfront_fee" in value:
        out["UpfrontFee"] = value["upfront_fee"]
    if "currency_code" in value:
        out["CurrencyCode"] = value["currency_code"]
    if "total_instance_count" in value:
        out["TotalInstanceCount"] = value["total_instance_count"]
    if "available_instance_count" in value:
        out["AvailableInstanceCount"] = value["available_instance_count"]
    if "in_use_instance_count" in value:
        out["InUseInstanceCount"] = value["in_use_instance_count"]
    if "unhealthy_instance_count" in value:
        out["UnhealthyInstanceCount"] = value["unhealthy_instance_count"]
    if "available_spare_instance_count" in value:
        out["AvailableSpareInstanceCount"] = value["available_spare_instance_count"]
    if "total_ultra_server_count" in value:
        out["TotalUltraServerCount"] = value["total_ultra_server_count"]
    if "target_resources" in value:
        import aws_sdk_sagemaker.types.sage_maker_resource_names

        out["TargetResources"] = (
            aws_sdk_sagemaker.types.sage_maker_resource_names.serialize_aws_json_1_1(
                value["target_resources"]
            )
        )
    if "reserved_capacity_summaries" in value:
        import aws_sdk_sagemaker.types.reserved_capacity_summaries

        out["ReservedCapacitySummaries"] = (
            aws_sdk_sagemaker.types.reserved_capacity_summaries.serialize_aws_json_1_1(
                value["reserved_capacity_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrainingPlanResponse:
    out: DescribeTrainingPlanResponse = {}  # type: ignore[typeddict-item]
    if "TrainingPlanArn" in data:
        out["training_plan_arn"] = data["TrainingPlanArn"]
    if "TrainingPlanName" in data:
        out["training_plan_name"] = data["TrainingPlanName"]
    if "Status" in data:
        import aws_sdk_sagemaker.types.training_plan_status

        out["status"] = (
            aws_sdk_sagemaker.types.training_plan_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "DurationHours" in data:
        out["duration_hours"] = data["DurationHours"]
    if "DurationMinutes" in data:
        out["duration_minutes"] = data["DurationMinutes"]
    if "StartTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["start_time"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["end_time"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "UpfrontFee" in data:
        out["upfront_fee"] = data["UpfrontFee"]
    if "CurrencyCode" in data:
        out["currency_code"] = data["CurrencyCode"]
    if "TotalInstanceCount" in data:
        out["total_instance_count"] = data["TotalInstanceCount"]
    if "AvailableInstanceCount" in data:
        out["available_instance_count"] = data["AvailableInstanceCount"]
    if "InUseInstanceCount" in data:
        out["in_use_instance_count"] = data["InUseInstanceCount"]
    if "UnhealthyInstanceCount" in data:
        out["unhealthy_instance_count"] = data["UnhealthyInstanceCount"]
    if "AvailableSpareInstanceCount" in data:
        out["available_spare_instance_count"] = data["AvailableSpareInstanceCount"]
    if "TotalUltraServerCount" in data:
        out["total_ultra_server_count"] = data["TotalUltraServerCount"]
    if "TargetResources" in data:
        import aws_sdk_sagemaker.types.sage_maker_resource_names

        out["target_resources"] = (
            aws_sdk_sagemaker.types.sage_maker_resource_names.deserialize_aws_json_1_1(
                data["TargetResources"]
            )
        )
    if "ReservedCapacitySummaries" in data:
        import aws_sdk_sagemaker.types.reserved_capacity_summaries

        out["reserved_capacity_summaries"] = (
            aws_sdk_sagemaker.types.reserved_capacity_summaries.deserialize_aws_json_1_1(
                data["ReservedCapacitySummaries"]
            )
        )
    return out
