"""Generated from Smithy shape ``com.amazonaws.kendra#DescribeThesaurusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.description
    import capo_kendra.types.error_message
    import capo_kendra.types.index_id
    import capo_kendra.types.long
    import capo_kendra.types.role_arn
    import capo_kendra.types.s3_path
    import capo_kendra.types.thesaurus_id
    import capo_kendra.types.thesaurus_name
    import capo_kendra.types.thesaurus_status
    import capo_kendra.types.timestamp


class DescribeThesaurusResponse(TypedDict, closed=True):
    id: NotRequired["capo_kendra.types.thesaurus_id.ThesaurusId"]
    """<p>The identifier of the thesaurus.</p>"""
    index_id: NotRequired["capo_kendra.types.index_id.IndexId"]
    """<p>The identifier of the index for the thesaurus.</p>"""
    name: NotRequired["capo_kendra.types.thesaurus_name.ThesaurusName"]
    """<p>The thesaurus name.</p>"""
    description: NotRequired["capo_kendra.types.description.Description"]
    """<p>The thesaurus description.</p>"""
    status: NotRequired["capo_kendra.types.thesaurus_status.ThesaurusStatus"]
    """<p>The current status of the thesaurus. When the value is <code>ACTIVE</code>, queries are able to use the thesaurus. If the <code>Status</code> field value is <code>FAILED</code>, the <code>ErrorMessage</code> field provides more information. </p> <p>If the status is <code>ACTIVE_BUT_UPDATE_FAILED</code>, it means that Amazon Kendra could not ingest the new thesaurus file. The old thesaurus file is still active. </p>"""
    error_message: NotRequired["capo_kendra.types.error_message.ErrorMessage"]
    """<p>When the <code>Status</code> field value is <code>FAILED</code>, the <code>ErrorMessage</code> field provides more information. </p>"""
    created_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the thesaurus was created.</p>"""
    updated_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the thesaurus was last updated.</p>"""
    role_arn: NotRequired["capo_kendra.types.role_arn.RoleArn"]
    """<p>An IAM role that gives Amazon Kendra permissions to access thesaurus file specified in <code>SourceS3Path</code>. </p>"""
    source_s3_path: NotRequired["capo_kendra.types.s3_path.S3Path"]
    file_size_bytes: NotRequired["capo_kendra.types.long.Long"]
    """<p>The size of the thesaurus file in bytes.</p>"""
    term_count: NotRequired["capo_kendra.types.long.Long"]
    """<p>The number of unique terms in the thesaurus file. For example, the synonyms <code>a,b,c</code> and <code>a=>d</code>, the term count would be 4. </p>"""
    synonym_rule_count: NotRequired["capo_kendra.types.long.Long"]
    """<p>The number of synonym rules in the thesaurus file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeThesaurusResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "index_id" in value:
        out["IndexId"] = value["index_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_kendra.types.thesaurus_status

        out["Status"] = capo_kendra.types.thesaurus_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "created_at" in value:
        import capo_kendra.types.timestamp

        out["CreatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_kendra.types.timestamp

        out["UpdatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "source_s3_path" in value:
        import capo_kendra.types.s3_path

        out["SourceS3Path"] = capo_kendra.types.s3_path.serialize_aws_json_1_1(
            value["source_s3_path"]
        )
    if "file_size_bytes" in value:
        out["FileSizeBytes"] = value["file_size_bytes"]
    if "term_count" in value:
        out["TermCount"] = value["term_count"]
    if "synonym_rule_count" in value:
        out["SynonymRuleCount"] = value["synonym_rule_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeThesaurusResponse:
    out: DescribeThesaurusResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import capo_kendra.types.thesaurus_status

        out["status"] = capo_kendra.types.thesaurus_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "CreatedAt" in data:
        import capo_kendra.types.timestamp

        out["created_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import capo_kendra.types.timestamp

        out["updated_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "SourceS3Path" in data:
        import capo_kendra.types.s3_path

        out["source_s3_path"] = capo_kendra.types.s3_path.deserialize_aws_json_1_1(
            data["SourceS3Path"]
        )
    if "FileSizeBytes" in data:
        out["file_size_bytes"] = data["FileSizeBytes"]
    if "TermCount" in data:
        out["term_count"] = data["TermCount"]
    if "SynonymRuleCount" in data:
        out["synonym_rule_count"] = data["SynonymRuleCount"]
    return out
