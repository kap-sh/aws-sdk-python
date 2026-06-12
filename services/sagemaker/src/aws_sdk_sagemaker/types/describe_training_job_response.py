"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeTrainingJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.algorithm_specification
    import aws_sdk_sagemaker.types.auto_ml_job_arn
    import aws_sdk_sagemaker.types.billable_time_in_seconds
    import aws_sdk_sagemaker.types.billable_token_count
    import aws_sdk_sagemaker.types.boolean
    import aws_sdk_sagemaker.types.checkpoint_config
    import aws_sdk_sagemaker.types.debug_hook_config
    import aws_sdk_sagemaker.types.debug_rule_configurations
    import aws_sdk_sagemaker.types.debug_rule_evaluation_statuses
    import aws_sdk_sagemaker.types.experiment_config
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.final_metric_data_list
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_arn
    import aws_sdk_sagemaker.types.hyper_parameters
    import aws_sdk_sagemaker.types.infra_check_config
    import aws_sdk_sagemaker.types.input_data_config
    import aws_sdk_sagemaker.types.labeling_job_arn
    import aws_sdk_sagemaker.types.mlflow_config
    import aws_sdk_sagemaker.types.mlflow_details
    import aws_sdk_sagemaker.types.model_artifacts
    import aws_sdk_sagemaker.types.model_package_arn
    import aws_sdk_sagemaker.types.model_package_config
    import aws_sdk_sagemaker.types.output_data_config
    import aws_sdk_sagemaker.types.profiler_config
    import aws_sdk_sagemaker.types.profiler_rule_configurations
    import aws_sdk_sagemaker.types.profiler_rule_evaluation_statuses
    import aws_sdk_sagemaker.types.profiling_status
    import aws_sdk_sagemaker.types.remote_debug_config
    import aws_sdk_sagemaker.types.resource_config
    import aws_sdk_sagemaker.types.retry_strategy
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.secondary_status
    import aws_sdk_sagemaker.types.secondary_status_transitions
    import aws_sdk_sagemaker.types.serverless_job_config
    import aws_sdk_sagemaker.types.stopping_condition
    import aws_sdk_sagemaker.types.tensor_board_output_config
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.training_environment_map
    import aws_sdk_sagemaker.types.training_job_arn
    import aws_sdk_sagemaker.types.training_job_name
    import aws_sdk_sagemaker.types.training_job_status
    import aws_sdk_sagemaker.types.training_progress_info
    import aws_sdk_sagemaker.types.training_time_in_seconds
    import aws_sdk_sagemaker.types.vpc_config
    import aws_sdk_sagemaker.types.warm_pool_status


