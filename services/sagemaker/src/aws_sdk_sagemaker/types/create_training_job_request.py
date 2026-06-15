"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateTrainingJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.algorithm_specification
    import aws_sdk_sagemaker.types.boolean
    import aws_sdk_sagemaker.types.checkpoint_config
    import aws_sdk_sagemaker.types.debug_hook_config
    import aws_sdk_sagemaker.types.debug_rule_configurations
    import aws_sdk_sagemaker.types.experiment_config
    import aws_sdk_sagemaker.types.hyper_parameters
    import aws_sdk_sagemaker.types.infra_check_config
    import aws_sdk_sagemaker.types.input_data_config
    import aws_sdk_sagemaker.types.mlflow_config
    import aws_sdk_sagemaker.types.model_package_config
    import aws_sdk_sagemaker.types.output_data_config
    import aws_sdk_sagemaker.types.profiler_config
    import aws_sdk_sagemaker.types.profiler_rule_configurations
    import aws_sdk_sagemaker.types.remote_debug_config
    import aws_sdk_sagemaker.types.resource_config
    import aws_sdk_sagemaker.types.retry_strategy
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.serverless_job_config
    import aws_sdk_sagemaker.types.session_chaining_config
    import aws_sdk_sagemaker.types.stopping_condition
    import aws_sdk_sagemaker.types.tag_list
    import aws_sdk_sagemaker.types.tensor_board_output_config
    import aws_sdk_sagemaker.types.training_environment_map
    import aws_sdk_sagemaker.types.training_job_name
    import aws_sdk_sagemaker.types.vpc_config


