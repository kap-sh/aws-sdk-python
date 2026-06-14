"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateHyperParameterTuningJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.autotune
    import aws_sdk_sagemaker.types.hyper_parameter_training_job_definition
    import aws_sdk_sagemaker.types.hyper_parameter_training_job_definitions
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_config
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_name
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_warm_start_config
    import aws_sdk_sagemaker.types.tag_list


class CreateHyperParameterTuningJobRequest(TypedDict):
    hyper_parameter_tuning_job_name: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_name.HyperParameterTuningJobName"
    ]
    """<p>The name of the tuning job. This name is the prefix for the names of all training jobs that this tuning job launches. The name must be unique within the same Amazon Web Services account and Amazon Web Services Region. The name must have 1 to 32 characters. Valid characters are a-z, A-Z, 0-9, and : + = @ _ % - (hyphen). The name is not case sensitive.</p>"""
    hyper_parameter_tuning_job_config: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_config.HyperParameterTuningJobConfig"
    ]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html\">HyperParameterTuningJobConfig</a> object that describes the tuning job, including the search strategy, the objective metric used to evaluate training jobs, ranges of parameters to search, and resource limits for the tuning job. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html\">How Hyperparameter Tuning Works</a>.</p>"""
    training_job_definition: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_training_job_definition.HyperParameterTrainingJobDefinition"
    ]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html\">HyperParameterTrainingJobDefinition</a> object that describes the training jobs that this tuning job launches, including static hyperparameters, input data configuration, output data configuration, resource configuration, and stopping condition.</p>"""
    training_job_definitions: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_training_job_definitions.HyperParameterTrainingJobDefinitions"
    ]
    r"""<p>A list of the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html\">HyperParameterTrainingJobDefinition</a> objects launched for this tuning job.</p>"""
    warm_start_config: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_warm_start_config.HyperParameterTuningJobWarmStartConfig"
    ]
    """<p>Specifies the configuration for starting the hyperparameter tuning job using one or more previous tuning jobs as a starting point. The results of previous tuning jobs are used to inform which combinations of hyperparameters to search over in the new tuning job.</p> <p>All training jobs launched by the new hyperparameter tuning job are evaluated by using the objective metric. If you specify <code>IDENTICAL_DATA_AND_ALGORITHM</code> as the <code>WarmStartType</code> value for the warm start configuration, the training job that performs the best in the new tuning job is compared to the best training jobs from the parent tuning jobs. From these, the training job that performs the best as measured by the objective metric is returned as the overall best training job.</p> <note> <p>All training jobs launched by parent hyperparameter tuning jobs and the new hyperparameter tuning jobs count against the limit of training jobs for the tuning job.</p> </note>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    r"""<p>An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services Resources</a>.</p> <p>Tags that you specify for the tuning job are also added to all training jobs that the tuning job launches.</p>"""
    autotune: NotRequired["aws_sdk_sagemaker.types.autotune.Autotune"]
    r"""<p>Configures SageMaker Automatic model tuning (AMT) to automatically find optimal parameters for the following fields:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html#sagemaker-Type-HyperParameterTuningJobConfig-ParameterRanges\">ParameterRanges</a>: The names and ranges of parameters that a hyperparameter tuning job can optimize.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceLimits.html\">ResourceLimits</a>: The maximum resources that can be used for a training job. These resources include the maximum number of training jobs, the maximum runtime of a tuning job, and the maximum number of training jobs to run at the same time.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html#sagemaker-Type-HyperParameterTuningJobConfig-TrainingJobEarlyStoppingType\">TrainingJobEarlyStoppingType</a>: A flag that specifies whether or not to use early stopping for training jobs launched by a hyperparameter tuning job.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-RetryStrategy\">RetryStrategy</a>: The number of times to retry a training job.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html\">Strategy</a>: Specifies how hyperparameter tuning chooses the combinations of hyperparameter values to use for the training jobs that it launches.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ConvergenceDetected.html\">ConvergenceDetected</a>: A flag to indicate that Automatic model tuning (AMT) has detected model convergence.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHyperParameterTuningJobRequest) -> dict:
    out: dict = {}
    if "hyper_parameter_tuning_job_name" in value:
        out["HyperParameterTuningJobName"] = value["hyper_parameter_tuning_job_name"]
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
    if "warm_start_config" in value:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_warm_start_config

        out["WarmStartConfig"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_warm_start_config.serialize_aws_json_1_1(
                value["warm_start_config"]
            )
        )
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "autotune" in value:
        import aws_sdk_sagemaker.types.autotune

        out["Autotune"] = aws_sdk_sagemaker.types.autotune.serialize_aws_json_1_1(
            value["autotune"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHyperParameterTuningJobRequest:
    out: CreateHyperParameterTuningJobRequest = {}  # type: ignore[typeddict-item]
    if "HyperParameterTuningJobName" in data:
        out["hyper_parameter_tuning_job_name"] = data["HyperParameterTuningJobName"]
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
    if "WarmStartConfig" in data:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_warm_start_config

        out["warm_start_config"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_warm_start_config.deserialize_aws_json_1_1(
                data["WarmStartConfig"]
            )
        )
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "Autotune" in data:
        import aws_sdk_sagemaker.types.autotune

        out["autotune"] = aws_sdk_sagemaker.types.autotune.deserialize_aws_json_1_1(
            data["Autotune"]
        )
    return out
