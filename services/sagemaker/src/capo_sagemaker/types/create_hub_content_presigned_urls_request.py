"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateHubContentPresignedUrlsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.hub_content_name
    import capo_sagemaker.types.hub_content_type
    import capo_sagemaker.types.hub_content_version
    import capo_sagemaker.types.hub_name_or_arn
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.presigned_url_access_config


class CreateHubContentPresignedUrlsRequest(TypedDict, closed=True):
    hub_name: NotRequired["capo_sagemaker.types.hub_name_or_arn.HubNameOrArn"]
    """<p>The name or Amazon Resource Name (ARN) of the hub that contains the content. For public content, use <code>SageMakerPublicHub</code>.</p>"""
    hub_content_type: NotRequired[
        "capo_sagemaker.types.hub_content_type.HubContentType"
    ]
    """<p>The type of hub content to access. Valid values include <code>Model</code>, <code>Notebook</code>, and <code>ModelReference</code>.</p>"""
    hub_content_name: NotRequired[
        "capo_sagemaker.types.hub_content_name.HubContentName"
    ]
    """<p>The name of the hub content for which to generate presigned URLs. This identifies the specific model or content within the hub.</p>"""
    hub_content_version: NotRequired[
        "capo_sagemaker.types.hub_content_version.HubContentVersion"
    ]
    """<p>The version of the hub content. If not specified, the latest version is used.</p>"""
    access_config: NotRequired[
        "capo_sagemaker.types.presigned_url_access_config.PresignedUrlAccessConfig"
    ]
    """<p>Configuration settings for accessing the hub content, including end-user license agreement acceptance for gated models and expected S3 URL validation.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of presigned URLs to return in the response. Default value is 100. Large models may contain hundreds of files, requiring pagination to retrieve all URLs.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p> A token for pagination. Use this token to retrieve the next set of presigned URLs when the response is truncated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHubContentPresignedUrlsRequest) -> dict:
    out: dict = {}
    if "hub_name" in value:
        out["HubName"] = value["hub_name"]
    if "hub_content_type" in value:
        import capo_sagemaker.types.hub_content_type

        out["HubContentType"] = (
            capo_sagemaker.types.hub_content_type.serialize_aws_json_1_1(
                value["hub_content_type"]
            )
        )
    if "hub_content_name" in value:
        out["HubContentName"] = value["hub_content_name"]
    if "hub_content_version" in value:
        out["HubContentVersion"] = value["hub_content_version"]
    if "access_config" in value:
        import capo_sagemaker.types.presigned_url_access_config

        out["AccessConfig"] = (
            capo_sagemaker.types.presigned_url_access_config.serialize_aws_json_1_1(
                value["access_config"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHubContentPresignedUrlsRequest:
    out: CreateHubContentPresignedUrlsRequest = {}  # type: ignore[typeddict-item]
    if "HubName" in data:
        out["hub_name"] = data["HubName"]
    if "HubContentType" in data:
        import capo_sagemaker.types.hub_content_type

        out["hub_content_type"] = (
            capo_sagemaker.types.hub_content_type.deserialize_aws_json_1_1(
                data["HubContentType"]
            )
        )
    if "HubContentName" in data:
        out["hub_content_name"] = data["HubContentName"]
    if "HubContentVersion" in data:
        out["hub_content_version"] = data["HubContentVersion"]
    if "AccessConfig" in data:
        import capo_sagemaker.types.presigned_url_access_config

        out["access_config"] = (
            capo_sagemaker.types.presigned_url_access_config.deserialize_aws_json_1_1(
                data["AccessConfig"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
