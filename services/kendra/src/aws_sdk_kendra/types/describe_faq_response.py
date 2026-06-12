"""Generated from Smithy shape ``com.amazonaws.kendra#DescribeFaqResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.description
    import aws_sdk_kendra.types.error_message
    import aws_sdk_kendra.types.faq_file_format
    import aws_sdk_kendra.types.faq_id
    import aws_sdk_kendra.types.faq_name
    import aws_sdk_kendra.types.faq_status
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.language_code
    import aws_sdk_kendra.types.role_arn
    import aws_sdk_kendra.types.s3_path
    import aws_sdk_kendra.types.timestamp


class DescribeFaqResponse(TypedDict):
    id: NotRequired["aws_sdk_kendra.types.faq_id.FaqId"]
    """<p>The identifier of the FAQ.</p>"""
    index_id: NotRequired["aws_sdk_kendra.types.index_id.IndexId"]
    """<p>The identifier of the index for the FAQ.</p>"""
    name: NotRequired["aws_sdk_kendra.types.faq_name.FaqName"]
    """<p>The name that you gave the FAQ when it was created.</p>"""
    description: NotRequired["aws_sdk_kendra.types.description.Description"]
    """<p>The description of the FAQ that you provided when it was created.</p>"""
    created_at: NotRequired["aws_sdk_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the FAQ was created.</p>"""
    updated_at: NotRequired["aws_sdk_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the FAQ was last updated.</p>"""
    s3_path: NotRequired["aws_sdk_kendra.types.s3_path.S3Path"]
    status: NotRequired["aws_sdk_kendra.types.faq_status.FaqStatus"]
    """<p>The status of the FAQ. It is ready to use when the status is <code>ACTIVE</code>.</p>"""
    role_arn: NotRequired["aws_sdk_kendra.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that provides access to the S3 bucket containing the FAQ file.</p>"""
    error_message: NotRequired["aws_sdk_kendra.types.error_message.ErrorMessage"]
    """<p>If the <code>Status</code> field is <code>FAILED</code>, the <code>ErrorMessage</code> field contains the reason why the FAQ failed.</p>"""
    file_format: NotRequired["aws_sdk_kendra.types.faq_file_format.FaqFileFormat"]
    """<p>The file format used for the FAQ file.</p>"""
    language_code: NotRequired["aws_sdk_kendra.types.language_code.LanguageCode"]
    """<p>The code for a language. This shows a supported language for the FAQ document. English is supported by default. For more information on supported languages, including their codes, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html\">Adding documents in languages other than English</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFaqResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "index_id" in value:
        out["IndexId"] = value["index_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import aws_sdk_kendra.types.timestamp

        out["CreatedAt"] = aws_sdk_kendra.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_kendra.types.timestamp

        out["UpdatedAt"] = aws_sdk_kendra.types.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "s3_path" in value:
        import aws_sdk_kendra.types.s3_path

        out["S3Path"] = aws_sdk_kendra.types.s3_path.serialize_aws_json_1_1(
            value["s3_path"]
        )
    if "status" in value:
        import aws_sdk_kendra.types.faq_status

        out["Status"] = aws_sdk_kendra.types.faq_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "file_format" in value:
        import aws_sdk_kendra.types.faq_file_format

        out["FileFormat"] = aws_sdk_kendra.types.faq_file_format.serialize_aws_json_1_1(
            value["file_format"]
        )
    if "language_code" in value:
        out["LanguageCode"] = value["language_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFaqResponse:
    out: DescribeFaqResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedAt" in data:
        import aws_sdk_kendra.types.timestamp

        out["created_at"] = aws_sdk_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import aws_sdk_kendra.types.timestamp

        out["updated_at"] = aws_sdk_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    if "S3Path" in data:
        import aws_sdk_kendra.types.s3_path

        out["s3_path"] = aws_sdk_kendra.types.s3_path.deserialize_aws_json_1_1(
            data["S3Path"]
        )
    if "Status" in data:
        import aws_sdk_kendra.types.faq_status

        out["status"] = aws_sdk_kendra.types.faq_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "FileFormat" in data:
        import aws_sdk_kendra.types.faq_file_format

        out["file_format"] = (
            aws_sdk_kendra.types.faq_file_format.deserialize_aws_json_1_1(
                data["FileFormat"]
            )
        )
    if "LanguageCode" in data:
        out["language_code"] = data["LanguageCode"]
    return out
