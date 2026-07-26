"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeAlgorithmOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.algorithm_arn
    import capo_sagemaker.types.algorithm_status
    import capo_sagemaker.types.algorithm_status_details
    import capo_sagemaker.types.algorithm_validation_specification
    import capo_sagemaker.types.certify_for_marketplace
    import capo_sagemaker.types.creation_time
    import capo_sagemaker.types.entity_description
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.inference_specification
    import capo_sagemaker.types.product_id
    import capo_sagemaker.types.training_specification


class DescribeAlgorithmOutput(TypedDict, closed=True):
    algorithm_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the algorithm being described.</p>"""
    algorithm_arn: NotRequired["capo_sagemaker.types.algorithm_arn.AlgorithmArn"]
    """<p>The Amazon Resource Name (ARN) of the algorithm.</p>"""
    algorithm_description: NotRequired[
        "capo_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>A brief summary about the algorithm.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>A timestamp specifying when the algorithm was created.</p>"""
    training_specification: NotRequired[
        "capo_sagemaker.types.training_specification.TrainingSpecification"
    ]
    """<p>Details about training jobs run by this algorithm.</p>"""
    inference_specification: NotRequired[
        "capo_sagemaker.types.inference_specification.InferenceSpecification"
    ]
    """<p>Details about inference jobs that the algorithm runs.</p>"""
    validation_specification: NotRequired[
        "capo_sagemaker.types.algorithm_validation_specification.AlgorithmValidationSpecification"
    ]
    """<p>Details about configurations for one or more training jobs that SageMaker runs to test the algorithm.</p>"""
    algorithm_status: NotRequired[
        "capo_sagemaker.types.algorithm_status.AlgorithmStatus"
    ]
    """<p>The current status of the algorithm.</p>"""
    algorithm_status_details: NotRequired[
        "capo_sagemaker.types.algorithm_status_details.AlgorithmStatusDetails"
    ]
    """<p>Details about the current status of the algorithm.</p>"""
    product_id: NotRequired["capo_sagemaker.types.product_id.ProductId"]
    """<p>The product identifier of the algorithm.</p>"""
    certify_for_marketplace: NotRequired[
        "capo_sagemaker.types.certify_for_marketplace.CertifyForMarketplace"
    ]
    """<p>Whether the algorithm is certified to be listed in Amazon Web Services Marketplace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAlgorithmOutput) -> dict:
    out: dict = {}
    if "algorithm_name" in value:
        out["AlgorithmName"] = value["algorithm_name"]
    if "algorithm_arn" in value:
        out["AlgorithmArn"] = value["algorithm_arn"]
    if "algorithm_description" in value:
        out["AlgorithmDescription"] = value["algorithm_description"]
    if "creation_time" in value:
        import capo_sagemaker.types.creation_time

        out["CreationTime"] = capo_sagemaker.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "training_specification" in value:
        import capo_sagemaker.types.training_specification

        out["TrainingSpecification"] = (
            capo_sagemaker.types.training_specification.serialize_aws_json_1_1(
                value["training_specification"]
            )
        )
    if "inference_specification" in value:
        import capo_sagemaker.types.inference_specification

        out["InferenceSpecification"] = (
            capo_sagemaker.types.inference_specification.serialize_aws_json_1_1(
                value["inference_specification"]
            )
        )
    if "validation_specification" in value:
        import capo_sagemaker.types.algorithm_validation_specification

        out["ValidationSpecification"] = (
            capo_sagemaker.types.algorithm_validation_specification.serialize_aws_json_1_1(
                value["validation_specification"]
            )
        )
    if "algorithm_status" in value:
        import capo_sagemaker.types.algorithm_status

        out["AlgorithmStatus"] = (
            capo_sagemaker.types.algorithm_status.serialize_aws_json_1_1(
                value["algorithm_status"]
            )
        )
    if "algorithm_status_details" in value:
        import capo_sagemaker.types.algorithm_status_details

        out["AlgorithmStatusDetails"] = (
            capo_sagemaker.types.algorithm_status_details.serialize_aws_json_1_1(
                value["algorithm_status_details"]
            )
        )
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "certify_for_marketplace" in value:
        out["CertifyForMarketplace"] = value["certify_for_marketplace"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAlgorithmOutput:
    out: DescribeAlgorithmOutput = {}  # type: ignore[typeddict-item]
    if "AlgorithmName" in data:
        out["algorithm_name"] = data["AlgorithmName"]
    if "AlgorithmArn" in data:
        out["algorithm_arn"] = data["AlgorithmArn"]
    if "AlgorithmDescription" in data:
        out["algorithm_description"] = data["AlgorithmDescription"]
    if "CreationTime" in data:
        import capo_sagemaker.types.creation_time

        out["creation_time"] = (
            capo_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "TrainingSpecification" in data:
        import capo_sagemaker.types.training_specification

        out["training_specification"] = (
            capo_sagemaker.types.training_specification.deserialize_aws_json_1_1(
                data["TrainingSpecification"]
            )
        )
    if "InferenceSpecification" in data:
        import capo_sagemaker.types.inference_specification

        out["inference_specification"] = (
            capo_sagemaker.types.inference_specification.deserialize_aws_json_1_1(
                data["InferenceSpecification"]
            )
        )
    if "ValidationSpecification" in data:
        import capo_sagemaker.types.algorithm_validation_specification

        out["validation_specification"] = (
            capo_sagemaker.types.algorithm_validation_specification.deserialize_aws_json_1_1(
                data["ValidationSpecification"]
            )
        )
    if "AlgorithmStatus" in data:
        import capo_sagemaker.types.algorithm_status

        out["algorithm_status"] = (
            capo_sagemaker.types.algorithm_status.deserialize_aws_json_1_1(
                data["AlgorithmStatus"]
            )
        )
    if "AlgorithmStatusDetails" in data:
        import capo_sagemaker.types.algorithm_status_details

        out["algorithm_status_details"] = (
            capo_sagemaker.types.algorithm_status_details.deserialize_aws_json_1_1(
                data["AlgorithmStatusDetails"]
            )
        )
    if "ProductId" in data:
        out["product_id"] = data["ProductId"]
    if "CertifyForMarketplace" in data:
        out["certify_for_marketplace"] = data["CertifyForMarketplace"]
    return out
