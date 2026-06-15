"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#VersionLineageMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.branch_name
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version_list
    import aws_sdk_bedrock_agentcore_control.types.version_created_by_source


class VersionLineageMetadata(TypedDict):
    parent_version_ids: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version_list.ConfigurationBundleVersionList"
    ]
    """<p>A list of parent version identifiers. Regular commits have 0-1 parents. Merge commits have 2 parents: the target branch parent and the source branch parent. The first parent represents the primary lineage.</p>"""
    branch_name: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.branch_name.BranchName"
    ]
    """<p>The branch name for this version. If not specified, inherits the parent's branch or defaults to <code>mainline</code>.</p>"""
    created_by: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.version_created_by_source.VersionCreatedBySource"
    ]
    """<p>The source that created this version.</p>"""
    commit_message: NotRequired["str"]
    """<p>A commit message describing the changes in this version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VersionLineageMetadata) -> dict:
    out: dict = {}
    if "parent_version_ids" in value:
        import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version_list

        out["parentVersionIds"] = (
            aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version_list.serialize_json(
                value["parent_version_ids"]
            )
        )
    if "branch_name" in value:
        out["branchName"] = value["branch_name"]
    if "created_by" in value:
        import aws_sdk_bedrock_agentcore_control.types.version_created_by_source

        out["createdBy"] = (
            aws_sdk_bedrock_agentcore_control.types.version_created_by_source.serialize_json(
                value["created_by"]
            )
        )
    if "commit_message" in value:
        out["commitMessage"] = value["commit_message"]
    return out


def deserialize_json(data: dict) -> VersionLineageMetadata:
    out: VersionLineageMetadata = {}  # type: ignore[typeddict-item]
    if "parentVersionIds" in data:
        import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version_list

        out["parent_version_ids"] = (
            aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version_list.deserialize_json(
                data["parentVersionIds"]
            )
        )
    if "branchName" in data:
        out["branch_name"] = data["branchName"]
    if "createdBy" in data:
        import aws_sdk_bedrock_agentcore_control.types.version_created_by_source

        out["created_by"] = (
            aws_sdk_bedrock_agentcore_control.types.version_created_by_source.deserialize_json(
                data["createdBy"]
            )
        )
    if "commitMessage" in data:
        out["commit_message"] = data["commitMessage"]
    return out
