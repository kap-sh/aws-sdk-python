"""Generated from Smithy shape ``com.amazonaws.codecommit#GetMergeConflictsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.conflict_metadata_list
    import aws_sdk_codecommit.types.is_mergeable
    import aws_sdk_codecommit.types.next_token
    import aws_sdk_codecommit.types.object_id


class GetMergeConflictsOutput(TypedDict, closed=True):
    mergeable: "aws_sdk_codecommit.types.is_mergeable.IsMergeable"
    """<p>A Boolean value that indicates whether the code is mergeable by the specified merge option.</p>"""
    destination_commit_id: "aws_sdk_codecommit.types.object_id.ObjectId"
    """<p>The commit ID of the destination commit specifier that was used in the merge evaluation.</p>"""
    source_commit_id: "aws_sdk_codecommit.types.object_id.ObjectId"
    """<p>The commit ID of the source commit specifier that was used in the merge evaluation.</p>"""
    base_commit_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>The commit ID of the merge base.</p>"""
    conflict_metadata_list: (
        "aws_sdk_codecommit.types.conflict_metadata_list.ConflictMetadataList"
    )
    """<p>A list of metadata for any conflicting files. If the specified merge strategy is FAST_FORWARD_MERGE, this list is always empty.</p>"""
    next_token: NotRequired["aws_sdk_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that can be used in a request to return the next batch of the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMergeConflictsOutput) -> dict:
    out: dict = {}
    out["mergeable"] = value.get("mergeable", False)
    out["destinationCommitId"] = value["destination_commit_id"]
    out["sourceCommitId"] = value["source_commit_id"]
    if "base_commit_id" in value:
        out["baseCommitId"] = value["base_commit_id"]
    import aws_sdk_codecommit.types.conflict_metadata_list

    out["conflictMetadataList"] = (
        aws_sdk_codecommit.types.conflict_metadata_list.serialize_aws_json_1_1(
            value["conflict_metadata_list"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMergeConflictsOutput:
    out: GetMergeConflictsOutput = {}  # type: ignore[typeddict-item]
    if "mergeable" in data:
        out["mergeable"] = data["mergeable"]
    else:
        out["mergeable"] = False
    if "destinationCommitId" in data:
        out["destination_commit_id"] = data["destinationCommitId"]
    else:
        raise DeserializationError(
            "GetMergeConflictsOutput.destination_commit_id required"
        )
    if "sourceCommitId" in data:
        out["source_commit_id"] = data["sourceCommitId"]
    else:
        raise DeserializationError("GetMergeConflictsOutput.source_commit_id required")
    if "baseCommitId" in data:
        out["base_commit_id"] = data["baseCommitId"]
    if "conflictMetadataList" in data:
        import aws_sdk_codecommit.types.conflict_metadata_list

        out["conflict_metadata_list"] = (
            aws_sdk_codecommit.types.conflict_metadata_list.deserialize_aws_json_1_1(
                data["conflictMetadataList"]
            )
        )
    else:
        raise DeserializationError(
            "GetMergeConflictsOutput.conflict_metadata_list required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
