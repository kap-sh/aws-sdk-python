"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelBiasJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.batch_transform_input
    import aws_sdk_sagemaker.types.endpoint_input
    import aws_sdk_sagemaker.types.monitoring_ground_truth_s3_input


class ModelBiasJobInput(TypedDict, closed=True):
    endpoint_input: NotRequired["aws_sdk_sagemaker.types.endpoint_input.EndpointInput"]
    batch_transform_input: NotRequired[
        "aws_sdk_sagemaker.types.batch_transform_input.BatchTransformInput"
    ]
    """<p>Input object for the batch transform job.</p>"""
    ground_truth_s3_input: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_ground_truth_s3_input.MonitoringGroundTruthS3Input"
    ]
    """<p>Location of ground truth labels to use in model bias job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelBiasJobInput) -> dict:
    out: dict = {}
    if "endpoint_input" in value:
        import aws_sdk_sagemaker.types.endpoint_input

        out["EndpointInput"] = (
            aws_sdk_sagemaker.types.endpoint_input.serialize_aws_json_1_1(
                value["endpoint_input"]
            )
        )
    if "batch_transform_input" in value:
        import aws_sdk_sagemaker.types.batch_transform_input

        out["BatchTransformInput"] = (
            aws_sdk_sagemaker.types.batch_transform_input.serialize_aws_json_1_1(
                value["batch_transform_input"]
            )
        )
    if "ground_truth_s3_input" in value:
        import aws_sdk_sagemaker.types.monitoring_ground_truth_s3_input

        out["GroundTruthS3Input"] = (
            aws_sdk_sagemaker.types.monitoring_ground_truth_s3_input.serialize_aws_json_1_1(
                value["ground_truth_s3_input"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelBiasJobInput:
    out: ModelBiasJobInput = {}  # type: ignore[typeddict-item]
    if "EndpointInput" in data:
        import aws_sdk_sagemaker.types.endpoint_input

        out["endpoint_input"] = (
            aws_sdk_sagemaker.types.endpoint_input.deserialize_aws_json_1_1(
                data["EndpointInput"]
            )
        )
    if "BatchTransformInput" in data:
        import aws_sdk_sagemaker.types.batch_transform_input

        out["batch_transform_input"] = (
            aws_sdk_sagemaker.types.batch_transform_input.deserialize_aws_json_1_1(
                data["BatchTransformInput"]
            )
        )
    if "GroundTruthS3Input" in data:
        import aws_sdk_sagemaker.types.monitoring_ground_truth_s3_input

        out["ground_truth_s3_input"] = (
            aws_sdk_sagemaker.types.monitoring_ground_truth_s3_input.deserialize_aws_json_1_1(
                data["GroundTruthS3Input"]
            )
        )
    return out