class CreateTrainingJobRequest(TypedDict):
    training_job_name: NotRequired[
        "aws_sdk_sagemaker.types.training_job_name.TrainingJobName"
    ]
    """<p>The name of the training job. The name must be unique within an Amazon Web Services Region in an Amazon Web Services account. </p>"""
    hyper_parameters: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameters.HyperParameters"
    ]
    r"""<p>Algorithm-specific parameters that influence the quality of the model. You set hyperparameters before you start the learning process. For a list of hyperparameters for each training algorithm provided by SageMaker, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html\">Algorithms</a>. </p> <p>You can specify a maximum of 100 hyperparameters. Each hyperparameter is a key-value pair. Each key and value is limited to 256 characters, as specified by the <code>Length Constraint</code>. </p> <important> <p>Do not include any security-sensitive information including account access IDs, secrets, or tokens in any hyperparameter fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by any security-sensitive information included in the request hyperparameter variable or plain text fields.</p> </important>"""
    algorithm_specification: NotRequired[
        "aws_sdk_sagemaker.types.algorithm_specification.AlgorithmSpecification"
    ]
    r"""<p>The registry path of the Docker image that contains the training algorithm and algorithm-specific metadata, including the input mode. For more information about algorithms provided by SageMaker, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html\">Algorithms</a>. For information about providing your own algorithms, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html\">Using Your Own Algorithms with Amazon SageMaker</a>. </p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    r"""<p>The Amazon Resource Name (ARN) of an IAM role that SageMaker can assume to perform tasks on your behalf. </p> <p>During model training, SageMaker needs your permission to read input data from an S3 bucket, download a Docker image that contains training code, write model artifacts to an S3 bucket, write logs to Amazon CloudWatch Logs, and publish metrics to Amazon CloudWatch. You grant permissions for all of these tasks to an IAM role. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html\">SageMaker Roles</a>. </p> <note> <p>To be able to pass this role to SageMaker, the caller of this API must have the <code>iam:PassRole</code> permission.</p> </note>"""
    input_data_config: NotRequired[
        "aws_sdk_sagemaker.types.input_data_config.InputDataConfig"
    ]
    """<p>An array of <code>Channel</code> objects. Each channel is a named input source. <code>InputDataConfig</code> describes the input data and its location. </p> <p>Algorithms can accept input data from one or more channels. For example, an algorithm might have two channels of input data, <code>training_data</code> and <code>validation_data</code>. The configuration for each channel provides the S3, EFS, or FSx location where the input data is stored. It also provides information about the stored data: the MIME type, compression method, and whether the data is wrapped in RecordIO format. </p> <p>Depending on the input mode that the algorithm supports, SageMaker either copies input data files from an S3 bucket to a local directory in the Docker container, or makes it available as input streams. For example, if you specify an EFS location, input data files are available as input streams. They do not need to be downloaded.</p> <p>Your input must be in the same Amazon Web Services region as your training job.</p>"""
    output_data_config: NotRequired[
        "aws_sdk_sagemaker.types.output_data_config.OutputDataConfig"
    ]
    """<p>Specifies the path to the S3 location where you want to store model artifacts. SageMaker creates subfolders for the artifacts. </p>"""
    resource_config: NotRequired[
        "aws_sdk_sagemaker.types.resource_config.ResourceConfig"
    ]
    """<p>The resources, including the ML compute instances and ML storage volumes, to use for model training. </p> <p>ML storage volumes store model artifacts and incremental states. Training algorithms might also use ML storage volumes for scratch space. If you want SageMaker to use the ML storage volume to store the training data, choose <code>File</code> as the <code>TrainingInputMode</code> in the algorithm specification. For distributed training algorithms, specify an instance count greater than 1.</p>"""
    vpc_config: NotRequired["aws_sdk_sagemaker.types.vpc_config.VpcConfig"]
    r"""<p>A <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html\">VpcConfig</a> object that specifies the VPC that you want your training job to connect to. Control access to and from your training container by configuring the VPC. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html\">Protect Training Jobs by Using an Amazon Virtual Private Cloud</a>.</p>"""
    stopping_condition: NotRequired[
        "aws_sdk_sagemaker.types.stopping_condition.StoppingCondition"
    ]
    """<p>Specifies a limit to how long a model training job can run. It also specifies how long a managed Spot training job has to complete. When the job reaches the time limit, SageMaker ends the training job. Use this API to cap model training costs.</p> <p>To stop a job, SageMaker sends the algorithm the <code>SIGTERM</code> signal, which delays job termination for 120 seconds. Algorithms can use this 120-second window to save the model artifacts, so the results of training are not lost. </p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    r"""<p>An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services Resources</a>.</p> <important> <p>Do not include any security-sensitive information including account access IDs, secrets, or tokens in any tags. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by any security-sensitive information included in the request tag variable or plain text fields.</p> </important>"""
    enable_network_isolation: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>Isolates the training container. No inbound or outbound network calls can be made, except for calls between peers within a training cluster for distributed training. If you enable network isolation for training jobs that are configured to use a VPC, SageMaker downloads and uploads customer data and model artifacts through the specified VPC, but the training container does not have network access.</p>"""
    enable_inter_container_traffic_encryption: NotRequired[
        "aws_sdk_sagemaker.types.boolean.Boolean"
    ]
    r"""<p>To encrypt all communications between ML compute instances in distributed training, choose <code>True</code>. Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithm in distributed training. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/train-encrypt.html\">Protect Communications Between ML Compute Instances in a Distributed Training Job</a>.</p>"""
    enable_managed_spot_training: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>To train models using managed spot training, choose <code>True</code>. Managed spot training provides a fully managed and scalable infrastructure for training machine learning models. this option is useful when training jobs can be interrupted and when there is flexibility when the training job is run. </p> <p>The complete and intermediate results of jobs are stored in an Amazon S3 bucket, and can be used as a starting point to train models incrementally. Amazon SageMaker provides metrics and logs in CloudWatch. They can be used to see when managed spot training jobs are running, interrupted, resumed, or completed. </p>"""
    checkpoint_config: NotRequired[
        "aws_sdk_sagemaker.types.checkpoint_config.CheckpointConfig"
    ]
    """<p>Contains information about the output location for managed spot training checkpoint data.</p>"""
    debug_hook_config: NotRequired[
        "aws_sdk_sagemaker.types.debug_hook_config.DebugHookConfig"
    ]
    debug_rule_configurations: NotRequired[
        "aws_sdk_sagemaker.types.debug_rule_configurations.DebugRuleConfigurations"
    ]
    """<p>Configuration information for Amazon SageMaker Debugger rules for debugging output tensors.</p>"""
    tensor_board_output_config: NotRequired[
        "aws_sdk_sagemaker.types.tensor_board_output_config.TensorBoardOutputConfig"
    ]
    experiment_config: NotRequired[
        "aws_sdk_sagemaker.types.experiment_config.ExperimentConfig"
    ]
    profiler_config: NotRequired[
        "aws_sdk_sagemaker.types.profiler_config.ProfilerConfig"
    ]
    profiler_rule_configurations: NotRequired[
        "aws_sdk_sagemaker.types.profiler_rule_configurations.ProfilerRuleConfigurations"
    ]
    """<p>Configuration information for Amazon SageMaker Debugger rules for profiling system and framework metrics.</p>"""
    environment: NotRequired[
        "aws_sdk_sagemaker.types.training_environment_map.TrainingEnvironmentMap"
    ]
    """<p>The environment variables to set in the Docker container.</p> <important> <p>Do not include any security-sensitive information including account access IDs, secrets, or tokens in any environment fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request environment variable or plain text fields.</p> </important>"""
    retry_strategy: NotRequired["aws_sdk_sagemaker.types.retry_strategy.RetryStrategy"]
    """<p>The number of times to retry the job when the job fails due to an <code>InternalServerError</code>.</p>"""
    remote_debug_config: NotRequired[
        "aws_sdk_sagemaker.types.remote_debug_config.RemoteDebugConfig"
    ]
    r"""<p>Configuration for remote debugging. To learn more about the remote debugging functionality of SageMaker, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-debugging.html\">Access a training container through Amazon Web Services Systems Manager (SSM) for remote debugging</a>.</p>"""
    infra_check_config: NotRequired[
        "aws_sdk_sagemaker.types.infra_check_config.InfraCheckConfig"
    ]
    """<p>Contains information about the infrastructure health check configuration for the training job.</p>"""
    session_chaining_config: NotRequired[
        "aws_sdk_sagemaker.types.session_chaining_config.SessionChainingConfig"
    ]
    """<p>Contains information about attribute-based access control (ABAC) for the training job.</p>"""
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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTrainingJobRequest) -> dict:
    out: dict = {}
    if "training_job_name" in value:
        out["TrainingJobName"] = value["training_job_name"]
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
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
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
    if "debug_hook_config" in value:
        import aws_sdk_sagemaker.types.debug_hook_config

        out["DebugHookConfig"] = (
            aws_sdk_sagemaker.types.debug_hook_config.serialize_aws_json_1_1(
                value["debug_hook_config"]
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
    if "experiment_config" in value:
        import aws_sdk_sagemaker.types.experiment_config

        out["ExperimentConfig"] = (
            aws_sdk_sagemaker.types.experiment_config.serialize_aws_json_1_1(
                value["experiment_config"]
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
    if "session_chaining_config" in value:
        import aws_sdk_sagemaker.types.session_chaining_config

        out["SessionChainingConfig"] = (
            aws_sdk_sagemaker.types.session_chaining_config.serialize_aws_json_1_1(
                value["session_chaining_config"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTrainingJobRequest:
    out: CreateTrainingJobRequest = {}  # type: ignore[typeddict-item]
    if "TrainingJobName" in data:
        out["training_job_name"] = data["TrainingJobName"]
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
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
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
    if "DebugHookConfig" in data:
        import aws_sdk_sagemaker.types.debug_hook_config

        out["debug_hook_config"] = (
            aws_sdk_sagemaker.types.debug_hook_config.deserialize_aws_json_1_1(
                data["DebugHookConfig"]
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
    if "ExperimentConfig" in data:
        import aws_sdk_sagemaker.types.experiment_config

        out["experiment_config"] = (
            aws_sdk_sagemaker.types.experiment_config.deserialize_aws_json_1_1(
                data["ExperimentConfig"]
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
    if "SessionChainingConfig" in data:
        import aws_sdk_sagemaker.types.session_chaining_config

        out["session_chaining_config"] = (
            aws_sdk_sagemaker.types.session_chaining_config.deserialize_aws_json_1_1(
                data["SessionChainingConfig"]
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
    return out
