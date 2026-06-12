"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentVersionInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.boolean
    import aws_sdk_ssm.types.date_time
    import aws_sdk_ssm.types.document_display_name
    import aws_sdk_ssm.types.document_format
    import aws_sdk_ssm.types.document_name
    import aws_sdk_ssm.types.document_status
    import aws_sdk_ssm.types.document_status_information
    import aws_sdk_ssm.types.document_version
    import aws_sdk_ssm.types.document_version_name
    import aws_sdk_ssm.types.review_status


class DocumentVersionInfo(TypedDict):
    name: NotRequired["aws_sdk_ssm.types.document_name.DocumentName"]
    """<p>The document name.</p>"""
    display_name: NotRequired[
        "aws_sdk_ssm.types.document_display_name.DocumentDisplayName"
    ]
    """<p>The friendly name of the SSM document. This value can differ for each version of the document. If you want to update this value, see <a>UpdateDocument</a>.</p>"""
    document_version: NotRequired["aws_sdk_ssm.types.document_version.DocumentVersion"]
    """<p>The document version.</p>"""
    version_name: NotRequired[
        "aws_sdk_ssm.types.document_version_name.DocumentVersionName"
    ]
    """<p>The version of the artifact associated with the document. For example, 12.6. This value is unique across all versions of a document, and can't be changed.</p>"""
    created_date: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The date the document was created.</p>"""
    is_default_version: "aws_sdk_ssm.types.boolean.Boolean"
    """<p>An identifier for the default version of the document.</p>"""
    document_format: NotRequired["aws_sdk_ssm.types.document_format.DocumentFormat"]
    """<p>The document format, either JSON or YAML.</p>"""
    status: NotRequired["aws_sdk_ssm.types.document_status.DocumentStatus"]
    """<p>The status of the SSM document, such as <code>Creating</code>, <code>Active</code>, <code>Failed</code>, and <code>Deleting</code>.</p>"""
    status_information: NotRequired[
        "aws_sdk_ssm.types.document_status_information.DocumentStatusInformation"
    ]
    """<p>A message returned by Amazon Web Services Systems Manager that explains the <code>Status</code> value. For example, a <code>Failed</code> status might be explained by the <code>StatusInformation</code> message, \"The specified S3 bucket doesn't exist. Verify that the URL of the S3 bucket is correct.\"</p>"""
    review_status: NotRequired["aws_sdk_ssm.types.review_status.ReviewStatus"]
    """<p>The current status of the approval review for the latest version of the document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentVersionInfo) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "version_name" in value:
        out["VersionName"] = value["version_name"]
    if "created_date" in value:
        import aws_sdk_ssm.types.date_time

        out["CreatedDate"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["created_date"]
        )
    out["IsDefaultVersion"] = value.get("is_default_version", False)
    if "document_format" in value:
        import aws_sdk_ssm.types.document_format

        out["DocumentFormat"] = (
            aws_sdk_ssm.types.document_format.serialize_aws_json_1_1(
                value["document_format"]
            )
        )
    if "status" in value:
        import aws_sdk_ssm.types.document_status

        out["Status"] = aws_sdk_ssm.types.document_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_information" in value:
        out["StatusInformation"] = value["status_information"]
    if "review_status" in value:
        import aws_sdk_ssm.types.review_status

        out["ReviewStatus"] = aws_sdk_ssm.types.review_status.serialize_aws_json_1_1(
            value["review_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentVersionInfo:
    out: DocumentVersionInfo = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "DocumentVersion" in data:
        out["document_version"] = data["DocumentVersion"]
    if "VersionName" in data:
        out["version_name"] = data["VersionName"]
    if "CreatedDate" in data:
        import aws_sdk_ssm.types.date_time

        out["created_date"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["CreatedDate"]
        )
    if "IsDefaultVersion" in data:
        out["is_default_version"] = data["IsDefaultVersion"]
    else:
        out["is_default_version"] = False
    if "DocumentFormat" in data:
        import aws_sdk_ssm.types.document_format

        out["document_format"] = (
            aws_sdk_ssm.types.document_format.deserialize_aws_json_1_1(
                data["DocumentFormat"]
            )
        )
    if "Status" in data:
        import aws_sdk_ssm.types.document_status

        out["status"] = aws_sdk_ssm.types.document_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "StatusInformation" in data:
        out["status_information"] = data["StatusInformation"]
    if "ReviewStatus" in data:
        import aws_sdk_ssm.types.review_status

        out["review_status"] = aws_sdk_ssm.types.review_status.deserialize_aws_json_1_1(
            data["ReviewStatus"]
        )
    return out
