"""Generated from Smithy shape ``com.amazonaws.sagemaker#AdditionalInferenceSpecificationDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.content_types
    import capo_sagemaker.types.entity_description
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.model_package_container_definition_list
    import capo_sagemaker.types.realtime_inference_instance_types
    import capo_sagemaker.types.response_mime_types
    import capo_sagemaker.types.transform_instance_types


class AdditionalInferenceSpecificationDefinition(TypedDict, closed=True):
    name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>A unique name to identify the additional inference specification. The name must be unique within the list of your additional inference specifications for a particular model package.</p>"""
    description: NotRequired[
        "capo_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>A description of the additional Inference specification</p>"""
    containers: NotRequired[
        "capo_sagemaker.types.model_package_container_definition_list.ModelPackageContainerDefinitionList"
    ]
    """<p>The Amazon ECR registry path of the Docker image that contains the inference code.</p>"""
    supported_transform_instance_types: NotRequired[
        "capo_sagemaker.types.transform_instance_types.TransformInstanceTypes"
    ]
    """<p>A list of the instance types on which a transformation job can be run or on which an endpoint can be deployed.</p>"""
    supported_realtime_inference_instance_types: NotRequired[
        "capo_sagemaker.types.realtime_inference_instance_types.RealtimeInferenceInstanceTypes"
    ]
    """<p>A list of the instance types that are used to generate inferences in real-time.</p>"""
    supported_content_types: NotRequired[
        "capo_sagemaker.types.content_types.ContentTypes"
    ]
    """<p>The supported MIME types for the input data.</p>"""
    supported_response_mime_types: NotRequired[
        "capo_sagemaker.types.response_mime_types.ResponseMIMETypes"
    ]
    """<p>The supported MIME types for the output data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalInferenceSpecificationDefinition) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "containers" in value:
        import capo_sagemaker.types.model_package_container_definition_list

        out["Containers"] = (
            capo_sagemaker.types.model_package_container_definition_list.serialize_aws_json_1_1(
                value["containers"]
            )
        )
    if "supported_transform_instance_types" in value:
        import capo_sagemaker.types.transform_instance_types

        out["SupportedTransformInstanceTypes"] = (
            capo_sagemaker.types.transform_instance_types.serialize_aws_json_1_1(
                value["supported_transform_instance_types"]
            )
        )
    if "supported_realtime_inference_instance_types" in value:
        import capo_sagemaker.types.realtime_inference_instance_types

        out["SupportedRealtimeInferenceInstanceTypes"] = (
            capo_sagemaker.types.realtime_inference_instance_types.serialize_aws_json_1_1(
                value["supported_realtime_inference_instance_types"]
            )
        )
    if "supported_content_types" in value:
        import capo_sagemaker.types.content_types

        out["SupportedContentTypes"] = (
            capo_sagemaker.types.content_types.serialize_aws_json_1_1(
                value["supported_content_types"]
            )
        )
    if "supported_response_mime_types" in value:
        import capo_sagemaker.types.response_mime_types

        out["SupportedResponseMIMETypes"] = (
            capo_sagemaker.types.response_mime_types.serialize_aws_json_1_1(
                value["supported_response_mime_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdditionalInferenceSpecificationDefinition:
    out: AdditionalInferenceSpecificationDefinition = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Containers" in data:
        import capo_sagemaker.types.model_package_container_definition_list

        out["containers"] = (
            capo_sagemaker.types.model_package_container_definition_list.deserialize_aws_json_1_1(
                data["Containers"]
            )
        )
    if "SupportedTransformInstanceTypes" in data:
        import capo_sagemaker.types.transform_instance_types

        out["supported_transform_instance_types"] = (
            capo_sagemaker.types.transform_instance_types.deserialize_aws_json_1_1(
                data["SupportedTransformInstanceTypes"]
            )
        )
    if "SupportedRealtimeInferenceInstanceTypes" in data:
        import capo_sagemaker.types.realtime_inference_instance_types

        out["supported_realtime_inference_instance_types"] = (
            capo_sagemaker.types.realtime_inference_instance_types.deserialize_aws_json_1_1(
                data["SupportedRealtimeInferenceInstanceTypes"]
            )
        )
    if "SupportedContentTypes" in data:
        import capo_sagemaker.types.content_types

        out["supported_content_types"] = (
            capo_sagemaker.types.content_types.deserialize_aws_json_1_1(
                data["SupportedContentTypes"]
            )
        )
    if "SupportedResponseMIMETypes" in data:
        import capo_sagemaker.types.response_mime_types

        out["supported_response_mime_types"] = (
            capo_sagemaker.types.response_mime_types.deserialize_aws_json_1_1(
                data["SupportedResponseMIMETypes"]
            )
        )
    return out