class DescribeTrainingJobResponse(TypedDict):
    training_job_name: NotRequired[
        "aws_sdk_sagemaker.types.training_job_name.TrainingJobName"
    ]
    """<p> Name of the model training job. </p>"""
    training_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.training_job_arn.TrainingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the training job.</p>"""
    tuning_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_arn.HyperParameterTuningJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the associated hyperparameter tuning job if the training job was launched by a hyperparameter tuning job.</p>"""
    labeling_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.labeling_job_arn.LabelingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the SageMaker Ground Truth labeling job that created the transform or training job.</p>"""
    auto_ml_job_arn: NotRequired["aws_sdk_sagemaker.types.auto_ml_job_arn.AutoMLJobArn"]
    """<p>The Amazon Resource Name (ARN) of an AutoML job.</p>"""
    model_artifacts: NotRequired[
        "aws_sdk_sagemaker.types.model_artifacts.ModelArtifacts"
    ]
    """<p>Information about the Amazon S3 location that is configured for storing model artifacts. </p>"""
    training_job_status: NotRequired[
        "aws_sdk_sagemaker.types.training_job_status.TrainingJobStatus"
    ]
    """<p>The status of the training job.</p> <p>SageMaker provides the following training job statuses:</p> <ul> <li> <p> <code>InProgress</code> - The training is in progress.</p> </li> <li> <p> <code>Completed</code> - The training job has completed.</p> </li> <li> <p> <code>Failed</code> - The training job has failed. To see the reason for the failure, see the <code>FailureReason</code> field in the response to a <code>DescribeTrainingJobResponse</code> call.</p> </li> <li> <p> <code>Stopping</code> - The training job is stopping.</p> </li> <li> <p> <code>Stopped</code> - The training job has stopped.</p> </li> </ul> <p>For more detailed information, see <code>SecondaryStatus</code>. </p>"""
    secondary_status: NotRequired[
        "aws_sdk_sagemaker.types.secondary_status.SecondaryStatus"
    ]
    """<p> Provides detailed information about the state of the training job. For detailed information on the secondary status of the training job, see <code>StatusMessage</code> under <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SecondaryStatusTransition.html\">SecondaryStatusTransition</a>.</p> <p>SageMaker provides primary statuses and secondary statuses that apply to each of them:</p> <dl> <dt>InProgress</dt> <dd> <ul> <li> <p> <code>Starting</code> - Starting the training job.</p> </li> <li> <p> <code>Pending</code> - The training job is waiting for compute capacity or compute resource provision.</p> </li> <li> <p> <code>Downloading</code> - An optional stage for algorithms that support <code>File</code> training input mode. It indicates that data is being downloaded to the ML storage volumes.</p> </li> <li> <p> <code>Training</code> - Training is in progress.</p> </li> <li> <p> <code>Interrupted</code> - The job stopped because the managed spot training instances were interrupted. </p> </li> <li> <p> <code>Uploading</code> - Training is complete and the model artifacts are being uploaded to the S3 location.</p> </li> </ul> </dd> <dt>Completed</dt> <dd> <ul> <li> <p> <code>Completed</code> - The training job has completed.</p> </li> </ul> </dd> <dt>Failed</dt> <dd> <ul> <li> <p> <code>Failed</code> - The training job has failed. The reason for the failure is returned in the <code>FailureReason</code> field of <code>DescribeTrainingJobResponse</code>.</p> </li> </ul> </dd> <dt>Stopped</dt> <dd> <ul> <li> <p> <code>MaxRuntimeExceeded</code> - The job stopped because it exceeded the maximum allowed runtime.</p> </li> <li> <p> <code>MaxWaitTimeExceeded</code> - The job stopped because it exceeded the maximum allowed wait time.</p> </li> <li> <p> <code>Stopped</code> - The training job has stopped.</p> </li> </ul> </dd> <dt>Stopping</dt> <dd> <ul> <li> <p> <code>Stopping</code> - Stopping the training job.</p> </li> </ul> </dd> </dl> <important> <p>Valid values for <code>SecondaryStatus</code> are subject to change. </p> </important> <p>We no longer support the following secondary statuses:</p> <ul> <li> <p> <code>LaunchingMLInstances</code> </p> </li> <li> <p> <code>PreparingTraining</code> </p> </li> <li> <p> <code>DownloadingTrainingImage</code> </p> </li> </ul>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the training job failed, the reason it failed. </p>"""
    hyper_parameters: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameters.HyperParameters"
    ]
    """<p>Algorithm-specific parameters. </p>"""
    algorithm_specification: NotRequired[
        "aws_sdk_sagemaker.types.algorithm_specification.AlgorithmSpecification"
    ]
    """<p>Information about the algorithm used for training, and algorithm metadata. </p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Web Services Identity and Access Management (IAM) role configured for the training job. </p>"""
    input_data_config: NotRequired[
        "aws_sdk_sagemaker.types.input_data_config.InputDataConfig"
    ]
    """<p>An array of <code>Channel</code> objects that describes each data input channel. </p>"""
    output_data_config: NotRequired[
        "aws_sdk_sagemaker.types.output_data_config.OutputDataConfig"
    ]
    """<p>The S3 path where model artifacts that you configured when creating the job are stored. SageMaker creates subfolders for model artifacts. </p>"""
    resource_config: NotRequired[
        "aws_sdk_sagemaker.types.resource_config.ResourceConfig"
    ]
    """<p>Resources, including ML compute instances and ML storage volumes, that are configured for model training. </p>"""
    warm_pool_status: NotRequired[
        "aws_sdk_sagemaker.types.warm_pool_status.WarmPoolStatus"
    ]
    """<p>The status of the warm pool associated with the training job.</p>"""
    vpc_config: NotRequired["aws_sdk_sagemaker.types.vpc_config.VpcConfig"]
    """<p>A <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html\">VpcConfig</a> object that specifies the VPC that this training job has access to. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html\">Protect Training Jobs by Using an Amazon Virtual Private Cloud</a>.</p>"""
    stopping_condition: NotRequired[
        "aws_sdk_sagemaker.types.stopping_condition.StoppingCondition"
    ]
    """<p>Specifies a limit to how long a model training job can run. It also specifies how long a managed Spot training job has to complete. When the job reaches the time limit, SageMaker ends the training job. Use this API to cap model training costs.</p> <p>To stop a job, SageMaker sends the algorithm the <code>SIGTERM</code> signal, which delays job termination for 120 seconds. Algorithms can use this 120-second window to save the model artifacts, so the results of training are not lost. </p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the training job was created.</p>"""
    training_start_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Indicates the time when the training job starts on training instances. You are billed for the time interval between this time and the value of <code>TrainingEndTime</code>. The start time in CloudWatch Logs might be later than this time. The difference is due to the time it takes to download the training data and to the size of the training container.</p>"""
    training_end_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Indicates the time when the training job ends on training instances. You are billed for the time interval between the value of <code>TrainingStartTime</code> and this time. For successful jobs and stopped jobs, this is the time after model artifacts are uploaded. For failed jobs, this is the time when SageMaker detects a job failure.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the status of the training job was last modified.</p>"""
    secondary_status_transitions: NotRequired[
        "aws_sdk_sagemaker.types.secondary_status_transitions.SecondaryStatusTransitions"
    ]
    """<p>A history of all of the secondary statuses that the training job has transitioned through.</p>"""
    final_metric_data_list: NotRequired[
        "aws_sdk_sagemaker.types.final_metric_data_list.FinalMetricDataList"
    ]
    """<p>A collection of <code>MetricData</code> objects that specify the names, values, and dates and times that the training algorithm emitted to Amazon CloudWatch.</p>"""
    enable_network_isolation: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>If you want to allow inbound or outbound network calls, except for calls between peers within a training cluster for distributed training, choose <code>True</code>. If you enable network isolation for training jobs that are configured to use a VPC, SageMaker downloads and uploads customer data and model artifacts through the specified VPC, but the training container does not have network access.</p>"""
    enable_inter_container_traffic_encryption: NotRequired[
        "aws_sdk_sagemaker.types.boolean.Boolean"
    ]
    """<p>To encrypt all communications between ML compute instances in distributed training, choose <code>True</code>. Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithms in distributed training.</p>"""
    enable_managed_spot_training: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>A Boolean indicating whether managed spot training is enabled (<code>True</code>) or not (<code>False</code>).</p>"""
    checkpoint_config: NotRequired[
        "aws_sdk_sagemaker.types.checkpoint_config.CheckpointConfig"
    ]
    training_time_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.training_time_in_seconds.TrainingTimeInSeconds"
    ]
    """<p>The training time in seconds.</p>"""
    billable_time_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.billable_time_in_seconds.BillableTimeInSeconds"
    ]
    """<p>The billable time in seconds. Billable time refers to the absolute wall-clock time.</p> <p>Multiply <code>BillableTimeInSeconds</code> by the number of instances (<code>InstanceCount</code>) in your training cluster to get the total compute time SageMaker bills you if you run distributed training. The formula is as follows: <code>BillableTimeInSeconds * InstanceCount</code> .</p> <p>You can calculate the savings from using managed spot training using the formula <code>(1 - BillableTimeInSeconds / TrainingTimeInSeconds) * 100</code>. For example, if <code>BillableTimeInSeconds</code> is 100 and <code>TrainingTimeInSeconds</code> is 500, the savings is 80%.</p>"""
    billable_token_count: NotRequired[
        "aws_sdk_sagemaker.types.billable_token_count.BillableTokenCount"
    ]
    """<p> The billable token count for eligible serverless training jobs. </p>"""
    debug_hook_config: NotRequired[
        "aws_sdk_sagemaker.types.debug_hook_config.DebugHookConfig"
    ]
    experiment_config: NotRequired[
        "aws_sdk_sagemaker.types.experiment_config.ExperimentConfig"
    ]
    debug_rule_configurations: NotRequired[
        "aws_sdk_sagemaker.types.debug_rule_configurations.DebugRuleConfigurations"
    ]
    """<p>Configuration information for Amazon SageMaker Debugger rules for debugging output tensors.</p>"""
    tensor_board_output_config: NotRequired[
        "aws_sdk_sagemaker.types.tensor_board_output_config.TensorBoardOutputConfig"
    ]
    debug_rule_evaluation_statuses: NotRequired[
        "aws_sdk_sagemaker.types.debug_rule_evaluation_statuses.DebugRuleEvaluationStatuses"
    ]
    """<p>Evaluation status of Amazon SageMaker Debugger rules for debugging on a training job.</p>"""
    profiler_config: NotRequired[
        "aws_sdk_sagemaker.types.profiler_config.ProfilerConfig"
    ]
    profiler_rule_configurations: NotRequired[
        "aws_sdk_sagemaker.types.profiler_rule_configurations.ProfilerRuleConfigurations"
    ]
    """<p>Configuration information for Amazon SageMaker Debugger rules for profiling system and framework metrics.</p>"""
    profiler_rule_evaluation_statuses: NotRequired[
        "aws_sdk_sagemaker.types.profiler_rule_evaluation_statuses.ProfilerRuleEvaluationStatuses"
    ]
    """<p>Evaluation status of Amazon SageMaker Debugger rules for profiling on a training job.</p>"""
    profiling_status: NotRequired[
        "aws_sdk_sagemaker.types.profiling_status.ProfilingStatus"
    ]
    """<p>Profiling status of a training job.</p>"""
    environment: NotRequired[
        "aws_sdk_sagemaker.types.training_environment_map.TrainingEnvironmentMap"
    ]
    """<p>The environment variables to set in the Docker container.</p> <important> <p>Do not include any security-sensitive information including account access IDs, secrets, or tokens in any environment fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request environment variable or plain text fields.</p> </important>"""
    retry_strategy: NotRequired["aws_sdk_sagemaker.types.retry_strategy.RetryStrategy"]
    """<p>The number of times to retry the job when the job fails due to an <code>InternalServerError</code>.</p>"""
    remote_debug_config: NotRequired[
        "aws_sdk_sagemaker.types.remote_debug_config.RemoteDebugConfig"
    ]
    """<p>Configuration for remote debugging. To learn more about the remote debugging functionality of SageMaker, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-debugging.html\">Access a training container through Amazon Web Services Systems Manager (SSM) for remote debugging</a>.</p>"""
    infra_check_config: NotRequired[
        "aws_sdk_sagemaker.types.infra_check_config.InfraCheckConfig"
    ]
    """<p>Contains information about the infrastructure health check configuration for the training job.</p>"""
    serverless_job_config: NotRequired[
        "aws_sdk_sagemaker.types.serverless_job_config.ServerlessJobConfig"
    ]
    """<p> The configuration for serverless training jobs. </p>"""
    mlflow_config: NotRequired["aws_sdk_sagemaker.types.mlflow_config.MlflowConfig"]
    """<p> The MLflow configuration using SageMaker managed MLflow. </p>"""
    model_package_config: NotRequired[
        "aws_sdk_sagemaker.types.model_package_config.ModelPackageConfig"
    ]
    """<p> The configuration for the model package. </p>"""
    mlflow_details: NotRequired["aws_sdk_sagemaker.types.mlflow_details.MlflowDetails"]
    """<p> The MLflow details of this job. </p>"""
    progress_info: NotRequired[
        "aws_sdk_sagemaker.types.training_progress_info.TrainingProgressInfo"
    ]
    """<p> The Serverless training job progress information. </p>"""
    output_model_package_arn: NotRequired[
        "aws_sdk_sagemaker.types.model_package_arn.ModelPackageArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the output model package containing model weights or checkpoints. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrainingJobResponse) -> dict:
    out: dict = {}
    if "training_job_name" in value:
        out["TrainingJobName"] = value["training_job_name"]
    if "training_job_arn" in value:
        out["TrainingJobArn"] = value["training_job_arn"]
    if "tuning_job_arn" in value:
        out["TuningJobArn"] = value["tuning_job_arn"]
    if "labeling_job_arn" in value:
        out["LabelingJobArn"] = value["labeling_job_arn"]
    if "auto_ml_job_arn" in value:
        out["AutoMLJobArn"] = value["auto_ml_job_arn"]
    if "model_artifacts" in value:
        import aws_sdk_sagemaker.types.model_artifacts

        out["ModelArtifacts"] = (
            aws_sdk_sagemaker.types.model_artifacts.serialize_aws_json_1_1(
                value["model_artifacts"]
            )
        )
    if "training_job_status" in value:
        import aws_sdk_sagemaker.types.training_job_status

        out["TrainingJobStatus"] = (
            aws_sdk_sagemaker.types.training_job_status.serialize_aws_json_1_1(
                value["training_job_status"]
            )
        )
    if "secondary_status" in value:
        import aws_sdk_sagemaker.types.secondary_status

        out["SecondaryStatus"] = (
            aws_sdk_sagemaker.types.secondary_status.serialize_aws_json_1_1(
                value["secondary_status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "hyper_parameters" in value:
        import aws_sdk_sagemaker.types.hyper_parameters

        out["HyperParameters"] = (
            aws_sdk_sagemaker.types.hyper_parameters.serialize_aws_json_1_1(
                value["hyper_parameters"]
            )
        )
    if "algorithm_specification" in value:
        import aws_sdk_sagemaker.types.algorithm_specification

        out["AlgorithmSpecification"] = (
            aws_sdk_sagemaker.types.algorithm_specification.serialize_aws_json_1_1(
                value["algorithm_specification"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "input_data_config" in value:
        import aws_sdk_sagemaker.types.input_data_config

        out["InputDataConfig"] = (
            aws_sdk_sagemaker.types.input_data_config.serialize_aws_json_1_1(
                value["input_data_config"]
            )
        )
    if "output_data_config" in value:
        import aws_sdk_sagemaker.types.output_data_config

        out["OutputDataConfig"] = (
            aws_sdk_sagemaker.types.output_data_config.serialize_aws_json_1_1(
                value["output_data_config"]
            )
        )
    if "resource_config" in value:
        import aws_sdk_sagemaker.types.resource_config

        out["ResourceConfig"] = (
            aws_sdk_sagemaker.types.resource_config.serialize_aws_json_1_1(
                value["resource_config"]
            )
        )
    if "warm_pool_status" in value:
        import aws_sdk_sagemaker.types.warm_pool_status

        out["WarmPoolStatus"] = (
            aws_sdk_sagemaker.types.warm_pool_status.serialize_aws_json_1_1(
                value["warm_pool_status"]
            )
        )
    if "vpc_config" in value:
        import aws_sdk_sagemaker.types.vpc_config

        out["VpcConfig"] = aws_sdk_sagemaker.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "stopping_condition" in value:
        import aws_sdk_sagemaker.types.stopping_condition

        out["StoppingCondition"] = (
            aws_sdk_sagemaker.types.stopping_condition.serialize_aws_json_1_1(
                value["stopping_condition"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "training_start_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["TrainingStartTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["training_start_time"]
            )
        )
    if "training_end_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["TrainingEndTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["training_end_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "secondary_status_transitions" in value:
        import aws_sdk_sagemaker.types.secondary_status_transitions

        out["SecondaryStatusTransitions"] = (
            aws_sdk_sagemaker.types.secondary_status_transitions.serialize_aws_json_1_1(
                value["secondary_status_transitions"]
            )
        )
    if "final_metric_data_list" in value:
        import aws_sdk_sagemaker.types.final_metric_data_list

        out["FinalMetricDataList"] = (
            aws_sdk_sagemaker.types.final_metric_data_list.serialize_aws_json_1_1(
                value["final_metric_data_list"]
            )
        )
    if "enable_network_isolation" in value:
        out["EnableNetworkIsolation"] = value["enable_network_isolation"]
    if "enable_inter_container_traffic_encryption" in value:
        out["EnableInterContainerTrafficEncryption"] = value[
            "enable_inter_container_traffic_encryption"
        ]
    if "enable_managed_spot_training" in value:
        out["EnableManagedSpotTraining"] = value["enable_managed_spot_training"]
    if "checkpoint_config" in value:
        import aws_sdk_sagemaker.types.checkpoint_config

        out["CheckpointConfig"] = (
            aws_sdk_sagemaker.types.checkpoint_config.serialize_aws_json_1_1(
                value["checkpoint_config"]
            )
        )
    if "training_time_in_seconds" in value:
        out["TrainingTimeInSeconds"] = value["training_time_in_seconds"]
    if "billable_time_in_seconds" in value:
        out["BillableTimeInSeconds"] = value["billable_time_in_seconds"]
    if "billable_token_count" in value:
        out["BillableTokenCount"] = value["billable_token_count"]
    if "debug_hook_config" in value:
        import aws_sdk_sagemaker.types.debug_hook_config

        out["DebugHookConfig"] = (
            aws_sdk_sagemaker.types.debug_hook_config.serialize_aws_json_1_1(
                value["debug_hook_config"]
            )
        )
    if "experiment_config" in value:
        import aws_sdk_sagemaker.types.experiment_config

        out["ExperimentConfig"] = (
            aws_sdk_sagemaker.types.experiment_config.serialize_aws_json_1_1(
                value["experiment_config"]
            )
        )
    if "debug_rule_configurations" in value:
        import aws_sdk_sagemaker.types.debug_rule_configurations

        out["DebugRuleConfigurations"] = (
            aws_sdk_sagemaker.types.debug_rule_configurations.serialize_aws_json_1_1(
                value["debug_rule_configurations"]
            )
        )
    if "tensor_board_output_config" in value:
        import aws_sdk_sagemaker.types.tensor_board_output_config

        out["TensorBoardOutputConfig"] = (
            aws_sdk_sagemaker.types.tensor_board_output_config.serialize_aws_json_1_1(
                value["tensor_board_output_config"]
            )
        )
    if "debug_rule_evaluation_statuses" in value:
        import aws_sdk_sagemaker.types.debug_rule_evaluation_statuses

        out["DebugRuleEvaluationStatuses"] = (
            aws_sdk_sagemaker.types.debug_rule_evaluation_statuses.serialize_aws_json_1_1(
                value["debug_rule_evaluation_statuses"]
            )
        )
    if "profiler_config" in value:
        import aws_sdk_sagemaker.types.profiler_config

        out["ProfilerConfig"] = (
            aws_sdk_sagemaker.types.profiler_config.serialize_aws_json_1_1(
                value["profiler_config"]
            )
        )
    if "profiler_rule_configurations" in value:
        import aws_sdk_sagemaker.types.profiler_rule_configurations

        out["ProfilerRuleConfigurations"] = (
            aws_sdk_sagemaker.types.profiler_rule_configurations.serialize_aws_json_1_1(
                value["profiler_rule_configurations"]
            )
        )
    if "profiler_rule_evaluation_statuses" in value:
        import aws_sdk_sagemaker.types.profiler_rule_evaluation_statuses

        out["ProfilerRuleEvaluationStatuses"] = (
            aws_sdk_sagemaker.types.profiler_rule_evaluation_statuses.serialize_aws_json_1_1(
                value["profiler_rule_evaluation_statuses"]
            )
        )
    if "profiling_status" in value:
        import aws_sdk_sagemaker.types.profiling_status

        out["ProfilingStatus"] = (
            aws_sdk_sagemaker.types.profiling_status.serialize_aws_json_1_1(
                value["profiling_status"]
            )
        )
    if "environment" in value:
        import aws_sdk_sagemaker.types.training_environment_map

        out["Environment"] = (
            aws_sdk_sagemaker.types.training_environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "retry_strategy" in value:
        import aws_sdk_sagemaker.types.retry_strategy

        out["RetryStrategy"] = (
            aws_sdk_sagemaker.types.retry_strategy.serialize_aws_json_1_1(
                value["retry_strategy"]
            )
        )
    if "remote_debug_config" in value:
        import aws_sdk_sagemaker.types.remote_debug_config

        out["RemoteDebugConfig"] = (
            aws_sdk_sagemaker.types.remote_debug_config.serialize_aws_json_1_1(
                value["remote_debug_config"]
            )
        )
    if "infra_check_config" in value:
        import aws_sdk_sagemaker.types.infra_check_config

        out["InfraCheckConfig"] = (
            aws_sdk_sagemaker.types.infra_check_config.serialize_aws_json_1_1(
                value["infra_check_config"]
            )
        )
    if "serverless_job_config" in value:
        import aws_sdk_sagemaker.types.serverless_job_config

        out["ServerlessJobConfig"] = (
            aws_sdk_sagemaker.types.serverless_job_config.serialize_aws_json_1_1(
                value["serverless_job_config"]
            )
        )
    if "mlflow_config" in value:
        import aws_sdk_sagemaker.types.mlflow_config

        out["MlflowConfig"] = (
            aws_sdk_sagemaker.types.mlflow_config.serialize_aws_json_1_1(
                value["mlflow_config"]
            )
        )
    if "model_package_config" in value:
        import aws_sdk_sagemaker.types.model_package_config

        out["ModelPackageConfig"] = (
            aws_sdk_sagemaker.types.model_package_config.serialize_aws_json_1_1(
                value["model_package_config"]
            )
        )
    if "mlflow_details" in value:
        import aws_sdk_sagemaker.types.mlflow_details

        out["MlflowDetails"] = (
            aws_sdk_sagemaker.types.mlflow_details.serialize_aws_json_1_1(
                value["mlflow_details"]
            )
        )
    if "progress_info" in value:
        import aws_sdk_sagemaker.types.training_progress_info

        out["ProgressInfo"] = (
            aws_sdk_sagemaker.types.training_progress_info.serialize_aws_json_1_1(
                value["progress_info"]
            )
        )
    if "output_model_package_arn" in value:
        out["OutputModelPackageArn"] = value["output_model_package_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrainingJobResponse:
    out: DescribeTrainingJobResponse = {}  # type: ignore[typeddict-item]
    if "TrainingJobName" in data:
        out["training_job_name"] = data["TrainingJobName"]
    if "TrainingJobArn" in data:
        out["training_job_arn"] = data["TrainingJobArn"]
    if "TuningJobArn" in data:
        out["tuning_job_arn"] = data["TuningJobArn"]
    if "LabelingJobArn" in data:
        out["labeling_job_arn"] = data["LabelingJobArn"]
    if "AutoMLJobArn" in data:
        out["auto_ml_job_arn"] = data["AutoMLJobArn"]
    if "ModelArtifacts" in data:
        import aws_sdk_sagemaker.types.model_artifacts

        out["model_artifacts"] = (
            aws_sdk_sagemaker.types.model_artifacts.deserialize_aws_json_1_1(
                data["ModelArtifacts"]
            )
        )
    if "TrainingJobStatus" in data:
        import aws_sdk_sagemaker.types.training_job_status

        out["training_job_status"] = (
            aws_sdk_sagemaker.types.training_job_status.deserialize_aws_json_1_1(
                data["TrainingJobStatus"]
            )
        )
    if "SecondaryStatus" in data:
        import aws_sdk_sagemaker.types.secondary_status

        out["secondary_status"] = (
            aws_sdk_sagemaker.types.secondary_status.deserialize_aws_json_1_1(
                data["SecondaryStatus"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "HyperParameters" in data:
        import aws_sdk_sagemaker.types.hyper_parameters

        out["hyper_parameters"] = (
            aws_sdk_sagemaker.types.hyper_parameters.deserialize_aws_json_1_1(
                data["HyperParameters"]
            )
        )
    if "AlgorithmSpecification" in data:
        import aws_sdk_sagemaker.types.algorithm_specification

        out["algorithm_specification"] = (
            aws_sdk_sagemaker.types.algorithm_specification.deserialize_aws_json_1_1(
                data["AlgorithmSpecification"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "InputDataConfig" in data:
        import aws_sdk_sagemaker.types.input_data_config

        out["input_data_config"] = (
            aws_sdk_sagemaker.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    if "OutputDataConfig" in data:
        import aws_sdk_sagemaker.types.output_data_config

        out["output_data_config"] = (
            aws_sdk_sagemaker.types.output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    if "ResourceConfig" in data:
        import aws_sdk_sagemaker.types.resource_config

        out["resource_config"] = (
            aws_sdk_sagemaker.types.resource_config.deserialize_aws_json_1_1(
                data["ResourceConfig"]
            )
        )
    if "WarmPoolStatus" in data:
        import aws_sdk_sagemaker.types.warm_pool_status

        out["warm_pool_status"] = (
            aws_sdk_sagemaker.types.warm_pool_status.deserialize_aws_json_1_1(
                data["WarmPoolStatus"]
            )
        )
    if "VpcConfig" in data:
        import aws_sdk_sagemaker.types.vpc_config

        out["vpc_config"] = aws_sdk_sagemaker.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if "StoppingCondition" in data:
        import aws_sdk_sagemaker.types.stopping_condition

        out["stopping_condition"] = (
            aws_sdk_sagemaker.types.stopping_condition.deserialize_aws_json_1_1(
                data["StoppingCondition"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "TrainingStartTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["training_start_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["TrainingStartTime"]
            )
        )
    if "TrainingEndTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["training_end_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["TrainingEndTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "SecondaryStatusTransitions" in data:
        import aws_sdk_sagemaker.types.secondary_status_transitions

        out["secondary_status_transitions"] = (
            aws_sdk_sagemaker.types.secondary_status_transitions.deserialize_aws_json_1_1(
                data["SecondaryStatusTransitions"]
            )
        )
    if "FinalMetricDataList" in data:
        import aws_sdk_sagemaker.types.final_metric_data_list

        out["final_metric_data_list"] = (
            aws_sdk_sagemaker.types.final_metric_data_list.deserialize_aws_json_1_1(
                data["FinalMetricDataList"]
            )
        )
    if "EnableNetworkIsolation" in data:
        out["enable_network_isolation"] = data["EnableNetworkIsolation"]
    if "EnableInterContainerTrafficEncryption" in data:
        out["enable_inter_container_traffic_encryption"] = data[
            "EnableInterContainerTrafficEncryption"
        ]
    if "EnableManagedSpotTraining" in data:
        out["enable_managed_spot_training"] = data["EnableManagedSpotTraining"]
    if "CheckpointConfig" in data:
        import aws_sdk_sagemaker.types.checkpoint_config

        out["checkpoint_config"] = (
            aws_sdk_sagemaker.types.checkpoint_config.deserialize_aws_json_1_1(
                data["CheckpointConfig"]
            )
        )
    if "TrainingTimeInSeconds" in data:
        out["training_time_in_seconds"] = data["TrainingTimeInSeconds"]
    if "BillableTimeInSeconds" in data:
        out["billable_time_in_seconds"] = data["BillableTimeInSeconds"]
    if "BillableTokenCount" in data:
        out["billable_token_count"] = data["BillableTokenCount"]
    if "DebugHookConfig" in data:
        import aws_sdk_sagemaker.types.debug_hook_config

        out["debug_hook_config"] = (
            aws_sdk_sagemaker.types.debug_hook_config.deserialize_aws_json_1_1(
                data["DebugHookConfig"]
            )
        )
    if "ExperimentConfig" in data:
        import aws_sdk_sagemaker.types.experiment_config

        out["experiment_config"] = (
            aws_sdk_sagemaker.types.experiment_config.deserialize_aws_json_1_1(
                data["ExperimentConfig"]
            )
        )
    if "DebugRuleConfigurations" in data:
        import aws_sdk_sagemaker.types.debug_rule_configurations

        out["debug_rule_configurations"] = (
            aws_sdk_sagemaker.types.debug_rule_configurations.deserialize_aws_json_1_1(
                data["DebugRuleConfigurations"]
            )
        )
    if "TensorBoardOutputConfig" in data:
        import aws_sdk_sagemaker.types.tensor_board_output_config

        out["tensor_board_output_config"] = (
            aws_sdk_sagemaker.types.tensor_board_output_config.deserialize_aws_json_1_1(
                data["TensorBoardOutputConfig"]
            )
        )
    if "DebugRuleEvaluationStatuses" in data:
        import aws_sdk_sagemaker.types.debug_rule_evaluation_statuses

        out["debug_rule_evaluation_statuses"] = (
            aws_sdk_sagemaker.types.debug_rule_evaluation_statuses.deserialize_aws_json_1_1(
                data["DebugRuleEvaluationStatuses"]
            )
        )
    if "ProfilerConfig" in data:
        import aws_sdk_sagemaker.types.profiler_config

        out["profiler_config"] = (
            aws_sdk_sagemaker.types.profiler_config.deserialize_aws_json_1_1(
                data["ProfilerConfig"]
            )
        )
    if "ProfilerRuleConfigurations" in data:
        import aws_sdk_sagemaker.types.profiler_rule_configurations

        out["profiler_rule_configurations"] = (
            aws_sdk_sagemaker.types.profiler_rule_configurations.deserialize_aws_json_1_1(
                data["ProfilerRuleConfigurations"]
            )
        )
    if "ProfilerRuleEvaluationStatuses" in data:
        import aws_sdk_sagemaker.types.profiler_rule_evaluation_statuses

        out["profiler_rule_evaluation_statuses"] = (
            aws_sdk_sagemaker.types.profiler_rule_evaluation_statuses.deserialize_aws_json_1_1(
                data["ProfilerRuleEvaluationStatuses"]
            )
        )
    if "ProfilingStatus" in data:
        import aws_sdk_sagemaker.types.profiling_status

        out["profiling_status"] = (
            aws_sdk_sagemaker.types.profiling_status.deserialize_aws_json_1_1(
                data["ProfilingStatus"]
            )
        )
    if "Environment" in data:
        import aws_sdk_sagemaker.types.training_environment_map

        out["environment"] = (
            aws_sdk_sagemaker.types.training_environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    if "RetryStrategy" in data:
        import aws_sdk_sagemaker.types.retry_strategy

        out["retry_strategy"] = (
            aws_sdk_sagemaker.types.retry_strategy.deserialize_aws_json_1_1(
                data["RetryStrategy"]
            )
        )
    if "RemoteDebugConfig" in data:
        import aws_sdk_sagemaker.types.remote_debug_config

        out["remote_debug_config"] = (
            aws_sdk_sagemaker.types.remote_debug_config.deserialize_aws_json_1_1(
                data["RemoteDebugConfig"]
            )
        )
    if "InfraCheckConfig" in data:
        import aws_sdk_sagemaker.types.infra_check_config

        out["infra_check_config"] = (
            aws_sdk_sagemaker.types.infra_check_config.deserialize_aws_json_1_1(
                data["InfraCheckConfig"]
            )
        )
    if "ServerlessJobConfig" in data:
        import aws_sdk_sagemaker.types.serverless_job_config

        out["serverless_job_config"] = (
            aws_sdk_sagemaker.types.serverless_job_config.deserialize_aws_json_1_1(
                data["ServerlessJobConfig"]
            )
        )
    if "MlflowConfig" in data:
        import aws_sdk_sagemaker.types.mlflow_config

        out["mlflow_config"] = (
            aws_sdk_sagemaker.types.mlflow_config.deserialize_aws_json_1_1(
                data["MlflowConfig"]
            )
        )
    if "ModelPackageConfig" in data:
        import aws_sdk_sagemaker.types.model_package_config

        out["model_package_config"] = (
            aws_sdk_sagemaker.types.model_package_config.deserialize_aws_json_1_1(
                data["ModelPackageConfig"]
            )
        )
    if "MlflowDetails" in data:
        import aws_sdk_sagemaker.types.mlflow_details

        out["mlflow_details"] = (
            aws_sdk_sagemaker.types.mlflow_details.deserialize_aws_json_1_1(
                data["MlflowDetails"]
            )
        )
    if "ProgressInfo" in data:
        import aws_sdk_sagemaker.types.training_progress_info

        out["progress_info"] = (
            aws_sdk_sagemaker.types.training_progress_info.deserialize_aws_json_1_1(
                data["ProgressInfo"]
            )
        )
    if "OutputModelPackageArn" in data:
        out["output_model_package_arn"] = data["OutputModelPackageArn"]
    return out
