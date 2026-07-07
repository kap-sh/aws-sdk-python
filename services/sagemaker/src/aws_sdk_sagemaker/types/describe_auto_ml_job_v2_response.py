"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeAutoMLJobV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_candidate
    import aws_sdk_sagemaker.types.auto_ml_compute_config
    import aws_sdk_sagemaker.types.auto_ml_data_split_config
    import aws_sdk_sagemaker.types.auto_ml_failure_reason
    import aws_sdk_sagemaker.types.auto_ml_job_arn
    import aws_sdk_sagemaker.types.auto_ml_job_artifacts
    import aws_sdk_sagemaker.types.auto_ml_job_input_data_config
    import aws_sdk_sagemaker.types.auto_ml_job_name
    import aws_sdk_sagemaker.types.auto_ml_job_objective
    import aws_sdk_sagemaker.types.auto_ml_job_secondary_status
    import aws_sdk_sagemaker.types.auto_ml_job_status
    import aws_sdk_sagemaker.types.auto_ml_output_data_config
    import aws_sdk_sagemaker.types.auto_ml_partial_failure_reasons
    import aws_sdk_sagemaker.types.auto_ml_problem_type_config
    import aws_sdk_sagemaker.types.auto_ml_problem_type_config_name
    import aws_sdk_sagemaker.types.auto_ml_resolved_attributes
    import aws_sdk_sagemaker.types.auto_ml_security_config
    import aws_sdk_sagemaker.types.model_deploy_config
    import aws_sdk_sagemaker.types.model_deploy_result
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.timestamp


