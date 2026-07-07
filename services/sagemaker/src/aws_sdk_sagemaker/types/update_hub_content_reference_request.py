"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateHubContentReferenceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hub_content_name
    import aws_sdk_sagemaker.types.hub_content_type
    import aws_sdk_sagemaker.types.hub_content_version
    import aws_sdk_sagemaker.types.hub_name_or_arn


class UpdateHubContentReferenceRequest(TypedDict, closed=True):
    hub_name: NotRequired["aws_sdk_sagemaker.types.hub_name_or_arn.HubNameOrArn"]
    """<p>The name of the SageMaker hub that contains the hub content you want to update. You can optionally use the hub ARN instead.</p>"""
    hub_content_name: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_name.HubContentName"
    ]
    """<p>The name of the hub content resource that you want to update.</p>"""
    hub_content_type: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_type.HubContentType"
    ]
    """<p>The content type of the resource that you want to update. Only specify a <code>ModelReference</code> resource for this API. To update a <code>Model</code> or <code>Notebook</code> resource, use the <code>UpdateHubContent</code> API instead.</p>"""
    min_version: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_version.HubContentVersion"
    ]
    """<p>The minimum hub content version of the referenced model that you want to use. The minimum version must be older than the latest available version of the referenced model. To support all versions of a model, set the value to <code>1.0.0</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateHubContentReferenceRequest) -> dict:
    out: dict = {}
    if "hub_name" in value:
        out["HubName"] = value["hub_name"]
    if "hub_content_name" in value:
        out["HubContentName"] = value["hub_content_name"]
    if "hub_content_type" in value:
        import aws_sdk_sagemaker.types.hub_content_type

        out["HubContentType"] = (
            aws_sdk_sagemaker.types.hub_content_type.serialize_aws_json_1_1(
                value["hub_content_type"]
            )
        )
    if "min_version" in value:
        out["MinVersion"] = value["min_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateHubContentReferenceRequest:
    out: UpdateHubContentReferenceRequest = {}  # type: ignore[typeddict-item]
    if "HubName" in data:
        out["hub_name"] = data["HubName"]
    if "HubContentName" in data:
        out["hub_content_name"] = data["HubContentName"]
    if "HubContentType" in data:
        import aws_sdk_sagemaker.types.hub_content_type

        out["hub_content_type"] = (
            aws_sdk_sagemaker.types.hub_content_type.deserialize_aws_json_1_1(
                data["HubContentType"]
            )
        )
    if "MinVersion" in data:
        out["min_version"] = data["MinVersion"]
    return out
