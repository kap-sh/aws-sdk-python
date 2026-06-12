"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#SourceCodeType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.branch_diff_source_code_type
    import aws_sdk_codeguru_reviewer.types.commit_diff_source_code_type
    import aws_sdk_codeguru_reviewer.types.repository_head_source_code_type
    import aws_sdk_codeguru_reviewer.types.request_metadata
    import aws_sdk_codeguru_reviewer.types.s3_bucket_repository


class SourceCodeType(TypedDict):
    commit_diff: NotRequired[
        "aws_sdk_codeguru_reviewer.types.commit_diff_source_code_type.CommitDiffSourceCodeType"
    ]
    """<p>A <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType\">SourceCodeType</a> that specifies a commit diff created by a pull request on an associated repository.</p>"""
    repository_head: NotRequired[
        "aws_sdk_codeguru_reviewer.types.repository_head_source_code_type.RepositoryHeadSourceCodeType"
    ]
    branch_diff: NotRequired[
        "aws_sdk_codeguru_reviewer.types.branch_diff_source_code_type.BranchDiffSourceCodeType"
    ]
    """<p>A type of <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType\">SourceCodeType</a> that specifies a source branch name and a destination branch name in an associated repository.</p>"""
    s3_bucket_repository: NotRequired[
        "aws_sdk_codeguru_reviewer.types.s3_bucket_repository.S3BucketRepository"
    ]
    """<p>Information about an associated repository in an S3 bucket that includes its name and an <code>S3RepositoryDetails</code> object. The <code>S3RepositoryDetails</code> object includes the name of an S3 bucket, an S3 key for a source code .zip file, and an S3 key for a build artifacts .zip file. <code>S3BucketRepository</code> is required in <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType\">SourceCodeType</a> for <code>S3BucketRepository</code> based code reviews.</p>"""
    request_metadata: NotRequired[
        "aws_sdk_codeguru_reviewer.types.request_metadata.RequestMetadata"
    ]
    """<p>Metadata that is associated with a code review. This applies to any type of code review supported by CodeGuru Reviewer. The <code>RequestMetadaa</code> field captures any event metadata. For example, it might capture metadata associated with an event trigger, such as a push or a pull request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceCodeType) -> dict:
    out: dict = {}
    if "commit_diff" in value:
        import aws_sdk_codeguru_reviewer.types.commit_diff_source_code_type

        out["CommitDiff"] = (
            aws_sdk_codeguru_reviewer.types.commit_diff_source_code_type.serialize_json(
                value["commit_diff"]
            )
        )
    if "repository_head" in value:
        import aws_sdk_codeguru_reviewer.types.repository_head_source_code_type

        out["RepositoryHead"] = (
            aws_sdk_codeguru_reviewer.types.repository_head_source_code_type.serialize_json(
                value["repository_head"]
            )
        )
    if "branch_diff" in value:
        import aws_sdk_codeguru_reviewer.types.branch_diff_source_code_type

        out["BranchDiff"] = (
            aws_sdk_codeguru_reviewer.types.branch_diff_source_code_type.serialize_json(
                value["branch_diff"]
            )
        )
    if "s3_bucket_repository" in value:
        import aws_sdk_codeguru_reviewer.types.s3_bucket_repository

        out["S3BucketRepository"] = (
            aws_sdk_codeguru_reviewer.types.s3_bucket_repository.serialize_json(
                value["s3_bucket_repository"]
            )
        )
    if "request_metadata" in value:
        import aws_sdk_codeguru_reviewer.types.request_metadata

        out["RequestMetadata"] = (
            aws_sdk_codeguru_reviewer.types.request_metadata.serialize_json(
                value["request_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> SourceCodeType:
    out: SourceCodeType = {}  # type: ignore[typeddict-item]
    if "CommitDiff" in data:
        import aws_sdk_codeguru_reviewer.types.commit_diff_source_code_type

        out["commit_diff"] = (
            aws_sdk_codeguru_reviewer.types.commit_diff_source_code_type.deserialize_json(
                data["CommitDiff"]
            )
        )
    if "RepositoryHead" in data:
        import aws_sdk_codeguru_reviewer.types.repository_head_source_code_type

        out["repository_head"] = (
            aws_sdk_codeguru_reviewer.types.repository_head_source_code_type.deserialize_json(
                data["RepositoryHead"]
            )
        )
    if "BranchDiff" in data:
        import aws_sdk_codeguru_reviewer.types.branch_diff_source_code_type

        out["branch_diff"] = (
            aws_sdk_codeguru_reviewer.types.branch_diff_source_code_type.deserialize_json(
                data["BranchDiff"]
            )
        )
    if "S3BucketRepository" in data:
        import aws_sdk_codeguru_reviewer.types.s3_bucket_repository

        out["s3_bucket_repository"] = (
            aws_sdk_codeguru_reviewer.types.s3_bucket_repository.deserialize_json(
                data["S3BucketRepository"]
            )
        )
    if "RequestMetadata" in data:
        import aws_sdk_codeguru_reviewer.types.request_metadata

        out["request_metadata"] = (
            aws_sdk_codeguru_reviewer.types.request_metadata.deserialize_json(
                data["RequestMetadata"]
            )
        )
    return out