class DescribeAutoMLJobV2Response(TypedDict, closed=True):
    auto_ml_job_name: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_job_name.AutoMLJobName"
    ]
    """<p>Returns the name of the AutoML job V2.</p>"""
    auto_ml_job_arn: NotRequired["aws_sdk_sagemaker.types.auto_ml_job_arn.AutoMLJobArn"]
    """<p>Returns the Amazon Resource Name (ARN) of the AutoML job V2.</p>"""
    auto_ml_job_input_data_config: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_job_input_data_config.AutoMLJobInputDataConfig"
    ]
    """<p>Returns an array of channel objects describing the input data and their location.</p>"""
    output_data_config: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_output_data_config.AutoMLOutputDataConfig"
    ]
    """<p>Returns the job's output data config.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role that has read permission to the input data location and write permission to the output data location in Amazon S3.</p>"""
    auto_ml_job_objective: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_job_objective.AutoMLJobObjective"
    ]
    """<p>Returns the job's objective.</p>"""
    auto_ml_problem_type_config: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_problem_type_config.AutoMLProblemTypeConfig"
    ]
    """<p>Returns the configuration settings of the problem type set for the AutoML job V2.</p>"""
    auto_ml_problem_type_config_name: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_problem_type_config_name.AutoMLProblemTypeConfigName"
    ]
    """<p>Returns the name of the problem type configuration set for the AutoML job V2.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Returns the creation time of the AutoML job V2.</p>"""
    end_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Returns the end time of the AutoML job V2.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Returns the job's last modified time.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_failure_reason.AutoMLFailureReason"
    ]
    """<p>Returns the reason for the failure of the AutoML job V2, when applicable.</p>"""
    partial_failure_reasons: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_partial_failure_reasons.AutoMLPartialFailureReasons"
    ]
    """<p>Returns a list of reasons for partial failures within an AutoML job V2.</p>"""
    best_candidate: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_candidate.AutoMLCandidate"
    ]
    """<p>Information about the candidate produced by an AutoML training job V2, including its status, steps, and other properties.</p>"""
    auto_ml_job_status: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_job_status.AutoMLJobStatus"
    ]
    """<p>Returns the status of the AutoML job V2.</p>"""
    auto_ml_job_secondary_status: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_job_secondary_status.AutoMLJobSecondaryStatus"
    ]
    """<p>Returns the secondary status of the AutoML job V2.</p>"""
    auto_ml_job_artifacts: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_job_artifacts.AutoMLJobArtifacts"
    ]
    resolved_attributes: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_resolved_attributes.AutoMLResolvedAttributes"
    ]
    """<p>Returns the resolved attributes used by the AutoML job V2.</p>"""
    model_deploy_config: NotRequired[
        "aws_sdk_sagemaker.types.model_deploy_config.ModelDeployConfig"
    ]
    """<p>Indicates whether the model was deployed automatically to an endpoint and the name of that endpoint if deployed automatically.</p>"""
    model_deploy_result: NotRequired[
        "aws_sdk_sagemaker.types.model_deploy_result.ModelDeployResult"
    ]
    """<p>Provides information about endpoint for the model deployment.</p>"""
    data_split_config: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_data_split_config.AutoMLDataSplitConfig"
    ]
    """<p>Returns the configuration settings of how the data are split into train and validation datasets.</p>"""
    security_config: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_security_config.AutoMLSecurityConfig"
    ]
    """<p>Returns the security configuration for traffic encryption or Amazon VPC settings.</p>"""
    auto_ml_compute_config: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_compute_config.AutoMLComputeConfig"
    ]
    """<p>The compute configuration used for the AutoML job V2.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAutoMLJobV2Response) -> dict:
    out: dict = {}
    if "auto_ml_job_name" in value:
        out["AutoMLJobName"] = value["auto_ml_job_name"]
    if "auto_ml_job_arn" in value:
        out["AutoMLJobArn"] = value["auto_ml_job_arn"]
    if "auto_ml_job_input_data_config" in value:
        import aws_sdk_sagemaker.types.auto_ml_job_input_data_config

        out["AutoMLJobInputDataConfig"] = (
            aws_sdk_sagemaker.types.auto_ml_job_input_data_config.serialize_aws_json_1_1(
                value["auto_ml_job_input_data_config"]
            )
        )
    if "output_data_config" in value:
        import aws_sdk_sagemaker.types.auto_ml_output_data_config

        out["OutputDataConfig"] = (
            aws_sdk_sagemaker.types.auto_ml_output_data_config.serialize_aws_json_1_1(
                value["output_data_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "auto_ml_job_objective" in value:
        import aws_sdk_sagemaker.types.auto_ml_job_objective

        out["AutoMLJobObjective"] = (
            aws_sdk_sagemaker.types.auto_ml_job_objective.serialize_aws_json_1_1(
                value["auto_ml_job_objective"]
            )
        )
    if "auto_ml_problem_type_config" in value:
        import aws_sdk_sagemaker.types.auto_ml_problem_type_config

        out["AutoMLProblemTypeConfig"] = (
            aws_sdk_sagemaker.types.auto_ml_problem_type_config.serialize_aws_json_1_1(
                value["auto_ml_problem_type_config"]
            )
        )
    if "auto_ml_problem_type_config_name" in value:
        import aws_sdk_sagemaker.types.auto_ml_problem_type_config_name

        out["AutoMLProblemTypeConfigName"] = (
            aws_sdk_sagemaker.types.auto_ml_problem_type_config_name.serialize_aws_json_1_1(
                value["auto_ml_problem_type_config_name"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "end_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["EndTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "partial_failure_reasons" in value:
        import aws_sdk_sagemaker.types.auto_ml_partial_failure_reasons

        out["PartialFailureReasons"] = (
            aws_sdk_sagemaker.types.auto_ml_partial_failure_reasons.serialize_aws_json_1_1(
                value["partial_failure_reasons"]
            )
        )
    if "best_candidate" in value:
        import aws_sdk_sagemaker.types.auto_ml_candidate

        out["BestCandidate"] = (
            aws_sdk_sagemaker.types.auto_ml_candidate.serialize_aws_json_1_1(
                value["best_candidate"]
            )
        )
    if "auto_ml_job_status" in value:
        import aws_sdk_sagemaker.types.auto_ml_job_status

        out["AutoMLJobStatus"] = (
            aws_sdk_sagemaker.types.auto_ml_job_status.serialize_aws_json_1_1(
                value["auto_ml_job_status"]
            )
        )
    if "auto_ml_job_secondary_status" in value:
        import aws_sdk_sagemaker.types.auto_ml_job_secondary_status

        out["AutoMLJobSecondaryStatus"] = (
            aws_sdk_sagemaker.types.auto_ml_job_secondary_status.serialize_aws_json_1_1(
                value["auto_ml_job_secondary_status"]
            )
        )
    if "auto_ml_job_artifacts" in value:
        import aws_sdk_sagemaker.types.auto_ml_job_artifacts

        out["AutoMLJobArtifacts"] = (
            aws_sdk_sagemaker.types.auto_ml_job_artifacts.serialize_aws_json_1_1(
                value["auto_ml_job_artifacts"]
            )
        )
    if "resolved_attributes" in value:
        import aws_sdk_sagemaker.types.auto_ml_resolved_attributes

        out["ResolvedAttributes"] = (
            aws_sdk_sagemaker.types.auto_ml_resolved_attributes.serialize_aws_json_1_1(
                value["resolved_attributes"]
            )
        )
    if "model_deploy_config" in value:
        import aws_sdk_sagemaker.types.model_deploy_config

        out["ModelDeployConfig"] = (
            aws_sdk_sagemaker.types.model_deploy_config.serialize_aws_json_1_1(
                value["model_deploy_config"]
            )
        )
    if "model_deploy_result" in value:
        import aws_sdk_sagemaker.types.model_deploy_result

        out["ModelDeployResult"] = (
            aws_sdk_sagemaker.types.model_deploy_result.serialize_aws_json_1_1(
                value["model_deploy_result"]
            )
        )
    if "data_split_config" in value:
        import aws_sdk_sagemaker.types.auto_ml_data_split_config

        out["DataSplitConfig"] = (
            aws_sdk_sagemaker.types.auto_ml_data_split_config.serialize_aws_json_1_1(
                value["data_split_config"]
            )
        )
    if "security_config" in value:
        import aws_sdk_sagemaker.types.auto_ml_security_config

        out["SecurityConfig"] = (
            aws_sdk_sagemaker.types.auto_ml_security_config.serialize_aws_json_1_1(
                value["security_config"]
            )
        )
    if "auto_ml_compute_config" in value:
        import aws_sdk_sagemaker.types.auto_ml_compute_config

        out["AutoMLComputeConfig"] = (
            aws_sdk_sagemaker.types.auto_ml_compute_config.serialize_aws_json_1_1(
                value["auto_ml_compute_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAutoMLJobV2Response:
    out: DescribeAutoMLJobV2Response = {}  # type: ignore[typeddict-item]
    if "AutoMLJobName" in data:
        out["auto_ml_job_name"] = data["AutoMLJobName"]
    if "AutoMLJobArn" in data:
        out["auto_ml_job_arn"] = data["AutoMLJobArn"]
    if "AutoMLJobInputDataConfig" in data:
        import aws_sdk_sagemaker.types.auto_ml_job_input_data_config

        out["auto_ml_job_input_data_config"] = (
            aws_sdk_sagemaker.types.auto_ml_job_input_data_config.deserialize_aws_json_1_1(
                data["AutoMLJobInputDataConfig"]
            )
        )
    if "OutputDataConfig" in data:
        import aws_sdk_sagemaker.types.auto_ml_output_data_config

        out["output_data_config"] = (
            aws_sdk_sagemaker.types.auto_ml_output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "AutoMLJobObjective" in data:
        import aws_sdk_sagemaker.types.auto_ml_job_objective

        out["auto_ml_job_objective"] = (
            aws_sdk_sagemaker.types.auto_ml_job_objective.deserialize_aws_json_1_1(
                data["AutoMLJobObjective"]
            )
        )
    if "AutoMLProblemTypeConfig" in data:
        import aws_sdk_sagemaker.types.auto_ml_problem_type_config

        out["auto_ml_problem_type_config"] = (
            aws_sdk_sagemaker.types.auto_ml_problem_type_config.deserialize_aws_json_1_1(
                data["AutoMLProblemTypeConfig"]
            )
        )
    if "AutoMLProblemTypeConfigName" in data:
        import aws_sdk_sagemaker.types.auto_ml_problem_type_config_name

        out["auto_ml_problem_type_config_name"] = (
            aws_sdk_sagemaker.types.auto_ml_problem_type_config_name.deserialize_aws_json_1_1(
                data["AutoMLProblemTypeConfigName"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["end_time"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "PartialFailureReasons" in data:
        import aws_sdk_sagemaker.types.auto_ml_partial_failure_reasons

        out["partial_failure_reasons"] = (
            aws_sdk_sagemaker.types.auto_ml_partial_failure_reasons.deserialize_aws_json_1_1(
                data["PartialFailureReasons"]
            )
        )
    if "BestCandidate" in data:
        import aws_sdk_sagemaker.types.auto_ml_candidate

        out["best_candidate"] = (
            aws_sdk_sagemaker.types.auto_ml_candidate.deserialize_aws_json_1_1(
                data["BestCandidate"]
            )
        )
    if "AutoMLJobStatus" in data:
        import aws_sdk_sagemaker.types.auto_ml_job_status

        out["auto_ml_job_status"] = (
            aws_sdk_sagemaker.types.auto_ml_job_status.deserialize_aws_json_1_1(
                data["AutoMLJobStatus"]
            )
        )
    if "AutoMLJobSecondaryStatus" in data:
        import aws_sdk_sagemaker.types.auto_ml_job_secondary_status

        out["auto_ml_job_secondary_status"] = (
            aws_sdk_sagemaker.types.auto_ml_job_secondary_status.deserialize_aws_json_1_1(
                data["AutoMLJobSecondaryStatus"]
            )
        )
    if "AutoMLJobArtifacts" in data:
        import aws_sdk_sagemaker.types.auto_ml_job_artifacts

        out["auto_ml_job_artifacts"] = (
            aws_sdk_sagemaker.types.auto_ml_job_artifacts.deserialize_aws_json_1_1(
                data["AutoMLJobArtifacts"]
            )
        )
    if "ResolvedAttributes" in data:
        import aws_sdk_sagemaker.types.auto_ml_resolved_attributes

        out["resolved_attributes"] = (
            aws_sdk_sagemaker.types.auto_ml_resolved_attributes.deserialize_aws_json_1_1(
                data["ResolvedAttributes"]
            )
        )
    if "ModelDeployConfig" in data:
        import aws_sdk_sagemaker.types.model_deploy_config

        out["model_deploy_config"] = (
            aws_sdk_sagemaker.types.model_deploy_config.deserialize_aws_json_1_1(
                data["ModelDeployConfig"]
            )
        )
    if "ModelDeployResult" in data:
        import aws_sdk_sagemaker.types.model_deploy_result

        out["model_deploy_result"] = (
            aws_sdk_sagemaker.types.model_deploy_result.deserialize_aws_json_1_1(
                data["ModelDeployResult"]
            )
        )
    if "DataSplitConfig" in data:
        import aws_sdk_sagemaker.types.auto_ml_data_split_config

        out["data_split_config"] = (
            aws_sdk_sagemaker.types.auto_ml_data_split_config.deserialize_aws_json_1_1(
                data["DataSplitConfig"]
            )
        )
    if "SecurityConfig" in data:
        import aws_sdk_sagemaker.types.auto_ml_security_config

        out["security_config"] = (
            aws_sdk_sagemaker.types.auto_ml_security_config.deserialize_aws_json_1_1(
                data["SecurityConfig"]
            )
        )
    if "AutoMLComputeConfig" in data:
        import aws_sdk_sagemaker.types.auto_ml_compute_config

        out["auto_ml_compute_config"] = (
            aws_sdk_sagemaker.types.auto_ml_compute_config.deserialize_aws_json_1_1(
                data["AutoMLComputeConfig"]
            )
        )
    return out
