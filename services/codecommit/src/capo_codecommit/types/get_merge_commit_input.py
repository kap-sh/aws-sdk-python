"""Generated from Smithy shape ``com.amazonaws.codecommit#GetMergeCommitInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.commit_name
    import capo_codecommit.types.conflict_detail_level_type_enum
    import capo_codecommit.types.conflict_resolution_strategy_type_enum
    import capo_codecommit.types.repository_name


class GetMergeCommitInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the merge commit about which you want to get information.</p>"""
    source_commit_specifier: "capo_codecommit.types.commit_name.CommitName"
    """<p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>"""
    destination_commit_specifier: "capo_codecommit.types.commit_name.CommitName"
    """<p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>"""
    conflict_detail_level: NotRequired[
        "capo_codecommit.types.conflict_detail_level_type_enum.ConflictDetailLevelTypeEnum"
    ]
    """<p>The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.</p>"""
    conflict_resolution_strategy: NotRequired[
        "capo_codecommit.types.conflict_resolution_strategy_type_enum.ConflictResolutionStrategyTypeEnum"
    ]
    """<p>Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMergeCommitInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["sourceCommitSpecifier"] = value["source_commit_specifier"]
    out["destinationCommitSpecifier"] = value["destination_commit_specifier"]
    if "conflict_detail_level" in value:
        import capo_codecommit.types.conflict_detail_level_type_enum

        out["conflictDetailLevel"] = (
            capo_codecommit.types.conflict_detail_level_type_enum.serialize_aws_json_1_1(
                value["conflict_detail_level"]
            )
        )
    if "conflict_resolution_strategy" in value:
        import capo_codecommit.types.conflict_resolution_strategy_type_enum

        out["conflictResolutionStrategy"] = (
            capo_codecommit.types.conflict_resolution_strategy_type_enum.serialize_aws_json_1_1(
                value["conflict_resolution_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMergeCommitInput:
    out: GetMergeCommitInput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("GetMergeCommitInput.repository_name required")
    if "sourceCommitSpecifier" in data:
        out["source_commit_specifier"] = data["sourceCommitSpecifier"]
    else:
        raise DeserializationError(
            "GetMergeCommitInput.source_commit_specifier required"
        )
    if "destinationCommitSpecifier" in data:
        out["destination_commit_specifier"] = data["destinationCommitSpecifier"]
    else:
        raise DeserializationError(
            "GetMergeCommitInput.destination_commit_specifier required"
        )
    if "conflictDetailLevel" in data:
        import capo_codecommit.types.conflict_detail_level_type_enum

        out["conflict_detail_level"] = (
            capo_codecommit.types.conflict_detail_level_type_enum.deserialize_aws_json_1_1(
                data["conflictDetailLevel"]
            )
        )
    if "conflictResolutionStrategy" in data:
        import capo_codecommit.types.conflict_resolution_strategy_type_enum

        out["conflict_resolution_strategy"] = (
            capo_codecommit.types.conflict_resolution_strategy_type_enum.deserialize_aws_json_1_1(
                data["conflictResolutionStrategy"]
            )
        )
    return out
