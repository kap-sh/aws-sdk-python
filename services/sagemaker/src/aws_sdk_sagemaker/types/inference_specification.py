"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.content_types
    import aws_sdk_sagemaker.types.model_package_container_definition_list
    import aws_sdk_sagemaker.types.realtime_inference_instance_types
    import aws_sdk_sagemaker.types.response_mime_types
    import aws_sdk_sagemaker.types.transform_instance_types


class InferenceSpecification(TypedDict):
    containers: NotRequired[
        "aws_sdk_sagemaker.types.model_package_container_definition_list.ModelPackageContainerDefinitionList"
    ]
    """<p>The Amazon ECR registry path of the Docker image that contains the inference code.</p>"""
    supported_transform_instance_types: NotRequired[
        "aws_sdk_sagemaker.types.transform_instance_types.TransformInstanceTypes"
    ]
    """<p>A list of the instance types on which a transformation job can be run or on which an endpoint can be deployed.</p> <p>This parameter is required for unversioned models, and optional for versioned models.</p>"""
    supported_realtime_inference_instance_types: NotRequired[
        "aws_sdk_sagemaker.types.realtime_inference_instance_types.RealtimeInferenceInstanceTypes"
    ]
    """<p>A list of the instance types that are used to generate inferences in real-time.</p> <p>This parameter is required for unversioned models, and optional for versioned models.</p>"""
    supported_content_types: NotRequired[
        "aws_sdk_sagemaker.types.content_types.ContentTypes"
    ]
    """<p>The supported MIME types for the input data.</p>"""
    supported_response_mime_types: NotRequired[
        "aws_sdk_sagemaker.types.response_mime_types.ResponseMIMETypes"
    ]
    """<p>The supported MIME types for the output data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceSpecification) -> dict:
    out: dict = {}
    if "containers" in value:
        import aws_sdk_sagemaker.types.model_package_container_definition_list

        out["Containers"] = (
            aws_sdk_sagemaker.types.model_package_container_definition_list.serialize_aws_json_1_1(
                value["containers"]
            )
        )
    if "supported_transform_instance_types" in value:
        import aws_sdk_sagemaker.types.transform_instance_types

        out["SupportedTransformInstanceTypes"] = (
            aws_sdk_sagemaker.types.transform_instance_types.serialize_aws_json_1_1(
                value["supported_transform_instance_types"]
            )
        )
    if "supported_realtime_inference_instance_types" in value:
        import aws_sdk_sagemaker.types.realtime_inference_instance_types

        out["SupportedRealtimeInferenceInstanceTypes"] = (
            aws_sdk_sagemaker.types.realtime_inference_instance_types.serialize_aws_json_1_1(
                value["supported_realtime_inference_instance_types"]
            )
        )
    if "supported_content_types" in value:
        import aws_sdk_sagemaker.types.content_types

        out["SupportedContentTypes"] = (
            aws_sdk_sagemaker.types.content_types.serialize_aws_json_1_1(
                value["supported_content_types"]
            )
        )
    if "supported_response_mime_types" in value:
        import aws_sdk_sagemaker.types.response_mime_types

        out["SupportedResponseMIMETypes"] = (
            aws_sdk_sagemaker.types.response_mime_types.serialize_aws_json_1_1(
                value["supported_response_mime_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceSpecification:
    out: InferenceSpecification = {}  # type: ignore[typeddict-item]
    if "Containers" in data:
        import aws_sdk_sagemaker.types.model_package_container_definition_list

        out["containers"] = (
            aws_sdk_sagemaker.types.model_package_container_definition_list.deserialize_aws_json_1_1(
                data["Containers"]
            )
        )
    if "SupportedTransformInstanceTypes" in data:
        import aws_sdk_sagemaker.types.transform_instance_types

        out["supported_transform_instance_types"] = (
            aws_sdk_sagemaker.types.transform_instance_types.deserialize_aws_json_1_1(
                data["SupportedTransformInstanceTypes"]
            )
        )
    if "SupportedRealtimeInferenceInstanceTypes" in data:
        import aws_sdk_sagemaker.types.realtime_inference_instance_types

        out["supported_realtime_inference_instance_types"] = (
            aws_sdk_sagemaker.types.realtime_inference_instance_types.deserialize_aws_json_1_1(
                data["SupportedRealtimeInferenceInstanceTypes"]
            )
        )
    if "SupportedContentTypes" in data:
        import aws_sdk_sagemaker.types.content_types

        out["supported_content_types"] = (
            aws_sdk_sagemaker.types.content_types.deserialize_aws_json_1_1(
                data["SupportedContentTypes"]
            )
        )
    if "SupportedResponseMIMETypes" in data:
        import aws_sdk_sagemaker.types.response_mime_types

        out["supported_response_mime_types"] = (
            aws_sdk_sagemaker.types.response_mime_types.deserialize_aws_json_1_1(
                data["SupportedResponseMIMETypes"]
            )
        )
    return out
