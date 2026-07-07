"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubContentInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.document_schema_version
    import aws_sdk_sagemaker.types.hub_content_arn
    import aws_sdk_sagemaker.types.hub_content_description
    import aws_sdk_sagemaker.types.hub_content_display_name
    import aws_sdk_sagemaker.types.hub_content_name
    import aws_sdk_sagemaker.types.hub_content_search_keyword_list
    import aws_sdk_sagemaker.types.hub_content_status
    import aws_sdk_sagemaker.types.hub_content_support_status
    import aws_sdk_sagemaker.types.hub_content_type
    import aws_sdk_sagemaker.types.hub_content_version
    import aws_sdk_sagemaker.types.sage_maker_public_hub_content_arn
    import aws_sdk_sagemaker.types.timestamp


class HubContentInfo(TypedDict, closed=True):
    hub_content_name: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_name.HubContentName"
    ]
    """<p>The name of the hub content.</p>"""
    hub_content_arn: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_arn.HubContentArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the hub content.</p>"""
    sage_maker_public_hub_content_arn: NotRequired[
        "aws_sdk_sagemaker.types.sage_maker_public_hub_content_arn.SageMakerPublicHubContentArn"
    ]
    """<p>The ARN of the public hub content.</p>"""
    hub_content_version: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_version.HubContentVersion"
    ]
    """<p>The version of the hub content.</p>"""
    hub_content_type: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_type.HubContentType"
    ]
    """<p>The type of hub content.</p>"""
    document_schema_version: NotRequired[
        "aws_sdk_sagemaker.types.document_schema_version.DocumentSchemaVersion"
    ]
    """<p>The version of the hub content document schema.</p>"""
    hub_content_display_name: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_display_name.HubContentDisplayName"
    ]
    """<p>The display name of the hub content.</p>"""
    hub_content_description: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_description.HubContentDescription"
    ]
    """<p>A description of the hub content.</p>"""
    support_status: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_support_status.HubContentSupportStatus"
    ]
    """<p>The support status of the hub content.</p>"""
    hub_content_search_keywords: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_search_keyword_list.HubContentSearchKeywordList"
    ]
    """<p>The searchable keywords for the hub content.</p>"""
    hub_content_status: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_status.HubContentStatus"
    ]
    """<p>The status of the hub content.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the hub content was created.</p>"""
    original_creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time when the hub content was originally created, before any updates or revisions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HubContentInfo) -> dict:
    out: dict = {}
    if "hub_content_name" in value:
        out["HubContentName"] = value["hub_content_name"]
    if "hub_content_arn" in value:
        out["HubContentArn"] = value["hub_content_arn"]
    if "sage_maker_public_hub_content_arn" in value:
        out["SageMakerPublicHubContentArn"] = value["sage_maker_public_hub_content_arn"]
    if "hub_content_version" in value:
        out["HubContentVersion"] = value["hub_content_version"]
    if "hub_content_type" in value:
        import aws_sdk_sagemaker.types.hub_content_type

        out["HubContentType"] = (
            aws_sdk_sagemaker.types.hub_content_type.serialize_aws_json_1_1(
                value["hub_content_type"]
            )
        )
    if "document_schema_version" in value:
        out["DocumentSchemaVersion"] = value["document_schema_version"]
    if "hub_content_display_name" in value:
        out["HubContentDisplayName"] = value["hub_content_display_name"]
    if "hub_content_description" in value:
        out["HubContentDescription"] = value["hub_content_description"]
    if "support_status" in value:
        import aws_sdk_sagemaker.types.hub_content_support_status

        out["SupportStatus"] = (
            aws_sdk_sagemaker.types.hub_content_support_status.serialize_aws_json_1_1(
                value["support_status"]
            )
        )
    if "hub_content_search_keywords" in value:
        import aws_sdk_sagemaker.types.hub_content_search_keyword_list

        out["HubContentSearchKeywords"] = (
            aws_sdk_sagemaker.types.hub_content_search_keyword_list.serialize_aws_json_1_1(
                value["hub_content_search_keywords"]
            )
        )
    if "hub_content_status" in value:
        import aws_sdk_sagemaker.types.hub_content_status

        out["HubContentStatus"] = (
            aws_sdk_sagemaker.types.hub_content_status.serialize_aws_json_1_1(
                value["hub_content_status"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "original_creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["OriginalCreationTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["original_creation_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HubContentInfo:
    out: HubContentInfo = {}  # type: ignore[typeddict-item]
    if "HubContentName" in data:
        out["hub_content_name"] = data["HubContentName"]
    if "HubContentArn" in data:
        out["hub_content_arn"] = data["HubContentArn"]
    if "SageMakerPublicHubContentArn" in data:
        out["sage_maker_public_hub_content_arn"] = data["SageMakerPublicHubContentArn"]
    if "HubContentVersion" in data:
        out["hub_content_version"] = data["HubContentVersion"]
    if "HubContentType" in data:
        import aws_sdk_sagemaker.types.hub_content_type

        out["hub_content_type"] = (
            aws_sdk_sagemaker.types.hub_content_type.deserialize_aws_json_1_1(
                data["HubContentType"]
            )
        )
    if "DocumentSchemaVersion" in data:
        out["document_schema_version"] = data["DocumentSchemaVersion"]
    if "HubContentDisplayName" in data:
        out["hub_content_display_name"] = data["HubContentDisplayName"]
    if "HubContentDescription" in data:
        out["hub_content_description"] = data["HubContentDescription"]
    if "SupportStatus" in data:
        import aws_sdk_sagemaker.types.hub_content_support_status

        out["support_status"] = (
            aws_sdk_sagemaker.types.hub_content_support_status.deserialize_aws_json_1_1(
                data["SupportStatus"]
            )
        )
    if "HubContentSearchKeywords" in data:
        import aws_sdk_sagemaker.types.hub_content_search_keyword_list

        out["hub_content_search_keywords"] = (
            aws_sdk_sagemaker.types.hub_content_search_keyword_list.deserialize_aws_json_1_1(
                data["HubContentSearchKeywords"]
            )
        )
    if "HubContentStatus" in data:
        import aws_sdk_sagemaker.types.hub_content_status

        out["hub_content_status"] = (
            aws_sdk_sagemaker.types.hub_content_status.deserialize_aws_json_1_1(
                data["HubContentStatus"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "OriginalCreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["original_creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["OriginalCreationTime"]
            )
        )
    return out
