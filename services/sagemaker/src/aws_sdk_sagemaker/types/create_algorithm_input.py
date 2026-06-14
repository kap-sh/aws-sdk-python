"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateAlgorithmInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.algorithm_validation_specification
    import aws_sdk_sagemaker.types.certify_for_marketplace
    import aws_sdk_sagemaker.types.entity_description
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.inference_specification
    import aws_sdk_sagemaker.types.tag_list
    import aws_sdk_sagemaker.types.training_specification


class CreateAlgorithmInput(TypedDict):
    algorithm_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the algorithm.</p>"""
    algorithm_description: NotRequired[
        "aws_sdk_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>A description of the algorithm.</p>"""
    training_specification: NotRequired[
        "aws_sdk_sagemaker.types.training_specification.TrainingSpecification"
    ]
    """<p>Specifies details about training jobs run by this algorithm, including the following:</p> <ul> <li> <p>The Amazon ECR path of the container and the version digest of the algorithm.</p> </li> <li> <p>The hyperparameters that the algorithm supports.</p> </li> <li> <p>The instance types that the algorithm supports for training.</p> </li> <li> <p>Whether the algorithm supports distributed training.</p> </li> <li> <p>The metrics that the algorithm emits to Amazon CloudWatch.</p> </li> <li> <p>Which metrics that the algorithm emits can be used as the objective metric for hyperparameter tuning jobs.</p> </li> <li> <p>The input channels that the algorithm supports for training data. For example, an algorithm might support <code>train</code>, <code>validation</code>, and <code>test</code> channels.</p> </li> </ul>"""
    inference_specification: NotRequired[
        "aws_sdk_sagemaker.types.inference_specification.InferenceSpecification"
    ]
    """<p>Specifies details about inference jobs that the algorithm runs, including the following:</p> <ul> <li> <p>The Amazon ECR paths of containers that contain the inference code and model artifacts.</p> </li> <li> <p>The instance types that the algorithm supports for transform jobs and real-time endpoints used for inference.</p> </li> <li> <p>The input and output content formats that the algorithm supports for inference.</p> </li> </ul>"""
    validation_specification: NotRequired[
        "aws_sdk_sagemaker.types.algorithm_validation_specification.AlgorithmValidationSpecification"
    ]
    """<p>Specifies configurations for one or more training jobs and that SageMaker runs to test the algorithm's training code and, optionally, one or more batch transform jobs that SageMaker runs to test the algorithm's inference code.</p>"""
    certify_for_marketplace: NotRequired[
        "aws_sdk_sagemaker.types.certify_for_marketplace.CertifyForMarketplace"
    ]
    """<p>Whether to certify the algorithm so that it can be listed in Amazon Web Services Marketplace.</p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    r"""<p>An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services Resources</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAlgorithmInput) -> dict:
    out: dict = {}
    if "algorithm_name" in value:
        out["AlgorithmName"] = value["algorithm_name"]
    if "algorithm_description" in value:
        out["AlgorithmDescription"] = value["algorithm_description"]
    if "training_specification" in value:
        import aws_sdk_sagemaker.types.training_specification

        out["TrainingSpecification"] = (
            aws_sdk_sagemaker.types.training_specification.serialize_aws_json_1_1(
                value["training_specification"]
            )
        )
    if "inference_specification" in value:
        import aws_sdk_sagemaker.types.inference_specification

        out["InferenceSpecification"] = (
            aws_sdk_sagemaker.types.inference_specification.serialize_aws_json_1_1(
                value["inference_specification"]
            )
        )
    if "validation_specification" in value:
        import aws_sdk_sagemaker.types.algorithm_validation_specification

        out["ValidationSpecification"] = (
            aws_sdk_sagemaker.types.algorithm_validation_specification.serialize_aws_json_1_1(
                value["validation_specification"]
            )
        )
    if "certify_for_marketplace" in value:
        out["CertifyForMarketplace"] = value["certify_for_marketplace"]
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAlgorithmInput:
    out: CreateAlgorithmInput = {}  # type: ignore[typeddict-item]
    if "AlgorithmName" in data:
        out["algorithm_name"] = data["AlgorithmName"]
    if "AlgorithmDescription" in data:
        out["algorithm_description"] = data["AlgorithmDescription"]
    if "TrainingSpecification" in data:
        import aws_sdk_sagemaker.types.training_specification

        out["training_specification"] = (
            aws_sdk_sagemaker.types.training_specification.deserialize_aws_json_1_1(
                data["TrainingSpecification"]
            )
        )
    if "InferenceSpecification" in data:
        import aws_sdk_sagemaker.types.inference_specification

        out["inference_specification"] = (
            aws_sdk_sagemaker.types.inference_specification.deserialize_aws_json_1_1(
                data["InferenceSpecification"]
            )
        )
    if "ValidationSpecification" in data:
        import aws_sdk_sagemaker.types.algorithm_validation_specification

        out["validation_specification"] = (
            aws_sdk_sagemaker.types.algorithm_validation_specification.deserialize_aws_json_1_1(
                data["ValidationSpecification"]
            )
        )
    if "CertifyForMarketplace" in data:
        out["certify_for_marketplace"] = data["CertifyForMarketplace"]
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
