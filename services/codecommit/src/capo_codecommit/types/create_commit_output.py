"""Generated from Smithy shape ``com.amazonaws.codecommit#CreateCommitOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.files_metadata
    import capo_codecommit.types.object_id


class CreateCommitOutput(TypedDict, closed=True):
    commit_id: NotRequired["capo_codecommit.types.object_id.ObjectId"]
    """<p>The full commit ID of the commit that contains your committed file changes.</p>"""
    tree_id: NotRequired["capo_codecommit.types.object_id.ObjectId"]
    """<p>The full SHA-1 pointer of the tree information for the commit that contains the commited file changes.</p>"""
    files_added: NotRequired["capo_codecommit.types.files_metadata.FilesMetadata"]
    """<p>The files added as part of the committed file changes.</p>"""
    files_updated: NotRequired["capo_codecommit.types.files_metadata.FilesMetadata"]
    """<p>The files updated as part of the commited file changes.</p>"""
    files_deleted: NotRequired["capo_codecommit.types.files_metadata.FilesMetadata"]
    """<p>The files deleted as part of the committed file changes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCommitOutput) -> dict:
    out: dict = {}
    if "commit_id" in value:
        out["commitId"] = value["commit_id"]
    if "tree_id" in value:
        out["treeId"] = value["tree_id"]
    if "files_added" in value:
        import capo_codecommit.types.files_metadata

        out["filesAdded"] = capo_codecommit.types.files_metadata.serialize_aws_json_1_1(
            value["files_added"]
        )
    if "files_updated" in value:
        import capo_codecommit.types.files_metadata

        out["filesUpdated"] = (
            capo_codecommit.types.files_metadata.serialize_aws_json_1_1(
                value["files_updated"]
            )
        )
    if "files_deleted" in value:
        import capo_codecommit.types.files_metadata

        out["filesDeleted"] = (
            capo_codecommit.types.files_metadata.serialize_aws_json_1_1(
                value["files_deleted"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCommitOutput:
    out: CreateCommitOutput = {}  # type: ignore[typeddict-item]
    if "commitId" in data:
        out["commit_id"] = data["commitId"]
    if "treeId" in data:
        out["tree_id"] = data["treeId"]
    if "filesAdded" in data:
        import capo_codecommit.types.files_metadata

        out["files_added"] = (
            capo_codecommit.types.files_metadata.deserialize_aws_json_1_1(
                data["filesAdded"]
            )
        )
    if "filesUpdated" in data:
        import capo_codecommit.types.files_metadata

        out["files_updated"] = (
            capo_codecommit.types.files_metadata.deserialize_aws_json_1_1(
                data["filesUpdated"]
            )
        )
    if "filesDeleted" in data:
        import capo_codecommit.types.files_metadata

        out["files_deleted"] = (
            capo_codecommit.types.files_metadata.deserialize_aws_json_1_1(
                data["filesDeleted"]
            )
        )
    return out
