"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.endpoint_arn
    import aws_sdk_sagemaker.types.endpoint_name
    import aws_sdk_sagemaker.types.inference_component_arn
    import aws_sdk_sagemaker.types.inference_component_name
    import aws_sdk_sagemaker.types.inference_component_status
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.variant_name


class InferenceComponentSummary(TypedDict):
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the inference component was created.</p>"""
    inference_component_arn: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_arn.InferenceComponentArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the inference component.</p>"""
    inference_component_name: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_name.InferenceComponentName"
    ]
    """<p>The name of the inference component.</p>"""
    endpoint_arn: NotRequired["aws_sdk_sagemaker.types.endpoint_arn.EndpointArn"]
    """<p>The Amazon Resource Name (ARN) of the endpoint that hosts the inference component.</p>"""
    endpoint_name: NotRequired["aws_sdk_sagemaker.types.endpoint_name.EndpointName"]
    """<p>The name of the endpoint that hosts the inference component.</p>"""
    variant_name: NotRequired["aws_sdk_sagemaker.types.variant_name.VariantName"]
    """<p>The name of the production variant that hosts the inference component.</p>"""
    inference_component_status: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_status.InferenceComponentStatus"
    ]
    """<p>The status of the inference component.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the inference component was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentSummary) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "inference_component_arn" in value:
        out["InferenceComponentArn"] = value["inference_component_arn"]
    if "inference_component_name" in value:
        out["InferenceComponentName"] = value["inference_component_name"]
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "variant_name" in value:
        out["VariantName"] = value["variant_name"]
    if "inference_component_status" in value:
        import aws_sdk_sagemaker.types.inference_component_status

        out["InferenceComponentStatus"] = (
            aws_sdk_sagemaker.types.inference_component_status.serialize_aws_json_1_1(
                value["inference_component_status"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceComponentSummary:
    out: InferenceComponentSummary = {}  # type: ignore[typeddict-item]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "InferenceComponentArn" in data:
        out["inference_component_arn"] = data["InferenceComponentArn"]
    if "InferenceComponentName" in data:
        out["inference_component_name"] = data["InferenceComponentName"]
    if "EndpointArn" in data:
        out["endpoint_arn"] = data["EndpointArn"]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    if "VariantName" in data:
        out["variant_name"] = data["VariantName"]
    if "InferenceComponentStatus" in data:
        import aws_sdk_sagemaker.types.inference_component_status

        out["inference_component_status"] = (
            aws_sdk_sagemaker.types.inference_component_status.deserialize_aws_json_1_1(
                data["InferenceComponentStatus"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
