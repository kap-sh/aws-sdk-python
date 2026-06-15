"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningJobConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_objective
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_strategy_config
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_strategy_type
    import aws_sdk_sagemaker.types.parameter_ranges
    import aws_sdk_sagemaker.types.random_seed
    import aws_sdk_sagemaker.types.resource_limits
    import aws_sdk_sagemaker.types.training_job_early_stopping_type
    import aws_sdk_sagemaker.types.tuning_job_completion_criteria


class HyperParameterTuningJobConfig(TypedDict):
    strategy: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_strategy_type.HyperParameterTuningJobStrategyType"
    ]
    r"""<p>Specifies how hyperparameter tuning chooses the combinations of hyperparameter values to use for the training job it launches. For information about search strategies, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html\">How Hyperparameter Tuning Works</a>.</p>"""
    strategy_config: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_strategy_config.HyperParameterTuningJobStrategyConfig"
    ]
    """<p>The configuration for the <code>Hyperband</code> optimization strategy. This parameter should be provided only if <code>Hyperband</code> is selected as the strategy for <code>HyperParameterTuningJobConfig</code>.</p>"""
    hyper_parameter_tuning_job_objective: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_objective.HyperParameterTuningJobObjective"
    ]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobObjective.html\">HyperParameterTuningJobObjective</a> specifies the objective metric used to evaluate the performance of training jobs launched by this tuning job.</p>"""
    resource_limits: NotRequired[
        "aws_sdk_sagemaker.types.resource_limits.ResourceLimits"
    ]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceLimits.html\">ResourceLimits</a> object that specifies the maximum number of training and parallel training jobs that can be used for this hyperparameter tuning job.</p>"""
    parameter_ranges: NotRequired[
        "aws_sdk_sagemaker.types.parameter_ranges.ParameterRanges"
    ]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ParameterRanges.html\">ParameterRanges</a> object that specifies the ranges of hyperparameters that this tuning job searches over to find the optimal configuration for the highest model performance against your chosen objective metric. </p>"""
    training_job_early_stopping_type: NotRequired[
        "aws_sdk_sagemaker.types.training_job_early_stopping_type.TrainingJobEarlyStoppingType"
    ]
    r"""<p>Specifies whether to use early stopping for training jobs launched by the hyperparameter tuning job. Because the <code>Hyperband</code> strategy has its own advanced internal early stopping mechanism, <code>TrainingJobEarlyStoppingType</code> must be <code>OFF</code> to use <code>Hyperband</code>. This parameter can take on one of the following values (the default value is <code>OFF</code>):</p> <dl> <dt>OFF</dt> <dd> <p>Training jobs launched by the hyperparameter tuning job do not use early stopping.</p> </dd> <dt>AUTO</dt> <dd> <p>SageMaker stops training jobs launched by the hyperparameter tuning job when they are unlikely to perform better than previously completed training jobs. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-early-stopping.html\">Stop Training Jobs Early</a>.</p> </dd> </dl>"""
    tuning_job_completion_criteria: NotRequired[
        "aws_sdk_sagemaker.types.tuning_job_completion_criteria.TuningJobCompletionCriteria"
    ]
    """<p>The tuning job's completion criteria.</p>"""
    random_seed: NotRequired["aws_sdk_sagemaker.types.random_seed.RandomSeed"]
    """<p>A value used to initialize a pseudo-random number generator. Setting a random seed and using the same seed later for the same tuning job will allow hyperparameter optimization to find more a consistent hyperparameter configuration between the two runs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTuningJobConfig) -> dict:
    out: dict = {}
    if "strategy" in value:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_strategy_type

        out["Strategy"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_strategy_type.serialize_aws_json_1_1(
                value["strategy"]
            )
        )
    if "strategy_config" in value:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_strategy_config

        out["StrategyConfig"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_strategy_config.serialize_aws_json_1_1(
                value["strategy_config"]
            )
        )
    if "hyper_parameter_tuning_job_objective" in value:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_objective

        out["HyperParameterTuningJobObjective"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_objective.serialize_aws_json_1_1(
                value["hyper_parameter_tuning_job_objective"]
            )
        )
    if "resource_limits" in value:
        import aws_sdk_sagemaker.types.resource_limits

        out["ResourceLimits"] = (
            aws_sdk_sagemaker.types.resource_limits.serialize_aws_json_1_1(
                value["resource_limits"]
            )
        )
    if "parameter_ranges" in value:
        import aws_sdk_sagemaker.types.parameter_ranges

        out["ParameterRanges"] = (
            aws_sdk_sagemaker.types.parameter_ranges.serialize_aws_json_1_1(
                value["parameter_ranges"]
            )
        )
    if "training_job_early_stopping_type" in value:
        import aws_sdk_sagemaker.types.training_job_early_stopping_type

        out["TrainingJobEarlyStoppingType"] = (
            aws_sdk_sagemaker.types.training_job_early_stopping_type.serialize_aws_json_1_1(
                value["training_job_early_stopping_type"]
            )
        )
    if "tuning_job_completion_criteria" in value:
        import aws_sdk_sagemaker.types.tuning_job_completion_criteria

        out["TuningJobCompletionCriteria"] = (
            aws_sdk_sagemaker.types.tuning_job_completion_criteria.serialize_aws_json_1_1(
                value["tuning_job_completion_criteria"]
            )
        )
    if "random_seed" in value:
        out["RandomSeed"] = value["random_seed"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HyperParameterTuningJobConfig:
    out: HyperParameterTuningJobConfig = {}  # type: ignore[typeddict-item]
    if "Strategy" in data:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_strategy_type

        out["strategy"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_strategy_type.deserialize_aws_json_1_1(
                data["Strategy"]
            )
        )
    if "StrategyConfig" in data:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_strategy_config

        out["strategy_config"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_strategy_config.deserialize_aws_json_1_1(
                data["StrategyConfig"]
            )
        )
    if "HyperParameterTuningJobObjective" in data:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_objective

        out["hyper_parameter_tuning_job_objective"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_objective.deserialize_aws_json_1_1(
                data["HyperParameterTuningJobObjective"]
            )
        )
    if "ResourceLimits" in data:
        import aws_sdk_sagemaker.types.resource_limits

        out["resource_limits"] = (
            aws_sdk_sagemaker.types.resource_limits.deserialize_aws_json_1_1(
                data["ResourceLimits"]
            )
        )
    if "ParameterRanges" in data:
        import aws_sdk_sagemaker.types.parameter_ranges

        out["parameter_ranges"] = (
            aws_sdk_sagemaker.types.parameter_ranges.deserialize_aws_json_1_1(
                data["ParameterRanges"]
            )
        )
    if "TrainingJobEarlyStoppingType" in data:
        import aws_sdk_sagemaker.types.training_job_early_stopping_type

        out["training_job_early_stopping_type"] = (
            aws_sdk_sagemaker.types.training_job_early_stopping_type.deserialize_aws_json_1_1(
                data["TrainingJobEarlyStoppingType"]
            )
        )
    if "TuningJobCompletionCriteria" in data:
        import aws_sdk_sagemaker.types.tuning_job_completion_criteria

        out["tuning_job_completion_criteria"] = (
            aws_sdk_sagemaker.types.tuning_job_completion_criteria.deserialize_aws_json_1_1(
                data["TuningJobCompletionCriteria"]
            )
        )
    if "RandomSeed" in data:
        out["random_seed"] = data["RandomSeed"]
    return out
