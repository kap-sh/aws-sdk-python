"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchDescribeMergeConflictsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.batch_describe_merge_conflicts_errors
    import aws_sdk_codecommit.types.conflicts
    import aws_sdk_codecommit.types.next_token
    import aws_sdk_codecommit.types.object_id


class BatchDescribeMergeConflictsOutput(TypedDict, closed=True):
    conflicts: "aws_sdk_codecommit.types.conflicts.Conflicts"
    """<p>A list of conflicts for each file, including the conflict metadata and the hunks of the differences between the files.</p>"""
    next_token: NotRequired["aws_sdk_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that can be used in a request to return the next batch of the results.</p>"""
    errors: NotRequired[
        "aws_sdk_codecommit.types.batch_describe_merge_conflicts_errors.BatchDescribeMergeConflictsErrors"
    ]
    """<p>A list of any errors returned while describing the merge conflicts for each file.</p>"""
    destination_commit_id: "aws_sdk_codecommit.types.object_id.ObjectId"
    """<p>The commit ID of the destination commit specifier that was used in the merge evaluation.</p>"""
    source_commit_id: "aws_sdk_codecommit.types.object_id.ObjectId"
    """<p>The commit ID of the source commit specifier that was used in the merge evaluation.</p>"""
    base_commit_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>The commit ID of the merge base.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDescribeMergeConflictsOutput) -> dict:
    out: dict = {}
    import aws_sdk_codecommit.types.conflicts

    out["conflicts"] = aws_sdk_codecommit.types.conflicts.serialize_aws_json_1_1(
        value["conflicts"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "errors" in value:
        import aws_sdk_codecommit.types.batch_describe_merge_conflicts_errors

        out["errors"] = (
            aws_sdk_codecommit.types.batch_describe_merge_conflicts_errors.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    out["destinationCommitId"] = value["destination_commit_id"]
    out["sourceCommitId"] = value["source_commit_id"]
    if "base_commit_id" in value:
        out["baseCommitId"] = value["base_commit_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDescribeMergeConflictsOutput:
    out: BatchDescribeMergeConflictsOutput = {}  # type: ignore[typeddict-item]
    if "conflicts" in data:
        import aws_sdk_codecommit.types.conflicts

        out["conflicts"] = aws_sdk_codecommit.types.conflicts.deserialize_aws_json_1_1(
            data["conflicts"]
        )
    else:
        raise DeserializationError(
            "BatchDescribeMergeConflictsOutput.conflicts required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "errors" in data:
        import aws_sdk_codecommit.types.batch_describe_merge_conflicts_errors

        out["errors"] = (
            aws_sdk_codecommit.types.batch_describe_merge_conflicts_errors.deserialize_aws_json_1_1(
                data["errors"]
            )
        )
    if "destinationCommitId" in data:
        out["destination_commit_id"] = data["destinationCommitId"]
    else:
        raise DeserializationError(
            "BatchDescribeMergeConflictsOutput.destination_commit_id required"
        )
    if "sourceCommitId" in data:
        out["source_commit_id"] = data["sourceCommitId"]
    else:
        raise DeserializationError(
            "BatchDescribeMergeConflictsOutput.source_commit_id required"
        )
    if "baseCommitId" in data:
        out["base_commit_id"] = data["baseCommitId"]
    return out
