"""Generated from Smithy shape ``com.amazonaws.kendra#UpdateQuerySuggestionsBlockListRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.description
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.query_suggestions_block_list_id
    import aws_sdk_kendra.types.query_suggestions_block_list_name
    import aws_sdk_kendra.types.role_arn
    import aws_sdk_kendra.types.s3_path


class UpdateQuerySuggestionsBlockListRequest(TypedDict):
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for the block list.</p>"""
    id: "aws_sdk_kendra.types.query_suggestions_block_list_id.QuerySuggestionsBlockListId"
    """<p>The identifier of the block list you want to update.</p>"""
    name: NotRequired[
        "aws_sdk_kendra.types.query_suggestions_block_list_name.QuerySuggestionsBlockListName"
    ]
    """<p>A new name for the block list.</p>"""
    description: NotRequired["aws_sdk_kendra.types.description.Description"]
    """<p>A new description for the block list.</p>"""
    source_s3_path: NotRequired["aws_sdk_kendra.types.s3_path.S3Path"]
    """<p>The S3 path where your block list text file sits in S3.</p> <p>If you update your block list and provide the same path to the block list text file in S3, then Amazon Kendra reloads the file to refresh the block list. Amazon Kendra does not automatically refresh your block list. You need to call the <code>UpdateQuerySuggestionsBlockList</code> API to refresh you block list.</p> <p>If you update your block list, then Amazon Kendra asynchronously refreshes all query suggestions with the latest content in the S3 file. This means changes might not take effect immediately.</p>"""
    role_arn: NotRequired["aws_sdk_kendra.types.role_arn.RoleArn"]
    """<p>The IAM (Identity and Access Management) role used to access the block list text file in S3.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateQuerySuggestionsBlockListRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "source_s3_path" in value:
        import aws_sdk_kendra.types.s3_path

        out["SourceS3Path"] = aws_sdk_kendra.types.s3_path.serialize_aws_json_1_1(
            value["source_s3_path"]
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateQuerySuggestionsBlockListRequest:
    out: UpdateQuerySuggestionsBlockListRequest = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError(
            "UpdateQuerySuggestionsBlockListRequest.index_id required"
        )
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("UpdateQuerySuggestionsBlockListRequest.id required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "SourceS3Path" in data:
        import aws_sdk_kendra.types.s3_path

        out["source_s3_path"] = aws_sdk_kendra.types.s3_path.deserialize_aws_json_1_1(
            data["SourceS3Path"]
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
