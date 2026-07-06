"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateDocumentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.attachments_source_list
    import aws_sdk_ssm.types.document_content
    import aws_sdk_ssm.types.document_display_name
    import aws_sdk_ssm.types.document_format
    import aws_sdk_ssm.types.document_name
    import aws_sdk_ssm.types.document_version
    import aws_sdk_ssm.types.document_version_name
    import aws_sdk_ssm.types.target_type


class UpdateDocumentRequest(TypedDict, closed=True):
    content: "aws_sdk_ssm.types.document_content.DocumentContent"
    """<p>A valid JSON or YAML string.</p>"""
    attachments: NotRequired[
        "aws_sdk_ssm.types.attachments_source_list.AttachmentsSourceList"
    ]
    """<p>A list of key-value pairs that describe attachments to a version of a document.</p>"""
    name: "aws_sdk_ssm.types.document_name.DocumentName"
    """<p>The name of the SSM document that you want to update.</p>"""
    display_name: NotRequired[
        "aws_sdk_ssm.types.document_display_name.DocumentDisplayName"
    ]
    """<p>The friendly name of the SSM document that you want to update. This value can differ for each version of the document. If you don't specify a value for this parameter in your request, the existing value is applied to the new document version.</p>"""
    version_name: NotRequired[
        "aws_sdk_ssm.types.document_version_name.DocumentVersionName"
    ]
    """<p>An optional field specifying the version of the artifact you are updating with the document. For example, 12.6. This value is unique across all versions of a document, and can't be changed.</p>"""
    document_version: NotRequired["aws_sdk_ssm.types.document_version.DocumentVersion"]
    """<p>The version of the document that you want to update. Currently, Systems Manager supports updating only the latest version of the document. You can specify the version number of the latest version or use the <code>$LATEST</code> variable.</p> <note> <p>If you change a document version for a State Manager association, Systems Manager immediately runs the association unless you previously specifed the <code>apply-only-at-cron-interval</code> parameter.</p> </note>"""
    document_format: NotRequired["aws_sdk_ssm.types.document_format.DocumentFormat"]
    """<p>Specify the document format for the new document version. Systems Manager supports JSON and YAML documents. JSON is the default format.</p>"""
    target_type: NotRequired["aws_sdk_ssm.types.target_type.TargetType"]
    """<p>Specify a new target type for the document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDocumentRequest) -> dict:
    out: dict = {}
    out["Content"] = value["content"]
    if "attachments" in value:
        import aws_sdk_ssm.types.attachments_source_list

        out["Attachments"] = (
            aws_sdk_ssm.types.attachments_source_list.serialize_aws_json_1_1(
                value["attachments"]
            )
        )
    out["Name"] = value["name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "version_name" in value:
        out["VersionName"] = value["version_name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "document_format" in value:
        import aws_sdk_ssm.types.document_format

        out["DocumentFormat"] = (
            aws_sdk_ssm.types.document_format.serialize_aws_json_1_1(
                value["document_format"]
            )
        )
    if "target_type" in value:
        out["TargetType"] = value["target_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDocumentRequest:
    out: UpdateDocumentRequest = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("UpdateDocumentRequest.content required")
    if "Attachments" in data:
        import aws_sdk_ssm.types.attachments_source_list

        out["attachments"] = (
            aws_sdk_ssm.types.attachments_source_list.deserialize_aws_json_1_1(
                data["Attachments"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateDocumentRequest.name required")
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "VersionName" in data:
        out["version_name"] = data["VersionName"]
    if "DocumentVersion" in data:
        out["document_version"] = data["DocumentVersion"]
    if "DocumentFormat" in data:
        import aws_sdk_ssm.types.document_format

        out["document_format"] = (
            aws_sdk_ssm.types.document_format.deserialize_aws_json_1_1(
                data["DocumentFormat"]
            )
        )
    if "TargetType" in data:
        out["target_type"] = data["TargetType"]
    return out
