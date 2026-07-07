"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeHubContentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.document_schema_version
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.hub_arn
    import aws_sdk_sagemaker.types.hub_content_arn
    import aws_sdk_sagemaker.types.hub_content_dependency_list
    import aws_sdk_sagemaker.types.hub_content_description
    import aws_sdk_sagemaker.types.hub_content_display_name
    import aws_sdk_sagemaker.types.hub_content_document
    import aws_sdk_sagemaker.types.hub_content_markdown
    import aws_sdk_sagemaker.types.hub_content_name
    import aws_sdk_sagemaker.types.hub_content_search_keyword_list
    import aws_sdk_sagemaker.types.hub_content_status
    import aws_sdk_sagemaker.types.hub_content_support_status
    import aws_sdk_sagemaker.types.hub_content_type
    import aws_sdk_sagemaker.types.hub_content_version
    import aws_sdk_sagemaker.types.hub_name
    import aws_sdk_sagemaker.types.reference_min_version
    import aws_sdk_sagemaker.types.sage_maker_public_hub_content_arn
    import aws_sdk_sagemaker.types.timestamp


class DescribeHubContentResponse(TypedDict, closed=True):
    hub_content_name: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_name.HubContentName"
    ]
    """<p>The name of the hub content.</p>"""
    hub_content_arn: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_arn.HubContentArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the hub content.</p>"""
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
    """<p>The document schema version for the hub content.</p>"""
    hub_name: NotRequired["aws_sdk_sagemaker.types.hub_name.HubName"]
    """<p>The name of the hub that contains the content.</p>"""
    hub_arn: NotRequired["aws_sdk_sagemaker.types.hub_arn.HubArn"]
    """<p>The Amazon Resource Name (ARN) of the hub that contains the content. </p>"""
    hub_content_display_name: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_display_name.HubContentDisplayName"
    ]
    """<p>The display name of the hub content.</p>"""
    hub_content_description: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_description.HubContentDescription"
    ]
    """<p>A description of the hub content.</p>"""
    hub_content_markdown: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_markdown.HubContentMarkdown"
    ]
    """<p>A string that provides a description of the hub content. This string can include links, tables, and standard markdown formating.</p>"""
    hub_content_document: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_document.HubContentDocument"
    ]
    """<p>The hub content document that describes information about the hub content such as type, associated containers, scripts, and more.</p>"""
    sage_maker_public_hub_content_arn: NotRequired[
        "aws_sdk_sagemaker.types.sage_maker_public_hub_content_arn.SageMakerPublicHubContentArn"
    ]
    """<p>The ARN of the public hub content.</p>"""
    reference_min_version: NotRequired[
        "aws_sdk_sagemaker.types.reference_min_version.ReferenceMinVersion"
    ]
    """<p>The minimum version of the hub content.</p>"""
    support_status: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_support_status.HubContentSupportStatus"
    ]
    """<p>The support status of the hub content.</p>"""
    hub_content_search_keywords: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_search_keyword_list.HubContentSearchKeywordList"
    ]
    """<p>The searchable keywords for the hub content.</p>"""
    hub_content_dependencies: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_dependency_list.HubContentDependencyList"
    ]
    """<p>The location of any dependencies that the hub content has, such as scripts, model artifacts, datasets, or notebooks.</p>"""
    hub_content_status: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_status.HubContentStatus"
    ]
    """<p>The status of the hub content.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>The failure reason if importing hub content failed.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that hub content was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The last modified time of the hub content.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeHubContentResponse) -> dict:
    out: dict = {}
    if "hub_content_name" in value:
        out["HubContentName"] = value["hub_content_name"]
    if "hub_content_arn" in value:
        out["HubContentArn"] = value["hub_content_arn"]
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
    if "hub_name" in value:
        out["HubName"] = value["hub_name"]
    if "hub_arn" in value:
        out["HubArn"] = value["hub_arn"]
    if "hub_content_display_name" in value:
        out["HubContentDisplayName"] = value["hub_content_display_name"]
    if "hub_content_description" in value:
        out["HubContentDescription"] = value["hub_content_description"]
    if "hub_content_markdown" in value:
        out["HubContentMarkdown"] = value["hub_content_markdown"]
    if "hub_content_document" in value:
        out["HubContentDocument"] = value["hub_content_document"]
    if "sage_maker_public_hub_content_arn" in value:
        out["SageMakerPublicHubContentArn"] = value["sage_maker_public_hub_content_arn"]
    if "reference_min_version" in value:
        out["ReferenceMinVersion"] = value["reference_min_version"]
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
    if "hub_content_dependencies" in value:
        import aws_sdk_sagemaker.types.hub_content_dependency_list

        out["HubContentDependencies"] = (
            aws_sdk_sagemaker.types.hub_content_dependency_list.serialize_aws_json_1_1(
                value["hub_content_dependencies"]
            )
        )
    if "hub_content_status" in value:
        import aws_sdk_sagemaker.types.hub_content_status

        out["HubContentStatus"] = (
            aws_sdk_sagemaker.types.hub_content_status.serialize_aws_json_1_1(
                value["hub_content_status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeHubContentResponse:
    out: DescribeHubContentResponse = {}  # type: ignore[typeddict-item]
    if "HubContentName" in data:
        out["hub_content_name"] = data["HubContentName"]
    if "HubContentArn" in data:
        out["hub_content_arn"] = data["HubContentArn"]
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
    if "HubName" in data:
        out["hub_name"] = data["HubName"]
    if "HubArn" in data:
        out["hub_arn"] = data["HubArn"]
    if "HubContentDisplayName" in data:
        out["hub_content_display_name"] = data["HubContentDisplayName"]
    if "HubContentDescription" in data:
        out["hub_content_description"] = data["HubContentDescription"]
    if "HubContentMarkdown" in data:
        out["hub_content_markdown"] = data["HubContentMarkdown"]
    if "HubContentDocument" in data:
        out["hub_content_document"] = data["HubContentDocument"]
    if "SageMakerPublicHubContentArn" in data:
        out["sage_maker_public_hub_content_arn"] = data["SageMakerPublicHubContentArn"]
    if "ReferenceMinVersion" in data:
        out["reference_min_version"] = data["ReferenceMinVersion"]
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
    if "HubContentDependencies" in data:
        import aws_sdk_sagemaker.types.hub_content_dependency_list

        out["hub_content_dependencies"] = (
            aws_sdk_sagemaker.types.hub_content_dependency_list.deserialize_aws_json_1_1(
                data["HubContentDependencies"]
            )
        )
    if "HubContentStatus" in data:
        import aws_sdk_sagemaker.types.hub_content_status

        out["hub_content_status"] = (
            aws_sdk_sagemaker.types.hub_content_status.deserialize_aws_json_1_1(
                data["HubContentStatus"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
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
