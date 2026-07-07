"""Generated from Smithy shape ``com.amazonaws.kendra#UpdateThesaurusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.description
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.role_arn
    import aws_sdk_kendra.types.s3_path
    import aws_sdk_kendra.types.thesaurus_id
    import aws_sdk_kendra.types.thesaurus_name


class UpdateThesaurusRequest(TypedDict, closed=True):
    id: "aws_sdk_kendra.types.thesaurus_id.ThesaurusId"
    """<p>The identifier of the thesaurus you want to update.</p>"""
    name: NotRequired["aws_sdk_kendra.types.thesaurus_name.ThesaurusName"]
    """<p>A new name for the thesaurus.</p>"""
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for the thesaurus.</p>"""
    description: NotRequired["aws_sdk_kendra.types.description.Description"]
    """<p>A new description for the thesaurus.</p>"""
    role_arn: NotRequired["aws_sdk_kendra.types.role_arn.RoleArn"]
    """<p>An IAM role that gives Amazon Kendra permissions to access thesaurus file specified in <code>SourceS3Path</code>.</p>"""
    source_s3_path: NotRequired["aws_sdk_kendra.types.s3_path.S3Path"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateThesaurusRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    out["IndexId"] = value["index_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "source_s3_path" in value:
        import aws_sdk_kendra.types.s3_path

        out["SourceS3Path"] = aws_sdk_kendra.types.s3_path.serialize_aws_json_1_1(
            value["source_s3_path"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateThesaurusRequest:
    out: UpdateThesaurusRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("UpdateThesaurusRequest.id required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("UpdateThesaurusRequest.index_id required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "SourceS3Path" in data:
        import aws_sdk_kendra.types.s3_path

        out["source_s3_path"] = aws_sdk_kendra.types.s3_path.deserialize_aws_json_1_1(
            data["SourceS3Path"]
        )
    return out
