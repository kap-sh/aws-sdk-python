"""Generated from Smithy shape ``com.amazonaws.codecommit#Folder``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.object_id
    import capo_codecommit.types.path


class Folder(TypedDict, closed=True):
    tree_id: NotRequired["capo_codecommit.types.object_id.ObjectId"]
    """<p>The full SHA-1 pointer of the tree information for the commit that contains the folder.</p>"""
    absolute_path: NotRequired["capo_codecommit.types.path.Path"]
    """<p>The fully qualified path of the folder in the repository.</p>"""
    relative_path: NotRequired["capo_codecommit.types.path.Path"]
    """<p>The relative path of the specified folder from the folder where the query originated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Folder) -> dict:
    out: dict = {}
    if "tree_id" in value:
        out["treeId"] = value["tree_id"]
    if "absolute_path" in value:
        out["absolutePath"] = value["absolute_path"]
    if "relative_path" in value:
        out["relativePath"] = value["relative_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Folder:
    out: Folder = {}  # type: ignore[typeddict-item]
    if "treeId" in data:
        out["tree_id"] = data["treeId"]
    if "absolutePath" in data:
        out["absolute_path"] = data["absolutePath"]
    if "relativePath" in data:
        out["relative_path"] = data["relativePath"]
    return out
