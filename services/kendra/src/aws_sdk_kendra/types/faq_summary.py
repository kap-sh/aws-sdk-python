"""Generated from Smithy shape ``com.amazonaws.kendra#FaqSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.faq_file_format
    import aws_sdk_kendra.types.faq_id
    import aws_sdk_kendra.types.faq_name
    import aws_sdk_kendra.types.faq_status
    import aws_sdk_kendra.types.language_code
    import aws_sdk_kendra.types.timestamp


class FaqSummary(TypedDict, closed=True):
    id: NotRequired["aws_sdk_kendra.types.faq_id.FaqId"]
    """<p>The identifier of the FAQ.</p>"""
    name: NotRequired["aws_sdk_kendra.types.faq_name.FaqName"]
    """<p>The name that you assigned the FAQ when you created or updated the FAQ.</p>"""
    status: NotRequired["aws_sdk_kendra.types.faq_status.FaqStatus"]
    """<p>The current status of the FAQ. When the status is <code>ACTIVE</code> the FAQ is ready for use.</p>"""
    created_at: NotRequired["aws_sdk_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the FAQ was created.</p>"""
    updated_at: NotRequired["aws_sdk_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the FAQ was last updated.</p>"""
    file_format: NotRequired["aws_sdk_kendra.types.faq_file_format.FaqFileFormat"]
    """<p>The file type used to create the FAQ. </p>"""
    language_code: NotRequired["aws_sdk_kendra.types.language_code.LanguageCode"]
    r"""<p>The code for a language. This shows a supported language for the FAQ document as part of the summary information for FAQs. English is supported by default. For more information on supported languages, including their codes, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html\">Adding documents in languages other than English</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaqSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_kendra.types.faq_status

        out["Status"] = aws_sdk_kendra.types.faq_status.serialize_aws_json_1_1(
            value["status"]
        )
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
    if "file_format" in value:
        import aws_sdk_kendra.types.faq_file_format

        out["FileFormat"] = aws_sdk_kendra.types.faq_file_format.serialize_aws_json_1_1(
            value["file_format"]
        )
    if "language_code" in value:
        out["LanguageCode"] = value["language_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FaqSummary:
    out: FaqSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_kendra.types.faq_status

        out["status"] = aws_sdk_kendra.types.faq_status.deserialize_aws_json_1_1(
            data["Status"]
        )
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
