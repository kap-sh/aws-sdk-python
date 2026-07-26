"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelQualityJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.batch_transform_input
    import capo_sagemaker.types.endpoint_input
    import capo_sagemaker.types.monitoring_ground_truth_s3_input


class ModelQualityJobInput(TypedDict, closed=True):
    endpoint_input: NotRequired["capo_sagemaker.types.endpoint_input.EndpointInput"]
    batch_transform_input: NotRequired[
        "capo_sagemaker.types.batch_transform_input.BatchTransformInput"
    ]
    """<p>Input object for the batch transform job.</p>"""
    ground_truth_s3_input: NotRequired[
        "capo_sagemaker.types.monitoring_ground_truth_s3_input.MonitoringGroundTruthS3Input"
    ]
    """<p>The ground truth label provided for the model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelQualityJobInput) -> dict:
    out: dict = {}
    if "endpoint_input" in value:
        import capo_sagemaker.types.endpoint_input

        out["EndpointInput"] = (
            capo_sagemaker.types.endpoint_input.serialize_aws_json_1_1(
                value["endpoint_input"]
            )
        )
    if "batch_transform_input" in value:
        import capo_sagemaker.types.batch_transform_input

        out["BatchTransformInput"] = (
            capo_sagemaker.types.batch_transform_input.serialize_aws_json_1_1(
                value["batch_transform_input"]
            )
        )
    if "ground_truth_s3_input" in value:
        import capo_sagemaker.types.monitoring_ground_truth_s3_input

        out["GroundTruthS3Input"] = (
            capo_sagemaker.types.monitoring_ground_truth_s3_input.serialize_aws_json_1_1(
                value["ground_truth_s3_input"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelQualityJobInput:
    out: ModelQualityJobInput = {}  # type: ignore[typeddict-item]
    if "EndpointInput" in data:
        import capo_sagemaker.types.endpoint_input

        out["endpoint_input"] = (
            capo_sagemaker.types.endpoint_input.deserialize_aws_json_1_1(
                data["EndpointInput"]
            )
        )
    if "BatchTransformInput" in data:
        import capo_sagemaker.types.batch_transform_input

        out["batch_transform_input"] = (
            capo_sagemaker.types.batch_transform_input.deserialize_aws_json_1_1(
                data["BatchTransformInput"]
            )
        )
    if "GroundTruthS3Input" in data:
        import capo_sagemaker.types.monitoring_ground_truth_s3_input

        out["ground_truth_s3_input"] = (
            capo_sagemaker.types.monitoring_ground_truth_s3_input.deserialize_aws_json_1_1(
                data["GroundTruthS3Input"]
            )
        )
    return out
