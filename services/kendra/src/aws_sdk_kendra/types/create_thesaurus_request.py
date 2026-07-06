"""Generated from Smithy shape ``com.amazonaws.kendra#CreateThesaurusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.client_token_name
    import aws_sdk_kendra.types.description
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.role_arn
    import aws_sdk_kendra.types.s3_path
    import aws_sdk_kendra.types.tag_list
    import aws_sdk_kendra.types.thesaurus_name


class CreateThesaurusRequest(TypedDict, closed=True):
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for the thesaurus.</p>"""
    name: "aws_sdk_kendra.types.thesaurus_name.ThesaurusName"
    """<p>A name for the thesaurus.</p>"""
    description: NotRequired["aws_sdk_kendra.types.description.Description"]
    """<p>A description for the thesaurus.</p>"""
    role_arn: "aws_sdk_kendra.types.role_arn.RoleArn"
    r"""<p>The Amazon Resource Name (ARN) of an IAM role with permission to access your S3 bucket that contains the thesaurus file. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html\">IAM access roles for Amazon Kendra</a>.</p>"""
    tags: NotRequired["aws_sdk_kendra.types.tag_list.TagList"]
    """<p>A list of key-value pairs that identify or categorize the thesaurus. You can also use tags to help control access to the thesaurus. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>"""
    source_s3_path: "aws_sdk_kendra.types.s3_path.S3Path"
    """<p>The path to the thesaurus file in S3.</p>"""
    client_token: NotRequired["aws_sdk_kendra.types.client_token_name.ClientTokenName"]
    """<p>A token that you provide to identify the request to create a thesaurus. Multiple calls to the <code>CreateThesaurus</code> API with the same client token will create only one thesaurus. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateThesaurusRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_kendra.types.tag_list

        out["Tags"] = aws_sdk_kendra.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    import aws_sdk_kendra.types.s3_path

    out["SourceS3Path"] = aws_sdk_kendra.types.s3_path.serialize_aws_json_1_1(
        value["source_s3_path"]
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateThesaurusRequest:
    out: CreateThesaurusRequest = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("CreateThesaurusRequest.index_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateThesaurusRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("CreateThesaurusRequest.role_arn required")
    if "Tags" in data:
        import aws_sdk_kendra.types.tag_list

        out["tags"] = aws_sdk_kendra.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "SourceS3Path" in data:
        import aws_sdk_kendra.types.s3_path

        out["source_s3_path"] = aws_sdk_kendra.types.s3_path.deserialize_aws_json_1_1(
            data["SourceS3Path"]
        )
    else:
        raise DeserializationError("CreateThesaurusRequest.source_s3_path required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
