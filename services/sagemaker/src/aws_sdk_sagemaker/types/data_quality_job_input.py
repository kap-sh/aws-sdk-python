"""Generated from Smithy shape ``com.amazonaws.sagemaker#DataQualityJobInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.batch_transform_input
    import aws_sdk_sagemaker.types.endpoint_input


class DataQualityJobInput(TypedDict):
    endpoint_input: NotRequired["aws_sdk_sagemaker.types.endpoint_input.EndpointInput"]
    batch_transform_input: NotRequired[
        "aws_sdk_sagemaker.types.batch_transform_input.BatchTransformInput"
    ]
    """<p>Input object for the batch transform job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityJobInput) -> dict:
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
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityJobInput:
    out: DataQualityJobInput = {}  # type: ignore[typeddict-item]
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
    return out
