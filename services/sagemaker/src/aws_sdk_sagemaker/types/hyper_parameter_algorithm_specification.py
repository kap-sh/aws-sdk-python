"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterAlgorithmSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.algorithm_image
    import aws_sdk_sagemaker.types.arn_or_name
    import aws_sdk_sagemaker.types.metric_definition_list
    import aws_sdk_sagemaker.types.training_input_mode


class HyperParameterAlgorithmSpecification(TypedDict):
    training_image: NotRequired[
        "aws_sdk_sagemaker.types.algorithm_image.AlgorithmImage"
    ]
    r"""<p> The registry path of the Docker image that contains the training algorithm. For information about Docker registry paths for built-in algorithms, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html\">Algorithms Provided by Amazon SageMaker: Common Parameters</a>. SageMaker supports both <code>registry/repository[:tag]</code> and <code>registry/repository[@digest]</code> image path formats. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html\">Using Your Own Algorithms with Amazon SageMaker</a>.</p>"""
    training_input_mode: NotRequired[
        "aws_sdk_sagemaker.types.training_input_mode.TrainingInputMode"
    ]
    algorithm_name: NotRequired["aws_sdk_sagemaker.types.arn_or_name.ArnOrName"]
    """<p>The name of the resource algorithm to use for the hyperparameter tuning job. If you specify a value for this parameter, do not specify a value for <code>TrainingImage</code>.</p>"""
    metric_definitions: NotRequired[
        "aws_sdk_sagemaker.types.metric_definition_list.MetricDefinitionList"
    ]
    r"""<p>An array of <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricDefinition.html\">MetricDefinition</a> objects that specify the metrics that the algorithm emits.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterAlgorithmSpecification) -> dict:
    out: dict = {}
    if "training_image" in value:
        out["TrainingImage"] = value["training_image"]
    if "training_input_mode" in value:
        import aws_sdk_sagemaker.types.training_input_mode

        out["TrainingInputMode"] = (
            aws_sdk_sagemaker.types.training_input_mode.serialize_aws_json_1_1(
                value["training_input_mode"]
            )
        )
    if "algorithm_name" in value:
        out["AlgorithmName"] = value["algorithm_name"]
    if "metric_definitions" in value:
        import aws_sdk_sagemaker.types.metric_definition_list

        out["MetricDefinitions"] = (
            aws_sdk_sagemaker.types.metric_definition_list.serialize_aws_json_1_1(
                value["metric_definitions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HyperParameterAlgorithmSpecification:
    out: HyperParameterAlgorithmSpecification = {}  # type: ignore[typeddict-item]
    if "TrainingImage" in data:
        out["training_image"] = data["TrainingImage"]
    if "TrainingInputMode" in data:
        import aws_sdk_sagemaker.types.training_input_mode

        out["training_input_mode"] = (
            aws_sdk_sagemaker.types.training_input_mode.deserialize_aws_json_1_1(
                data["TrainingInputMode"]
            )
        )
    if "AlgorithmName" in data:
        out["algorithm_name"] = data["AlgorithmName"]
    if "MetricDefinitions" in data:
        import aws_sdk_sagemaker.types.metric_definition_list

        out["metric_definitions"] = (
            aws_sdk_sagemaker.types.metric_definition_list.deserialize_aws_json_1_1(
                data["MetricDefinitions"]
            )
        )
    return out
