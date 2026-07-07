"""Generated from Smithy shape ``com.amazonaws.codecommit#SubModule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.object_id
    import aws_sdk_codecommit.types.path


class SubModule(TypedDict, closed=True):
    commit_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>The commit ID that contains the reference to the submodule.</p>"""
    absolute_path: NotRequired["aws_sdk_codecommit.types.path.Path"]
    """<p>The fully qualified path to the folder that contains the reference to the submodule.</p>"""
    relative_path: NotRequired["aws_sdk_codecommit.types.path.Path"]
    """<p>The relative path of the submodule from the folder where the query originated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubModule) -> dict:
    out: dict = {}
    if "commit_id" in value:
        out["commitId"] = value["commit_id"]
    if "absolute_path" in value:
        out["absolutePath"] = value["absolute_path"]
    if "relative_path" in value:
        out["relativePath"] = value["relative_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SubModule:
    out: SubModule = {}  # type: ignore[typeddict-item]
    if "commitId" in data:
        out["commit_id"] = data["commitId"]
    if "absolutePath" in data:
        out["absolute_path"] = data["absolutePath"]
    if "relativePath" in data:
        out["relative_path"] = data["relativePath"]
    return out
