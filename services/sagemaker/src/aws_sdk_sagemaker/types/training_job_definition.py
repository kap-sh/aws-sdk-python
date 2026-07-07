"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingJobDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hyper_parameters
    import aws_sdk_sagemaker.types.input_data_config
    import aws_sdk_sagemaker.types.output_data_config
    import aws_sdk_sagemaker.types.resource_config
    import aws_sdk_sagemaker.types.stopping_condition
    import aws_sdk_sagemaker.types.training_input_mode


class TrainingJobDefinition(TypedDict, closed=True):
    training_input_mode: NotRequired[
        "aws_sdk_sagemaker.types.training_input_mode.TrainingInputMode"
    ]
    hyper_parameters: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameters.HyperParameters"
    ]
    """<p>The hyperparameters used for the training job.</p>"""
    input_data_config: NotRequired[
        "aws_sdk_sagemaker.types.input_data_config.InputDataConfig"
    ]
    """<p>An array of <code>Channel</code> objects, each of which specifies an input source.</p>"""
    output_data_config: NotRequired[
        "aws_sdk_sagemaker.types.output_data_config.OutputDataConfig"
    ]
    """<p>the path to the S3 bucket where you want to store model artifacts. SageMaker creates subfolders for the artifacts.</p>"""
    resource_config: NotRequired[
        "aws_sdk_sagemaker.types.resource_config.ResourceConfig"
    ]
    """<p>The resources, including the ML compute instances and ML storage volumes, to use for model training.</p>"""
    stopping_condition: NotRequired[
        "aws_sdk_sagemaker.types.stopping_condition.StoppingCondition"
    ]
    """<p>Specifies a limit to how long a model training job can run. It also specifies how long a managed Spot training job has to complete. When the job reaches the time limit, SageMaker ends the training job. Use this API to cap model training costs.</p> <p>To stop a job, SageMaker sends the algorithm the SIGTERM signal, which delays job termination for 120 seconds. Algorithms can use this 120-second window to save the model artifacts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingJobDefinition) -> dict:
    out: dict = {}
    if "training_input_mode" in value:
        import aws_sdk_sagemaker.types.training_input_mode

        out["TrainingInputMode"] = (
            aws_sdk_sagemaker.types.training_input_mode.serialize_aws_json_1_1(
                value["training_input_mode"]
            )
        )
    if "hyper_parameters" in value:
        import aws_sdk_sagemaker.types.hyper_parameters

        out["HyperParameters"] = (
            aws_sdk_sagemaker.types.hyper_parameters.serialize_aws_json_1_1(
                value["hyper_parameters"]
            )
        )
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
    if "stopping_condition" in value:
        import aws_sdk_sagemaker.types.stopping_condition

        out["StoppingCondition"] = (
            aws_sdk_sagemaker.types.stopping_condition.serialize_aws_json_1_1(
                value["stopping_condition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingJobDefinition:
    out: TrainingJobDefinition = {}  # type: ignore[typeddict-item]
    if "TrainingInputMode" in data:
        import aws_sdk_sagemaker.types.training_input_mode

        out["training_input_mode"] = (
            aws_sdk_sagemaker.types.training_input_mode.deserialize_aws_json_1_1(
                data["TrainingInputMode"]
            )
        )
    if "HyperParameters" in data:
        import aws_sdk_sagemaker.types.hyper_parameters

        out["hyper_parameters"] = (
            aws_sdk_sagemaker.types.hyper_parameters.deserialize_aws_json_1_1(
                data["HyperParameters"]
            )
        )
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
    if "StoppingCondition" in data:
        import aws_sdk_sagemaker.types.stopping_condition

        out["stopping_condition"] = (
            aws_sdk_sagemaker.types.stopping_condition.deserialize_aws_json_1_1(
                data["StoppingCondition"]
            )
        )
    return out
