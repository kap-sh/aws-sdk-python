"""Generated from Smithy shape ``com.amazonaws.codecommit#GetMergeConflictsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.commit_name
    import aws_sdk_codecommit.types.conflict_detail_level_type_enum
    import aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum
    import aws_sdk_codecommit.types.max_results
    import aws_sdk_codecommit.types.merge_option_type_enum
    import aws_sdk_codecommit.types.next_token
    import aws_sdk_codecommit.types.repository_name


class GetMergeConflictsInput(TypedDict):
    repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository where the pull request was created.</p>"""
    destination_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName"
    """<p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>"""
    source_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName"
    """<p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>"""
    merge_option: "aws_sdk_codecommit.types.merge_option_type_enum.MergeOptionTypeEnum"
    """<p>The merge option or strategy you want to use to merge the code. </p>"""
    conflict_detail_level: NotRequired[
        "aws_sdk_codecommit.types.conflict_detail_level_type_enum.ConflictDetailLevelTypeEnum"
    ]
    """<p>The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.</p>"""
    max_conflict_files: NotRequired["aws_sdk_codecommit.types.max_results.MaxResults"]
    """<p>The maximum number of files to include in the output.</p>"""
    conflict_resolution_strategy: NotRequired[
        "aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum.ConflictResolutionStrategyTypeEnum"
    ]
    """<p>Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.</p>"""
    next_token: NotRequired["aws_sdk_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMergeConflictsInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["destinationCommitSpecifier"] = value["destination_commit_specifier"]
    out["sourceCommitSpecifier"] = value["source_commit_specifier"]
    import aws_sdk_codecommit.types.merge_option_type_enum

    out["mergeOption"] = (
        aws_sdk_codecommit.types.merge_option_type_enum.serialize_aws_json_1_1(
            value["merge_option"]
        )
    )
    if "conflict_detail_level" in value:
        import aws_sdk_codecommit.types.conflict_detail_level_type_enum

        out["conflictDetailLevel"] = (
            aws_sdk_codecommit.types.conflict_detail_level_type_enum.serialize_aws_json_1_1(
                value["conflict_detail_level"]
            )
        )
    if "max_conflict_files" in value:
        out["maxConflictFiles"] = value["max_conflict_files"]
    if "conflict_resolution_strategy" in value:
        import aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum

        out["conflictResolutionStrategy"] = (
            aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum.serialize_aws_json_1_1(
                value["conflict_resolution_strategy"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMergeConflictsInput:
    out: GetMergeConflictsInput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("GetMergeConflictsInput.repository_name required")
    if "destinationCommitSpecifier" in data:
        out["destination_commit_specifier"] = data["destinationCommitSpecifier"]
    else:
        raise DeserializationError(
            "GetMergeConflictsInput.destination_commit_specifier required"
        )
    if "sourceCommitSpecifier" in data:
        out["source_commit_specifier"] = data["sourceCommitSpecifier"]
    else:
        raise DeserializationError(
            "GetMergeConflictsInput.source_commit_specifier required"
        )
    if "mergeOption" in data:
        import aws_sdk_codecommit.types.merge_option_type_enum

        out["merge_option"] = (
            aws_sdk_codecommit.types.merge_option_type_enum.deserialize_aws_json_1_1(
                data["mergeOption"]
            )
        )
    else:
        raise DeserializationError("GetMergeConflictsInput.merge_option required")
    if "conflictDetailLevel" in data:
        import aws_sdk_codecommit.types.conflict_detail_level_type_enum

        out["conflict_detail_level"] = (
            aws_sdk_codecommit.types.conflict_detail_level_type_enum.deserialize_aws_json_1_1(
                data["conflictDetailLevel"]
            )
        )
    if "maxConflictFiles" in data:
        out["max_conflict_files"] = data["maxConflictFiles"]
    if "conflictResolutionStrategy" in data:
        import aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum

        out["conflict_resolution_strategy"] = (
            aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum.deserialize_aws_json_1_1(
                data["conflictResolutionStrategy"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
