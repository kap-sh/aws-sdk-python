"""Generated from Smithy shape ``com.amazonaws.codecommit#DescribeMergeConflictsInput``."""

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
    import aws_sdk_codecommit.types.path
    import aws_sdk_codecommit.types.repository_name


class DescribeMergeConflictsInput(TypedDict):
    repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository where you want to get information about a merge conflict.</p>"""
    destination_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName"
    """<p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>"""
    source_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName"
    """<p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>"""
    merge_option: "aws_sdk_codecommit.types.merge_option_type_enum.MergeOptionTypeEnum"
    """<p>The merge option or strategy you want to use to merge the code.</p>"""
    max_merge_hunks: NotRequired["aws_sdk_codecommit.types.max_results.MaxResults"]
    """<p>The maximum number of merge hunks to include in the output.</p>"""
    file_path: "aws_sdk_codecommit.types.path.Path"
    """<p>The path of the target files used to describe the conflicts. </p>"""
    conflict_detail_level: NotRequired[
        "aws_sdk_codecommit.types.conflict_detail_level_type_enum.ConflictDetailLevelTypeEnum"
    ]
    """<p>The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.</p>"""
    conflict_resolution_strategy: NotRequired[
        "aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum.ConflictResolutionStrategyTypeEnum"
    ]
    """<p>Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.</p>"""
    next_token: NotRequired["aws_sdk_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMergeConflictsInput) -> dict:
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
    if "max_merge_hunks" in value:
        out["maxMergeHunks"] = value["max_merge_hunks"]
    out["filePath"] = value["file_path"]
    if "conflict_detail_level" in value:
        import aws_sdk_codecommit.types.conflict_detail_level_type_enum

        out["conflictDetailLevel"] = (
            aws_sdk_codecommit.types.conflict_detail_level_type_enum.serialize_aws_json_1_1(
                value["conflict_detail_level"]
            )
        )
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


def deserialize_aws_json_1_1(data: dict) -> DescribeMergeConflictsInput:
    out: DescribeMergeConflictsInput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "DescribeMergeConflictsInput.repository_name required"
        )
    if "destinationCommitSpecifier" in data:
        out["destination_commit_specifier"] = data["destinationCommitSpecifier"]
    else:
        raise DeserializationError(
            "DescribeMergeConflictsInput.destination_commit_specifier required"
        )
    if "sourceCommitSpecifier" in data:
        out["source_commit_specifier"] = data["sourceCommitSpecifier"]
    else:
        raise DeserializationError(
            "DescribeMergeConflictsInput.source_commit_specifier required"
        )
    if "mergeOption" in data:
        import aws_sdk_codecommit.types.merge_option_type_enum

        out["merge_option"] = (
            aws_sdk_codecommit.types.merge_option_type_enum.deserialize_aws_json_1_1(
                data["mergeOption"]
            )
        )
    else:
        raise DeserializationError("DescribeMergeConflictsInput.merge_option required")
    if "maxMergeHunks" in data:
        out["max_merge_hunks"] = data["maxMergeHunks"]
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    else:
        raise DeserializationError("DescribeMergeConflictsInput.file_path required")
    if "conflictDetailLevel" in data:
        import aws_sdk_codecommit.types.conflict_detail_level_type_enum

        out["conflict_detail_level"] = (
            aws_sdk_codecommit.types.conflict_detail_level_type_enum.deserialize_aws_json_1_1(
                data["conflictDetailLevel"]
            )
        )
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
