"""Generated from Smithy shape ``com.amazonaws.sagemaker#LabelingJobAlgorithmsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.labeling_job_algorithm_specification_arn
    import aws_sdk_sagemaker.types.labeling_job_resource_config
    import aws_sdk_sagemaker.types.model_arn


class LabelingJobAlgorithmsConfig(TypedDict, closed=True):
    labeling_job_algorithm_specification_arn: NotRequired[
        "aws_sdk_sagemaker.types.labeling_job_algorithm_specification_arn.LabelingJobAlgorithmSpecificationArn"
    ]
    """<p>Specifies the Amazon Resource Name (ARN) of the algorithm used for auto-labeling. You must select one of the following ARNs:</p> <ul> <li> <p> <i>Image classification</i> </p> <p> <code>arn:aws:sagemaker:<i>region</i>:027400017018:labeling-job-algorithm-specification/image-classification</code> </p> </li> <li> <p> <i>Text classification</i> </p> <p> <code>arn:aws:sagemaker:<i>region</i>:027400017018:labeling-job-algorithm-specification/text-classification</code> </p> </li> <li> <p> <i>Object detection</i> </p> <p> <code>arn:aws:sagemaker:<i>region</i>:027400017018:labeling-job-algorithm-specification/object-detection</code> </p> </li> <li> <p> <i>Semantic Segmentation</i> </p> <p> <code>arn:aws:sagemaker:<i>region</i>:027400017018:labeling-job-algorithm-specification/semantic-segmentation</code> </p> </li> </ul>"""
    initial_active_learning_model_arn: NotRequired[
        "aws_sdk_sagemaker.types.model_arn.ModelArn"
    ]
    """<p>At the end of an auto-label job Ground Truth sends the Amazon Resource Name (ARN) of the final model used for auto-labeling. You can use this model as the starting point for subsequent similar jobs by providing the ARN of the model here. </p>"""
    labeling_job_resource_config: NotRequired[
        "aws_sdk_sagemaker.types.labeling_job_resource_config.LabelingJobResourceConfig"
    ]
    """<p>Provides configuration information for a labeling job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelingJobAlgorithmsConfig) -> dict:
    out: dict = {}
    if "labeling_job_algorithm_specification_arn" in value:
        out["LabelingJobAlgorithmSpecificationArn"] = value[
            "labeling_job_algorithm_specification_arn"
        ]
    if "initial_active_learning_model_arn" in value:
        out["InitialActiveLearningModelArn"] = value[
            "initial_active_learning_model_arn"
        ]
    if "labeling_job_resource_config" in value:
        import aws_sdk_sagemaker.types.labeling_job_resource_config

        out["LabelingJobResourceConfig"] = (
            aws_sdk_sagemaker.types.labeling_job_resource_config.serialize_aws_json_1_1(
                value["labeling_job_resource_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelingJobAlgorithmsConfig:
    out: LabelingJobAlgorithmsConfig = {}  # type: ignore[typeddict-item]
    if "LabelingJobAlgorithmSpecificationArn" in data:
        out["labeling_job_algorithm_specification_arn"] = data[
            "LabelingJobAlgorithmSpecificationArn"
        ]
    if "InitialActiveLearningModelArn" in data:
        out["initial_active_learning_model_arn"] = data["InitialActiveLearningModelArn"]
    if "LabelingJobResourceConfig" in data:
        import aws_sdk_sagemaker.types.labeling_job_resource_config

        out["labeling_job_resource_config"] = (
            aws_sdk_sagemaker.types.labeling_job_resource_config.deserialize_aws_json_1_1(
                data["LabelingJobResourceConfig"]
            )
        )
    return out
