"""Generated from Smithy shape ``com.amazonaws.kendra#CreateFaqRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.client_token_name
    import aws_sdk_kendra.types.description
    import aws_sdk_kendra.types.faq_file_format
    import aws_sdk_kendra.types.faq_name
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.language_code
    import aws_sdk_kendra.types.role_arn
    import aws_sdk_kendra.types.s3_path
    import aws_sdk_kendra.types.tag_list


class CreateFaqRequest(TypedDict):
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for the FAQ.</p>"""
    name: "aws_sdk_kendra.types.faq_name.FaqName"
    """<p>A name for the FAQ.</p>"""
    description: NotRequired["aws_sdk_kendra.types.description.Description"]
    """<p>A description for the FAQ.</p>"""
    s3_path: "aws_sdk_kendra.types.s3_path.S3Path"
    """<p>The path to the FAQ file in S3.</p>"""
    role_arn: "aws_sdk_kendra.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role with permission to access the S3 bucket that contains the FAQ file. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html\">IAM access roles for Amazon Kendra</a>.</p>"""
    tags: NotRequired["aws_sdk_kendra.types.tag_list.TagList"]
    """<p>A list of key-value pairs that identify the FAQ. You can use the tags to identify and organize your resources and to control access to resources.</p>"""
    file_format: NotRequired["aws_sdk_kendra.types.faq_file_format.FaqFileFormat"]
    """<p>The format of the FAQ input file. You can choose between a basic CSV format, a CSV format that includes customs attributes in a header, and a JSON format that includes custom attributes.</p> <p>The default format is CSV.</p> <p>The format must match the format of the file stored in the S3 bucket identified in the <code>S3Path</code> parameter.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/in-creating-faq.html\">Adding questions and answers</a>.</p>"""
    client_token: NotRequired["aws_sdk_kendra.types.client_token_name.ClientTokenName"]
    """<p>A token that you provide to identify the request to create a FAQ. Multiple calls to the <code>CreateFaqRequest</code> API with the same client token will create only one FAQ. </p>"""
    language_code: NotRequired["aws_sdk_kendra.types.language_code.LanguageCode"]
    """<p>The code for a language. This allows you to support a language for the FAQ document. English is supported by default. For more information on supported languages, including their codes, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html\">Adding documents in languages other than English</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFaqRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_kendra.types.s3_path

    out["S3Path"] = aws_sdk_kendra.types.s3_path.serialize_aws_json_1_1(
        value["s3_path"]
    )
    out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_kendra.types.tag_list

        out["Tags"] = aws_sdk_kendra.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "file_format" in value:
        import aws_sdk_kendra.types.faq_file_format

        out["FileFormat"] = aws_sdk_kendra.types.faq_file_format.serialize_aws_json_1_1(
            value["file_format"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "language_code" in value:
        out["LanguageCode"] = value["language_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFaqRequest:
    out: CreateFaqRequest = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("CreateFaqRequest.index_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateFaqRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "S3Path" in data:
        import aws_sdk_kendra.types.s3_path

        out["s3_path"] = aws_sdk_kendra.types.s3_path.deserialize_aws_json_1_1(
            data["S3Path"]
        )
    else:
        raise DeserializationError("CreateFaqRequest.s3_path required")
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("CreateFaqRequest.role_arn required")
    if "Tags" in data:
        import aws_sdk_kendra.types.tag_list

        out["tags"] = aws_sdk_kendra.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "FileFormat" in data:
        import aws_sdk_kendra.types.faq_file_format

        out["file_format"] = (
            aws_sdk_kendra.types.faq_file_format.deserialize_aws_json_1_1(
                data["FileFormat"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "LanguageCode" in data:
        out["language_code"] = data["LanguageCode"]
    return out
