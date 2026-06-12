"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateHubContentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hub_content_description
    import aws_sdk_sagemaker.types.hub_content_display_name
    import aws_sdk_sagemaker.types.hub_content_markdown
    import aws_sdk_sagemaker.types.hub_content_name
    import aws_sdk_sagemaker.types.hub_content_search_keyword_list
    import aws_sdk_sagemaker.types.hub_content_support_status
    import aws_sdk_sagemaker.types.hub_content_type
    import aws_sdk_sagemaker.types.hub_content_version
    import aws_sdk_sagemaker.types.hub_name_or_arn


class UpdateHubContentRequest(TypedDict):
    hub_name: NotRequired["aws_sdk_sagemaker.types.hub_name_or_arn.HubNameOrArn"]
    """<p>The name of the SageMaker hub that contains the hub content you want to update. You can optionally use the hub ARN instead.</p>"""
    hub_content_name: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_name.HubContentName"
    ]
    """<p>The name of the hub content resource that you want to update.</p>"""
    hub_content_type: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_type.HubContentType"
    ]
    """<p>The content type of the resource that you want to update. Only specify a <code>Model</code> or <code>Notebook</code> resource for this API. To update a <code>ModelReference</code>, use the <code>UpdateHubContentReference</code> API instead.</p>"""
    hub_content_version: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_version.HubContentVersion"
    ]
    """<p>The hub content version that you want to update. For example, if you have two versions of a resource in your hub, you can update the second version.</p>"""
    hub_content_display_name: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_display_name.HubContentDisplayName"
    ]
    """<p>The display name of the hub content.</p>"""
    hub_content_description: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_description.HubContentDescription"
    ]
    """<p>The description of the hub content.</p>"""
    hub_content_markdown: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_markdown.HubContentMarkdown"
    ]
    """<p>A string that provides a description of the hub content. This string can include links, tables, and standard markdown formatting.</p>"""
    hub_content_search_keywords: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_search_keyword_list.HubContentSearchKeywordList"
    ]
    """<p>The searchable keywords of the hub content.</p>"""
    support_status: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_support_status.HubContentSupportStatus"
    ]
    """<p>Indicates the current status of the hub content resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateHubContentRequest) -> dict:
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
    if "hub_content_version" in value:
        out["HubContentVersion"] = value["hub_content_version"]
    if "hub_content_display_name" in value:
        out["HubContentDisplayName"] = value["hub_content_display_name"]
    if "hub_content_description" in value:
        out["HubContentDescription"] = value["hub_content_description"]
    if "hub_content_markdown" in value:
        out["HubContentMarkdown"] = value["hub_content_markdown"]
    if "hub_content_search_keywords" in value:
        import aws_sdk_sagemaker.types.hub_content_search_keyword_list

        out["HubContentSearchKeywords"] = (
            aws_sdk_sagemaker.types.hub_content_search_keyword_list.serialize_aws_json_1_1(
                value["hub_content_search_keywords"]
            )
        )
    if "support_status" in value:
        import aws_sdk_sagemaker.types.hub_content_support_status

        out["SupportStatus"] = (
            aws_sdk_sagemaker.types.hub_content_support_status.serialize_aws_json_1_1(
                value["support_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateHubContentRequest:
    out: UpdateHubContentRequest = {}  # type: ignore[typeddict-item]
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
    if "HubContentVersion" in data:
        out["hub_content_version"] = data["HubContentVersion"]
    if "HubContentDisplayName" in data:
        out["hub_content_display_name"] = data["HubContentDisplayName"]
    if "HubContentDescription" in data:
        out["hub_content_description"] = data["HubContentDescription"]
    if "HubContentMarkdown" in data:
        out["hub_content_markdown"] = data["HubContentMarkdown"]
    if "HubContentSearchKeywords" in data:
        import aws_sdk_sagemaker.types.hub_content_search_keyword_list

        out["hub_content_search_keywords"] = (
            aws_sdk_sagemaker.types.hub_content_search_keyword_list.deserialize_aws_json_1_1(
                data["HubContentSearchKeywords"]
            )
        )
    if "SupportStatus" in data:
        import aws_sdk_sagemaker.types.hub_content_support_status

        out["support_status"] = (
            aws_sdk_sagemaker.types.hub_content_support_status.deserialize_aws_json_1_1(
                data["SupportStatus"]
            )
        )
    return out
