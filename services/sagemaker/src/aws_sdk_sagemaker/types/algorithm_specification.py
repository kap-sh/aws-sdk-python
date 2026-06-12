"""Generated from Smithy shape ``com.amazonaws.sagemaker#AlgorithmSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.algorithm_image
    import aws_sdk_sagemaker.types.arn_or_name
    import aws_sdk_sagemaker.types.boolean
    import aws_sdk_sagemaker.types.metric_definition_list
    import aws_sdk_sagemaker.types.training_container_arguments
    import aws_sdk_sagemaker.types.training_container_entrypoint
    import aws_sdk_sagemaker.types.training_image_config
    import aws_sdk_sagemaker.types.training_input_mode


class AlgorithmSpecification(TypedDict):
    training_image: NotRequired[
        "aws_sdk_sagemaker.types.algorithm_image.AlgorithmImage"
    ]
    """<p>The registry path of the Docker image that contains the training algorithm. For information about docker registry paths for SageMaker built-in algorithms, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html\">Docker Registry Paths and Example Code</a> in the <i>Amazon SageMaker developer guide</i>. SageMaker supports both <code>registry/repository[:tag]</code> and <code>registry/repository[@digest]</code> image path formats. For more information about using your custom training container, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html\">Using Your Own Algorithms with Amazon SageMaker</a>.</p> <note> <p>You must specify either the algorithm name to the <code>AlgorithmName</code> parameter or the image URI of the algorithm container to the <code>TrainingImage</code> parameter.</p> <p>For more information, see the note in the <code>AlgorithmName</code> parameter description.</p> </note>"""
    algorithm_name: NotRequired["aws_sdk_sagemaker.types.arn_or_name.ArnOrName"]
    """<p>The name of the algorithm resource to use for the training job. This must be an algorithm resource that you created or subscribe to on Amazon Web Services Marketplace.</p> <note> <p>You must specify either the algorithm name to the <code>AlgorithmName</code> parameter or the image URI of the algorithm container to the <code>TrainingImage</code> parameter.</p> <p>Note that the <code>AlgorithmName</code> parameter is mutually exclusive with the <code>TrainingImage</code> parameter. If you specify a value for the <code>AlgorithmName</code> parameter, you can't specify a value for <code>TrainingImage</code>, and vice versa.</p> <p>If you specify values for both parameters, the training job might break; if you don't specify any value for both parameters, the training job might raise a <code>null</code> error.</p> </note>"""
    training_input_mode: NotRequired[
        "aws_sdk_sagemaker.types.training_input_mode.TrainingInputMode"
    ]
    metric_definitions: NotRequired[
        "aws_sdk_sagemaker.types.metric_definition_list.MetricDefinitionList"
    ]
    """<p>A list of metric definition objects. Each object specifies the metric name and regular expressions used to parse algorithm logs. SageMaker publishes each metric to Amazon CloudWatch.</p>"""
    enable_sage_maker_metrics_time_series: NotRequired[
        "aws_sdk_sagemaker.types.boolean.Boolean"
    ]
    """<p>To generate and save time-series metrics during training, set to <code>true</code>. The default is <code>false</code> and time-series metrics aren't generated except in the following cases:</p> <ul> <li> <p>You use one of the SageMaker built-in algorithms</p> </li> <li> <p>You use one of the following <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/pre-built-containers-frameworks-deep-learning.html\">Prebuilt SageMaker Docker Images</a>:</p> <ul> <li> <p>Tensorflow (version &gt;= 1.15)</p> </li> <li> <p>MXNet (version &gt;= 1.6)</p> </li> <li> <p>PyTorch (version &gt;= 1.3)</p> </li> </ul> </li> <li> <p>You specify at least one <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricDefinition.html\">MetricDefinition</a> </p> </li> </ul>"""
    container_entrypoint: NotRequired[
        "aws_sdk_sagemaker.types.training_container_entrypoint.TrainingContainerEntrypoint"
    ]
    """<p>The <a href=\"https://docs.docker.com/engine/reference/builder/\">entrypoint script for a Docker container</a> used to run a training job. This script takes precedence over the default train processing instructions. See <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html\">How Amazon SageMaker Runs Your Training Image</a> for more information.</p>"""
    container_arguments: NotRequired[
        "aws_sdk_sagemaker.types.training_container_arguments.TrainingContainerArguments"
    ]
    """<p>The arguments for a container used to run a training job. See <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html\">How Amazon SageMaker Runs Your Training Image</a> for additional information.</p>"""
    training_image_config: NotRequired[
        "aws_sdk_sagemaker.types.training_image_config.TrainingImageConfig"
    ]
    """<p>The configuration to use an image from a private Docker registry for a training job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlgorithmSpecification) -> dict:
    out: dict = {}
    if "training_image" in value:
        out["TrainingImage"] = value["training_image"]
    if "algorithm_name" in value:
        out["AlgorithmName"] = value["algorithm_name"]
    if "training_input_mode" in value:
        import aws_sdk_sagemaker.types.training_input_mode

        out["TrainingInputMode"] = (
            aws_sdk_sagemaker.types.training_input_mode.serialize_aws_json_1_1(
                value["training_input_mode"]
            )
        )
    if "metric_definitions" in value:
        import aws_sdk_sagemaker.types.metric_definition_list

        out["MetricDefinitions"] = (
            aws_sdk_sagemaker.types.metric_definition_list.serialize_aws_json_1_1(
                value["metric_definitions"]
            )
        )
    if "enable_sage_maker_metrics_time_series" in value:
        out["EnableSageMakerMetricsTimeSeries"] = value[
            "enable_sage_maker_metrics_time_series"
        ]
    if "container_entrypoint" in value:
        import aws_sdk_sagemaker.types.training_container_entrypoint

        out["ContainerEntrypoint"] = (
            aws_sdk_sagemaker.types.training_container_entrypoint.serialize_aws_json_1_1(
                value["container_entrypoint"]
            )
        )
    if "container_arguments" in value:
        import aws_sdk_sagemaker.types.training_container_arguments

        out["ContainerArguments"] = (
            aws_sdk_sagemaker.types.training_container_arguments.serialize_aws_json_1_1(
                value["container_arguments"]
            )
        )
    if "training_image_config" in value:
        import aws_sdk_sagemaker.types.training_image_config

        out["TrainingImageConfig"] = (
            aws_sdk_sagemaker.types.training_image_config.serialize_aws_json_1_1(
                value["training_image_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AlgorithmSpecification:
    out: AlgorithmSpecification = {}  # type: ignore[typeddict-item]
    if "TrainingImage" in data:
        out["training_image"] = data["TrainingImage"]
    if "AlgorithmName" in data:
        out["algorithm_name"] = data["AlgorithmName"]
    if "TrainingInputMode" in data:
        import aws_sdk_sagemaker.types.training_input_mode

        out["training_input_mode"] = (
            aws_sdk_sagemaker.types.training_input_mode.deserialize_aws_json_1_1(
                data["TrainingInputMode"]
            )
        )
    if "MetricDefinitions" in data:
        import aws_sdk_sagemaker.types.metric_definition_list

        out["metric_definitions"] = (
            aws_sdk_sagemaker.types.metric_definition_list.deserialize_aws_json_1_1(
                data["MetricDefinitions"]
            )
        )
    if "EnableSageMakerMetricsTimeSeries" in data:
        out["enable_sage_maker_metrics_time_series"] = data[
            "EnableSageMakerMetricsTimeSeries"
        ]
    if "ContainerEntrypoint" in data:
        import aws_sdk_sagemaker.types.training_container_entrypoint

        out["container_entrypoint"] = (
            aws_sdk_sagemaker.types.training_container_entrypoint.deserialize_aws_json_1_1(
                data["ContainerEntrypoint"]
            )
        )
    if "ContainerArguments" in data:
        import aws_sdk_sagemaker.types.training_container_arguments

        out["container_arguments"] = (
            aws_sdk_sagemaker.types.training_container_arguments.deserialize_aws_json_1_1(
                data["ContainerArguments"]
            )
        )
    if "TrainingImageConfig" in data:
        import aws_sdk_sagemaker.types.training_image_config

        out["training_image_config"] = (
            aws_sdk_sagemaker.types.training_image_config.deserialize_aws_json_1_1(
                data["TrainingImageConfig"]
            )
        )
    return out
