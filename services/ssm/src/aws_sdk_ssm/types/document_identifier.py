"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.date_time
    import aws_sdk_ssm.types.document_arn
    import aws_sdk_ssm.types.document_author
    import aws_sdk_ssm.types.document_display_name
    import aws_sdk_ssm.types.document_format
    import aws_sdk_ssm.types.document_owner
    import aws_sdk_ssm.types.document_requires_list
    import aws_sdk_ssm.types.document_schema_version
    import aws_sdk_ssm.types.document_type
    import aws_sdk_ssm.types.document_version
    import aws_sdk_ssm.types.document_version_name
    import aws_sdk_ssm.types.platform_type_list
    import aws_sdk_ssm.types.review_status
    import aws_sdk_ssm.types.tag_list
    import aws_sdk_ssm.types.target_type


class DocumentIdentifier(TypedDict):
    name: NotRequired["aws_sdk_ssm.types.document_arn.DocumentARN"]
    """<p>The name of the SSM document.</p>"""
    created_date: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The date the SSM document was created.</p>"""
    display_name: NotRequired[
        "aws_sdk_ssm.types.document_display_name.DocumentDisplayName"
    ]
    """<p>An optional field where you can specify a friendly name for the SSM document. This value can differ for each version of the document. If you want to update this value, see <a>UpdateDocument</a>.</p>"""
    owner: NotRequired["aws_sdk_ssm.types.document_owner.DocumentOwner"]
    """<p>The Amazon Web Services user that created the document.</p>"""
    version_name: NotRequired[
        "aws_sdk_ssm.types.document_version_name.DocumentVersionName"
    ]
    """<p>An optional field specifying the version of the artifact associated with the document. For example, 12.6. This value is unique across all versions of a document, and can't be changed.</p>"""
    platform_types: NotRequired["aws_sdk_ssm.types.platform_type_list.PlatformTypeList"]
    """<p>The operating system platform. </p>"""
    document_version: NotRequired["aws_sdk_ssm.types.document_version.DocumentVersion"]
    """<p>The document version.</p>"""
    document_type: NotRequired["aws_sdk_ssm.types.document_type.DocumentType"]
    """<p>The document type.</p>"""
    schema_version: NotRequired[
        "aws_sdk_ssm.types.document_schema_version.DocumentSchemaVersion"
    ]
    """<p>The schema version.</p>"""
    document_format: NotRequired["aws_sdk_ssm.types.document_format.DocumentFormat"]
    """<p>The document format, either JSON or YAML.</p>"""
    target_type: NotRequired["aws_sdk_ssm.types.target_type.TargetType"]
    """<p>The target type which defines the kinds of resources the document can run on. For example, <code>/AWS::EC2::Instance</code>. For a list of valid resource types, see <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html\">Amazon Web Services resource and property types reference</a> in the <i>CloudFormation User Guide</i>. </p>"""
    tags: NotRequired["aws_sdk_ssm.types.tag_list.TagList"]
    """<p>The tags, or metadata, that have been applied to the document.</p>"""
    requires: NotRequired[
        "aws_sdk_ssm.types.document_requires_list.DocumentRequiresList"
    ]
    """<p>A list of SSM documents required by a document. For example, an <code>ApplicationConfiguration</code> document requires an <code>ApplicationConfigurationSchema</code> document.</p>"""
    review_status: NotRequired["aws_sdk_ssm.types.review_status.ReviewStatus"]
    """<p>The current status of a document review.</p>"""
    author: NotRequired["aws_sdk_ssm.types.document_author.DocumentAuthor"]
    """<p>The user in your organization who created the document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentIdentifier) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "created_date" in value:
        import aws_sdk_ssm.types.date_time

        out["CreatedDate"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["created_date"]
        )
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "version_name" in value:
        out["VersionName"] = value["version_name"]
    if "platform_types" in value:
        import aws_sdk_ssm.types.platform_type_list

        out["PlatformTypes"] = (
            aws_sdk_ssm.types.platform_type_list.serialize_aws_json_1_1(
                value["platform_types"]
            )
        )
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "document_type" in value:
        import aws_sdk_ssm.types.document_type

        out["DocumentType"] = aws_sdk_ssm.types.document_type.serialize_aws_json_1_1(
            value["document_type"]
        )
    if "schema_version" in value:
        out["SchemaVersion"] = value["schema_version"]
    if "document_format" in value:
        import aws_sdk_ssm.types.document_format

        out["DocumentFormat"] = (
            aws_sdk_ssm.types.document_format.serialize_aws_json_1_1(
                value["document_format"]
            )
        )
    if "target_type" in value:
        out["TargetType"] = value["target_type"]
    if "tags" in value:
        import aws_sdk_ssm.types.tag_list

        out["Tags"] = aws_sdk_ssm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "requires" in value:
        import aws_sdk_ssm.types.document_requires_list

        out["Requires"] = (
            aws_sdk_ssm.types.document_requires_list.serialize_aws_json_1_1(
                value["requires"]
            )
        )
    if "review_status" in value:
        import aws_sdk_ssm.types.review_status

        out["ReviewStatus"] = aws_sdk_ssm.types.review_status.serialize_aws_json_1_1(
            value["review_status"]
        )
    if "author" in value:
        out["Author"] = value["author"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentIdentifier:
    out: DocumentIdentifier = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "CreatedDate" in data:
        import aws_sdk_ssm.types.date_time

        out["created_date"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["CreatedDate"]
        )
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "VersionName" in data:
        out["version_name"] = data["VersionName"]
    if "PlatformTypes" in data:
        import aws_sdk_ssm.types.platform_type_list

        out["platform_types"] = (
            aws_sdk_ssm.types.platform_type_list.deserialize_aws_json_1_1(
                data["PlatformTypes"]
            )
        )
    if "DocumentVersion" in data:
        out["document_version"] = data["DocumentVersion"]
    if "DocumentType" in data:
        import aws_sdk_ssm.types.document_type

        out["document_type"] = aws_sdk_ssm.types.document_type.deserialize_aws_json_1_1(
            data["DocumentType"]
        )
    if "SchemaVersion" in data:
        out["schema_version"] = data["SchemaVersion"]
    if "DocumentFormat" in data:
        import aws_sdk_ssm.types.document_format

        out["document_format"] = (
            aws_sdk_ssm.types.document_format.deserialize_aws_json_1_1(
                data["DocumentFormat"]
            )
        )
    if "TargetType" in data:
        out["target_type"] = data["TargetType"]
    if "Tags" in data:
        import aws_sdk_ssm.types.tag_list

        out["tags"] = aws_sdk_ssm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if "Requires" in data:
        import aws_sdk_ssm.types.document_requires_list

        out["requires"] = (
            aws_sdk_ssm.types.document_requires_list.deserialize_aws_json_1_1(
                data["Requires"]
            )
        )
    if "ReviewStatus" in data:
        import aws_sdk_ssm.types.review_status

        out["review_status"] = aws_sdk_ssm.types.review_status.deserialize_aws_json_1_1(
            data["ReviewStatus"]
        )
    if "Author" in data:
        out["author"] = data["Author"]
    return out
