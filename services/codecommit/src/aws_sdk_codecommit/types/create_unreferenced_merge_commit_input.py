"""Generated from Smithy shape ``com.amazonaws.codecommit#CreateUnreferencedMergeCommitInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.commit_name
    import aws_sdk_codecommit.types.conflict_detail_level_type_enum
    import aws_sdk_codecommit.types.conflict_resolution
    import aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum
    import aws_sdk_codecommit.types.email
    import aws_sdk_codecommit.types.keep_empty_folders
    import aws_sdk_codecommit.types.merge_option_type_enum
    import aws_sdk_codecommit.types.message
    import aws_sdk_codecommit.types.name
    import aws_sdk_codecommit.types.repository_name


class CreateUnreferencedMergeCommitInput(TypedDict, closed=True):
    repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository where you want to create the unreferenced merge commit.</p>"""
    source_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName"
    """<p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>"""
    destination_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName"
    """<p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>"""
    merge_option: "aws_sdk_codecommit.types.merge_option_type_enum.MergeOptionTypeEnum"
    """<p>The merge option or strategy you want to use to merge the code.</p>"""
    conflict_detail_level: NotRequired[
        "aws_sdk_codecommit.types.conflict_detail_level_type_enum.ConflictDetailLevelTypeEnum"
    ]
    """<p>The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.</p>"""
    conflict_resolution_strategy: NotRequired[
        "aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum.ConflictResolutionStrategyTypeEnum"
    ]
    """<p>Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.</p>"""
    author_name: NotRequired["aws_sdk_codecommit.types.name.Name"]
    """<p>The name of the author who created the unreferenced commit. This information is used as both the author and committer for the commit.</p>"""
    email: NotRequired["aws_sdk_codecommit.types.email.Email"]
    """<p>The email address for the person who created the unreferenced commit.</p>"""
    commit_message: NotRequired["aws_sdk_codecommit.types.message.Message"]
    """<p>The commit message for the unreferenced commit.</p>"""
    keep_empty_folders: "aws_sdk_codecommit.types.keep_empty_folders.KeepEmptyFolders"
    """<p>If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If this is specified as true, a .gitkeep file is created for empty folders. The default is false.</p>"""
    conflict_resolution: NotRequired[
        "aws_sdk_codecommit.types.conflict_resolution.ConflictResolution"
    ]
    """<p>If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving conflicts during a merge.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUnreferencedMergeCommitInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["sourceCommitSpecifier"] = value["source_commit_specifier"]
    out["destinationCommitSpecifier"] = value["destination_commit_specifier"]
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
    if "conflict_resolution_strategy" in value:
        import aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum

        out["conflictResolutionStrategy"] = (
            aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum.serialize_aws_json_1_1(
                value["conflict_resolution_strategy"]
            )
        )
    if "author_name" in value:
        out["authorName"] = value["author_name"]
    if "email" in value:
        out["email"] = value["email"]
    if "commit_message" in value:
        out["commitMessage"] = value["commit_message"]
    out["keepEmptyFolders"] = value.get("keep_empty_folders", False)
    if "conflict_resolution" in value:
        import aws_sdk_codecommit.types.conflict_resolution

        out["conflictResolution"] = (
            aws_sdk_codecommit.types.conflict_resolution.serialize_aws_json_1_1(
                value["conflict_resolution"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUnreferencedMergeCommitInput:
    out: CreateUnreferencedMergeCommitInput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "CreateUnreferencedMergeCommitInput.repository_name required"
        )
    if "sourceCommitSpecifier" in data:
        out["source_commit_specifier"] = data["sourceCommitSpecifier"]
    else:
        raise DeserializationError(
            "CreateUnreferencedMergeCommitInput.source_commit_specifier required"
        )
    if "destinationCommitSpecifier" in data:
        out["destination_commit_specifier"] = data["destinationCommitSpecifier"]
    else:
        raise DeserializationError(
            "CreateUnreferencedMergeCommitInput.destination_commit_specifier required"
        )
    if "mergeOption" in data:
        import aws_sdk_codecommit.types.merge_option_type_enum

        out["merge_option"] = (
            aws_sdk_codecommit.types.merge_option_type_enum.deserialize_aws_json_1_1(
                data["mergeOption"]
            )
        )
    else:
        raise DeserializationError(
            "CreateUnreferencedMergeCommitInput.merge_option required"
        )
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
    if "authorName" in data:
        out["author_name"] = data["authorName"]
    if "email" in data:
        out["email"] = data["email"]
    if "commitMessage" in data:
        out["commit_message"] = data["commitMessage"]
    if "keepEmptyFolders" in data:
        out["keep_empty_folders"] = data["keepEmptyFolders"]
    else:
        out["keep_empty_folders"] = False
    if "conflictResolution" in data:
        import aws_sdk_codecommit.types.conflict_resolution

        out["conflict_resolution"] = (
            aws_sdk_codecommit.types.conflict_resolution.deserialize_aws_json_1_1(
                data["conflictResolution"]
            )
        )
    return out
