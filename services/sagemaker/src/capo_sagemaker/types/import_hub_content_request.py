"""Generated from Smithy shape ``com.amazonaws.sagemaker#ImportHubContentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.document_schema_version
    import capo_sagemaker.types.hub_content_description
    import capo_sagemaker.types.hub_content_display_name
    import capo_sagemaker.types.hub_content_document
    import capo_sagemaker.types.hub_content_markdown
    import capo_sagemaker.types.hub_content_name
    import capo_sagemaker.types.hub_content_search_keyword_list
    import capo_sagemaker.types.hub_content_support_status
    import capo_sagemaker.types.hub_content_type
    import capo_sagemaker.types.hub_content_version
    import capo_sagemaker.types.hub_name_or_arn
    import capo_sagemaker.types.tag_list


class ImportHubContentRequest(TypedDict, closed=True):
    hub_content_name: NotRequired[
        "capo_sagemaker.types.hub_content_name.HubContentName"
    ]
    """<p>The name of the hub content to import.</p>"""
    hub_content_version: NotRequired[
        "capo_sagemaker.types.hub_content_version.HubContentVersion"
    ]
    """<p>The version of the hub content to import.</p>"""
    hub_content_type: NotRequired[
        "capo_sagemaker.types.hub_content_type.HubContentType"
    ]
    """<p>The type of hub content to import.</p>"""
    document_schema_version: NotRequired[
        "capo_sagemaker.types.document_schema_version.DocumentSchemaVersion"
    ]
    """<p>The version of the hub content schema to import.</p>"""
    hub_name: NotRequired["capo_sagemaker.types.hub_name_or_arn.HubNameOrArn"]
    """<p>The name of the hub to import content into.</p>"""
    hub_content_display_name: NotRequired[
        "capo_sagemaker.types.hub_content_display_name.HubContentDisplayName"
    ]
    """<p>The display name of the hub content to import.</p>"""
    hub_content_description: NotRequired[
        "capo_sagemaker.types.hub_content_description.HubContentDescription"
    ]
    """<p>A description of the hub content to import.</p>"""
    hub_content_markdown: NotRequired[
        "capo_sagemaker.types.hub_content_markdown.HubContentMarkdown"
    ]
    """<p>A string that provides a description of the hub content. This string can include links, tables, and standard markdown formating.</p>"""
    hub_content_document: NotRequired[
        "capo_sagemaker.types.hub_content_document.HubContentDocument"
    ]
    """<p>The hub content document that describes information about the hub content such as type, associated containers, scripts, and more.</p>"""
    support_status: NotRequired[
        "capo_sagemaker.types.hub_content_support_status.HubContentSupportStatus"
    ]
    """<p>The status of the hub content resource.</p>"""
    hub_content_search_keywords: NotRequired[
        "capo_sagemaker.types.hub_content_search_keyword_list.HubContentSearchKeywordList"
    ]
    """<p>The searchable keywords of the hub content.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>Any tags associated with the hub content.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportHubContentRequest) -> dict:
    out: dict = {}
    if "hub_content_name" in value:
        out["HubContentName"] = value["hub_content_name"]
    if "hub_content_version" in value:
        out["HubContentVersion"] = value["hub_content_version"]
    if "hub_content_type" in value:
        import capo_sagemaker.types.hub_content_type

        out["HubContentType"] = (
            capo_sagemaker.types.hub_content_type.serialize_aws_json_1_1(
                value["hub_content_type"]
            )
        )
    if "document_schema_version" in value:
        out["DocumentSchemaVersion"] = value["document_schema_version"]
    if "hub_name" in value:
        out["HubName"] = value["hub_name"]
    if "hub_content_display_name" in value:
        out["HubContentDisplayName"] = value["hub_content_display_name"]
    if "hub_content_description" in value:
        out["HubContentDescription"] = value["hub_content_description"]
    if "hub_content_markdown" in value:
        out["HubContentMarkdown"] = value["hub_content_markdown"]
    if "hub_content_document" in value:
        out["HubContentDocument"] = value["hub_content_document"]
    if "support_status" in value:
        import capo_sagemaker.types.hub_content_support_status

        out["SupportStatus"] = (
            capo_sagemaker.types.hub_content_support_status.serialize_aws_json_1_1(
                value["support_status"]
            )
        )
    if "hub_content_search_keywords" in value:
        import capo_sagemaker.types.hub_content_search_keyword_list

        out["HubContentSearchKeywords"] = (
            capo_sagemaker.types.hub_content_search_keyword_list.serialize_aws_json_1_1(
                value["hub_content_search_keywords"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportHubContentRequest:
    out: ImportHubContentRequest = {}  # type: ignore[typeddict-item]
    if "HubContentName" in data:
        out["hub_content_name"] = data["HubContentName"]
    if "HubContentVersion" in data:
        out["hub_content_version"] = data["HubContentVersion"]
    if "HubContentType" in data:
        import capo_sagemaker.types.hub_content_type

        out["hub_content_type"] = (
            capo_sagemaker.types.hub_content_type.deserialize_aws_json_1_1(
                data["HubContentType"]
            )
        )
    if "DocumentSchemaVersion" in data:
        out["document_schema_version"] = data["DocumentSchemaVersion"]
    if "HubName" in data:
        out["hub_name"] = data["HubName"]
    if "HubContentDisplayName" in data:
        out["hub_content_display_name"] = data["HubContentDisplayName"]
    if "HubContentDescription" in data:
        out["hub_content_description"] = data["HubContentDescription"]
    if "HubContentMarkdown" in data:
        out["hub_content_markdown"] = data["HubContentMarkdown"]
    if "HubContentDocument" in data:
        out["hub_content_document"] = data["HubContentDocument"]
    if "SupportStatus" in data:
        import capo_sagemaker.types.hub_content_support_status

        out["support_status"] = (
            capo_sagemaker.types.hub_content_support_status.deserialize_aws_json_1_1(
                data["SupportStatus"]
            )
        )
    if "HubContentSearchKeywords" in data:
        import capo_sagemaker.types.hub_content_search_keyword_list

        out["hub_content_search_keywords"] = (
            capo_sagemaker.types.hub_content_search_keyword_list.deserialize_aws_json_1_1(
                data["HubContentSearchKeywords"]
            )
        )
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
