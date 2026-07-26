"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeProcessingJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.app_specification
    import capo_sagemaker.types.auto_ml_job_arn
    import capo_sagemaker.types.exit_message
    import capo_sagemaker.types.experiment_config
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.monitoring_schedule_arn
    import capo_sagemaker.types.network_config
    import capo_sagemaker.types.processing_environment_map
    import capo_sagemaker.types.processing_inputs
    import capo_sagemaker.types.processing_job_arn
    import capo_sagemaker.types.processing_job_name
    import capo_sagemaker.types.processing_job_status
    import capo_sagemaker.types.processing_output_config
    import capo_sagemaker.types.processing_resources
    import capo_sagemaker.types.processing_stopping_condition
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.training_job_arn


class DescribeProcessingJobResponse(TypedDict, closed=True):
    processing_inputs: NotRequired[
        "capo_sagemaker.types.processing_inputs.ProcessingInputs"
    ]
    """<p>The inputs for a processing job.</p>"""
    processing_output_config: NotRequired[
        "capo_sagemaker.types.processing_output_config.ProcessingOutputConfig"
    ]
    """<p>Output configuration for the processing job.</p>"""
    processing_job_name: NotRequired[
        "capo_sagemaker.types.processing_job_name.ProcessingJobName"
    ]
    """<p>The name of the processing job. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.</p>"""
    processing_resources: NotRequired[
        "capo_sagemaker.types.processing_resources.ProcessingResources"
    ]
    """<p>Identifies the resources, ML compute instances, and ML storage volumes to deploy for a processing job. In distributed training, you specify more than one instance.</p>"""
    stopping_condition: NotRequired[
        "capo_sagemaker.types.processing_stopping_condition.ProcessingStoppingCondition"
    ]
    """<p>The time limit for how long the processing job is allowed to run.</p>"""
    app_specification: NotRequired[
        "capo_sagemaker.types.app_specification.AppSpecification"
    ]
    """<p>Configures the processing job to run a specified container image.</p>"""
    environment: NotRequired[
        "capo_sagemaker.types.processing_environment_map.ProcessingEnvironmentMap"
    ]
    """<p>The environment variables set in the Docker container.</p>"""
    network_config: NotRequired["capo_sagemaker.types.network_config.NetworkConfig"]
    """<p>Networking options for a processing job.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.</p>"""
    experiment_config: NotRequired[
        "capo_sagemaker.types.experiment_config.ExperimentConfig"
    ]
    """<p>The configuration information used to create an experiment.</p>"""
    processing_job_arn: NotRequired[
        "capo_sagemaker.types.processing_job_arn.ProcessingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the processing job.</p>"""
    processing_job_status: NotRequired[
        "capo_sagemaker.types.processing_job_status.ProcessingJobStatus"
    ]
    """<p>Provides the status of a processing job.</p>"""
    exit_message: NotRequired["capo_sagemaker.types.exit_message.ExitMessage"]
    """<p>An optional string, up to one KB in size, that contains metadata from the processing container when the processing job exits.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>A string, up to one KB in size, that contains the reason a processing job failed, if it failed.</p>"""
    processing_end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time at which the processing job completed.</p>"""
    processing_start_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time at which the processing job started.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time at which the processing job was last modified.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time at which the processing job was created.</p>"""
    monitoring_schedule_arn: NotRequired[
        "capo_sagemaker.types.monitoring_schedule_arn.MonitoringScheduleArn"
    ]
    """<p>The ARN of a monitoring schedule for an endpoint associated with this processing job.</p>"""
    auto_ml_job_arn: NotRequired["capo_sagemaker.types.auto_ml_job_arn.AutoMLJobArn"]
    """<p>The ARN of an AutoML job associated with this processing job.</p>"""
    training_job_arn: NotRequired[
        "capo_sagemaker.types.training_job_arn.TrainingJobArn"
    ]
    """<p>The ARN of a training job associated with this processing job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProcessingJobResponse) -> dict:
    out: dict = {}
    if "processing_inputs" in value:
        import capo_sagemaker.types.processing_inputs

        out["ProcessingInputs"] = (
            capo_sagemaker.types.processing_inputs.serialize_aws_json_1_1(
                value["processing_inputs"]
            )
        )
    if "processing_output_config" in value:
        import capo_sagemaker.types.processing_output_config

        out["ProcessingOutputConfig"] = (
            capo_sagemaker.types.processing_output_config.serialize_aws_json_1_1(
                value["processing_output_config"]
            )
        )
    if "processing_job_name" in value:
        out["ProcessingJobName"] = value["processing_job_name"]
    if "processing_resources" in value:
        import capo_sagemaker.types.processing_resources

        out["ProcessingResources"] = (
            capo_sagemaker.types.processing_resources.serialize_aws_json_1_1(
                value["processing_resources"]
            )
        )
    if "stopping_condition" in value:
        import capo_sagemaker.types.processing_stopping_condition

        out["StoppingCondition"] = (
            capo_sagemaker.types.processing_stopping_condition.serialize_aws_json_1_1(
                value["stopping_condition"]
            )
        )
    if "app_specification" in value:
        import capo_sagemaker.types.app_specification

        out["AppSpecification"] = (
            capo_sagemaker.types.app_specification.serialize_aws_json_1_1(
                value["app_specification"]
            )
        )
    if "environment" in value:
        import capo_sagemaker.types.processing_environment_map

        out["Environment"] = (
            capo_sagemaker.types.processing_environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "network_config" in value:
        import capo_sagemaker.types.network_config

        out["NetworkConfig"] = (
            capo_sagemaker.types.network_config.serialize_aws_json_1_1(
                value["network_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "experiment_config" in value:
        import capo_sagemaker.types.experiment_config

        out["ExperimentConfig"] = (
            capo_sagemaker.types.experiment_config.serialize_aws_json_1_1(
                value["experiment_config"]
            )
        )
    if "processing_job_arn" in value:
        out["ProcessingJobArn"] = value["processing_job_arn"]
    if "processing_job_status" in value:
        import capo_sagemaker.types.processing_job_status

        out["ProcessingJobStatus"] = (
            capo_sagemaker.types.processing_job_status.serialize_aws_json_1_1(
                value["processing_job_status"]
            )
        )
    if "exit_message" in value:
        out["ExitMessage"] = value["exit_message"]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "processing_end_time" in value:
        import capo_sagemaker.types.timestamp

        out["ProcessingEndTime"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["processing_end_time"]
            )
        )
    if "processing_start_time" in value:
        import capo_sagemaker.types.timestamp

        out["ProcessingStartTime"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["processing_start_time"]
            )
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "monitoring_schedule_arn" in value:
        out["MonitoringScheduleArn"] = value["monitoring_schedule_arn"]
    if "auto_ml_job_arn" in value:
        out["AutoMLJobArn"] = value["auto_ml_job_arn"]
    if "training_job_arn" in value:
        out["TrainingJobArn"] = value["training_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProcessingJobResponse:
    out: DescribeProcessingJobResponse = {}  # type: ignore[typeddict-item]
    if "ProcessingInputs" in data:
        import capo_sagemaker.types.processing_inputs

        out["processing_inputs"] = (
            capo_sagemaker.types.processing_inputs.deserialize_aws_json_1_1(
                data["ProcessingInputs"]
            )
        )
    if "ProcessingOutputConfig" in data:
        import capo_sagemaker.types.processing_output_config

        out["processing_output_config"] = (
            capo_sagemaker.types.processing_output_config.deserialize_aws_json_1_1(
                data["ProcessingOutputConfig"]
            )
        )
    if "ProcessingJobName" in data:
        out["processing_job_name"] = data["ProcessingJobName"]
    if "ProcessingResources" in data:
        import capo_sagemaker.types.processing_resources

        out["processing_resources"] = (
            capo_sagemaker.types.processing_resources.deserialize_aws_json_1_1(
                data["ProcessingResources"]
            )
        )
    if "StoppingCondition" in data:
        import capo_sagemaker.types.processing_stopping_condition

        out["stopping_condition"] = (
            capo_sagemaker.types.processing_stopping_condition.deserialize_aws_json_1_1(
                data["StoppingCondition"]
            )
        )
    if "AppSpecification" in data:
        import capo_sagemaker.types.app_specification

        out["app_specification"] = (
            capo_sagemaker.types.app_specification.deserialize_aws_json_1_1(
                data["AppSpecification"]
            )
        )
    if "Environment" in data:
        import capo_sagemaker.types.processing_environment_map

        out["environment"] = (
            capo_sagemaker.types.processing_environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    if "NetworkConfig" in data:
        import capo_sagemaker.types.network_config

        out["network_config"] = (
            capo_sagemaker.types.network_config.deserialize_aws_json_1_1(
                data["NetworkConfig"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "ExperimentConfig" in data:
        import capo_sagemaker.types.experiment_config

        out["experiment_config"] = (
            capo_sagemaker.types.experiment_config.deserialize_aws_json_1_1(
                data["ExperimentConfig"]
            )
        )
    if "ProcessingJobArn" in data:
        out["processing_job_arn"] = data["ProcessingJobArn"]
    if "ProcessingJobStatus" in data:
        import capo_sagemaker.types.processing_job_status

        out["processing_job_status"] = (
            capo_sagemaker.types.processing_job_status.deserialize_aws_json_1_1(
                data["ProcessingJobStatus"]
            )
        )
    if "ExitMessage" in data:
        out["exit_message"] = data["ExitMessage"]
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "ProcessingEndTime" in data:
        import capo_sagemaker.types.timestamp

        out["processing_end_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["ProcessingEndTime"]
            )
        )
    if "ProcessingStartTime" in data:
        import capo_sagemaker.types.timestamp

        out["processing_start_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["ProcessingStartTime"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "MonitoringScheduleArn" in data:
        out["monitoring_schedule_arn"] = data["MonitoringScheduleArn"]
    if "AutoMLJobArn" in data:
        out["auto_ml_job_arn"] = data["AutoMLJobArn"]
    if "TrainingJobArn" in data:
        out["training_job_arn"] = data["TrainingJobArn"]
    return out
