"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeHyperParameterTuningJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.autotune
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.hyper_parameter_training_job_definition
    import aws_sdk_sagemaker.types.hyper_parameter_training_job_definitions
    import aws_sdk_sagemaker.types.hyper_parameter_training_job_summary
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_arn
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_completion_details
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_config
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_consumed_resources
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_name
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_status
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_warm_start_config
    import aws_sdk_sagemaker.types.objective_status_counters
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.training_job_status_counters


class DescribeHyperParameterTuningJobResponse(TypedDict):
    hyper_parameter_tuning_job_name: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_name.HyperParameterTuningJobName"
    ]
    """<p>The name of the hyperparameter tuning job.</p>"""
    hyper_parameter_tuning_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_arn.HyperParameterTuningJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the tuning job.</p>"""
    hyper_parameter_tuning_job_config: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_config.HyperParameterTuningJobConfig"
    ]
    """<p>The <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html\">HyperParameterTuningJobConfig</a> object that specifies the configuration of the tuning job.</p>"""
    training_job_definition: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_training_job_definition.HyperParameterTrainingJobDefinition"
    ]
    """<p>The <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html\">HyperParameterTrainingJobDefinition</a> object that specifies the definition of the training jobs that this tuning job launches.</p>"""
    training_job_definitions: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_training_job_definitions.HyperParameterTrainingJobDefinitions"
    ]
    """<p>A list of the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html\">HyperParameterTrainingJobDefinition</a> objects launched for this tuning job.</p>"""
    hyper_parameter_tuning_job_status: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_status.HyperParameterTuningJobStatus"
    ]
    """<p>The status of the tuning job.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the tuning job started.</p>"""
    hyper_parameter_tuning_end_time: NotRequired[
        "aws_sdk_sagemaker.types.timestamp.Timestamp"
    ]
    """<p>The date and time that the tuning job ended.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the status of the tuning job was modified. </p>"""
    training_job_status_counters: NotRequired[
        "aws_sdk_sagemaker.types.training_job_status_counters.TrainingJobStatusCounters"
    ]
    """<p>The <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingJobStatusCounters.html\">TrainingJobStatusCounters</a> object that specifies the number of training jobs, categorized by status, that this tuning job launched.</p>"""
    objective_status_counters: NotRequired[
        "aws_sdk_sagemaker.types.objective_status_counters.ObjectiveStatusCounters"
    ]
    """<p>The <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ObjectiveStatusCounters.html\">ObjectiveStatusCounters</a> object that specifies the number of training jobs, categorized by the status of their final objective metric, that this tuning job launched.</p>"""
    best_training_job: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_training_job_summary.HyperParameterTrainingJobSummary"
    ]
    """<p>A <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingJobSummary.html\">TrainingJobSummary</a> object that describes the training job that completed with the best current <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobObjective.html\">HyperParameterTuningJobObjective</a>.</p>"""
    overall_best_training_job: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_training_job_summary.HyperParameterTrainingJobSummary"
    ]
    """<p>If the hyperparameter tuning job is an warm start tuning job with a <code>WarmStartType</code> of <code>IDENTICAL_DATA_AND_ALGORITHM</code>, this is the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingJobSummary.html\">TrainingJobSummary</a> for the training job with the best objective metric value of all training jobs launched by this tuning job and all parent jobs specified for the warm start tuning job.</p>"""
    warm_start_config: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_warm_start_config.HyperParameterTuningJobWarmStartConfig"
    ]
    """<p>The configuration for starting the hyperparameter parameter tuning job using one or more previous tuning jobs as a starting point. The results of previous tuning jobs are used to inform which combinations of hyperparameters to search over in the new tuning job.</p>"""
    autotune: NotRequired["aws_sdk_sagemaker.types.autotune.Autotune"]
    """<p>A flag to indicate if autotune is enabled for the hyperparameter tuning job.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the tuning job failed, the reason it failed.</p>"""
    tuning_job_completion_details: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_completion_details.HyperParameterTuningJobCompletionDetails"
    ]
    """<p>Tuning job completion information returned as the response from a hyperparameter tuning job. This information tells if your tuning job has or has not converged. It also includes the number of training jobs that have not improved model performance as evaluated against the objective function.</p>"""
    consumed_resources: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_consumed_resources.HyperParameterTuningJobConsumedResources"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeHyperParameterTuningJobResponse) -> dict:
    out: dict = {}
    if "hyper_parameter_tuning_job_name" in value:
        out["HyperParameterTuningJobName"] = value["hyper_parameter_tuning_job_name"]
    if "hyper_parameter_tuning_job_arn" in value:
        out["HyperParameterTuningJobArn"] = value["hyper_parameter_tuning_job_arn"]
    if "hyper_parameter_tuning_job_config" in value:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_config

        out["HyperParameterTuningJobConfig"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_config.serialize_aws_json_1_1(
                value["hyper_parameter_tuning_job_config"]
            )
        )
    if "training_job_definition" in value:
        import aws_sdk_sagemaker.types.hyper_parameter_training_job_definition

        out["TrainingJobDefinition"] = (
            aws_sdk_sagemaker.types.hyper_parameter_training_job_definition.serialize_aws_json_1_1(
                value["training_job_definition"]
            )
        )
    if "training_job_definitions" in value:
        import aws_sdk_sagemaker.types.hyper_parameter_training_job_definitions

        out["TrainingJobDefinitions"] = (
            aws_sdk_sagemaker.types.hyper_parameter_training_job_definitions.serialize_aws_json_1_1(
                value["training_job_definitions"]
            )
        )
    if "hyper_parameter_tuning_job_status" in value:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_status

        out["HyperParameterTuningJobStatus"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_status.serialize_aws_json_1_1(
                value["hyper_parameter_tuning_job_status"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "hyper_parameter_tuning_end_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["HyperParameterTuningEndTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["hyper_parameter_tuning_end_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "training_job_status_counters" in value:
        import aws_sdk_sagemaker.types.training_job_status_counters

        out["TrainingJobStatusCounters"] = (
            aws_sdk_sagemaker.types.training_job_status_counters.serialize_aws_json_1_1(
                value["training_job_status_counters"]
            )
        )
    if "objective_status_counters" in value:
        import aws_sdk_sagemaker.types.objective_status_counters

        out["ObjectiveStatusCounters"] = (
            aws_sdk_sagemaker.types.objective_status_counters.serialize_aws_json_1_1(
                value["objective_status_counters"]
            )
        )
    if "best_training_job" in value:
        import aws_sdk_sagemaker.types.hyper_parameter_training_job_summary

        out["BestTrainingJob"] = (
            aws_sdk_sagemaker.types.hyper_parameter_training_job_summary.serialize_aws_json_1_1(
                value["best_training_job"]
            )
        )
    if "overall_best_training_job" in value:
        import aws_sdk_sagemaker.types.hyper_parameter_training_job_summary

        out["OverallBestTrainingJob"] = (
            aws_sdk_sagemaker.types.hyper_parameter_training_job_summary.serialize_aws_json_1_1(
                value["overall_best_training_job"]
            )
        )
    if "warm_start_config" in value:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_warm_start_config

        out["WarmStartConfig"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_warm_start_config.serialize_aws_json_1_1(
                value["warm_start_config"]
            )
        )
    if "autotune" in value:
        import aws_sdk_sagemaker.types.autotune

        out["Autotune"] = aws_sdk_sagemaker.types.autotune.serialize_aws_json_1_1(
            value["autotune"]
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "tuning_job_completion_details" in value:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_completion_details

        out["TuningJobCompletionDetails"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_completion_details.serialize_aws_json_1_1(
                value["tuning_job_completion_details"]
            )
        )
    if "consumed_resources" in value:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_consumed_resources

        out["ConsumedResources"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_consumed_resources.serialize_aws_json_1_1(
                value["consumed_resources"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeHyperParameterTuningJobResponse:
    out: DescribeHyperParameterTuningJobResponse = {}  # type: ignore[typeddict-item]
    if "HyperParameterTuningJobName" in data:
        out["hyper_parameter_tuning_job_name"] = data["HyperParameterTuningJobName"]
    if "HyperParameterTuningJobArn" in data:
        out["hyper_parameter_tuning_job_arn"] = data["HyperParameterTuningJobArn"]
    if "HyperParameterTuningJobConfig" in data:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_config

        out["hyper_parameter_tuning_job_config"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_config.deserialize_aws_json_1_1(
                data["HyperParameterTuningJobConfig"]
            )
        )
    if "TrainingJobDefinition" in data:
        import aws_sdk_sagemaker.types.hyper_parameter_training_job_definition

        out["training_job_definition"] = (
            aws_sdk_sagemaker.types.hyper_parameter_training_job_definition.deserialize_aws_json_1_1(
                data["TrainingJobDefinition"]
            )
        )
    if "TrainingJobDefinitions" in data:
        import aws_sdk_sagemaker.types.hyper_parameter_training_job_definitions

        out["training_job_definitions"] = (
            aws_sdk_sagemaker.types.hyper_parameter_training_job_definitions.deserialize_aws_json_1_1(
                data["TrainingJobDefinitions"]
            )
        )
    if "HyperParameterTuningJobStatus" in data:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_status

        out["hyper_parameter_tuning_job_status"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_status.deserialize_aws_json_1_1(
                data["HyperParameterTuningJobStatus"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "HyperParameterTuningEndTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["hyper_parameter_tuning_end_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["HyperParameterTuningEndTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "TrainingJobStatusCounters" in data:
        import aws_sdk_sagemaker.types.training_job_status_counters

        out["training_job_status_counters"] = (
            aws_sdk_sagemaker.types.training_job_status_counters.deserialize_aws_json_1_1(
                data["TrainingJobStatusCounters"]
            )
        )
    if "ObjectiveStatusCounters" in data:
        import aws_sdk_sagemaker.types.objective_status_counters

        out["objective_status_counters"] = (
            aws_sdk_sagemaker.types.objective_status_counters.deserialize_aws_json_1_1(
                data["ObjectiveStatusCounters"]
            )
        )
    if "BestTrainingJob" in data:
        import aws_sdk_sagemaker.types.hyper_parameter_training_job_summary

        out["best_training_job"] = (
            aws_sdk_sagemaker.types.hyper_parameter_training_job_summary.deserialize_aws_json_1_1(
                data["BestTrainingJob"]
            )
        )
    if "OverallBestTrainingJob" in data:
        import aws_sdk_sagemaker.types.hyper_parameter_training_job_summary

        out["overall_best_training_job"] = (
            aws_sdk_sagemaker.types.hyper_parameter_training_job_summary.deserialize_aws_json_1_1(
                data["OverallBestTrainingJob"]
            )
        )
    if "WarmStartConfig" in data:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_warm_start_config

        out["warm_start_config"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_warm_start_config.deserialize_aws_json_1_1(
                data["WarmStartConfig"]
            )
        )
    if "Autotune" in data:
        import aws_sdk_sagemaker.types.autotune

        out["autotune"] = aws_sdk_sagemaker.types.autotune.deserialize_aws_json_1_1(
            data["Autotune"]
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "TuningJobCompletionDetails" in data:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_completion_details

        out["tuning_job_completion_details"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_completion_details.deserialize_aws_json_1_1(
                data["TuningJobCompletionDetails"]
            )
        )
    if "ConsumedResources" in data:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_consumed_resources

        out["consumed_resources"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_consumed_resources.deserialize_aws_json_1_1(
                data["ConsumedResources"]
            )
        )
    return out
