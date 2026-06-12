"""Generated from Smithy shape ``com.amazonaws.codecommit#GetFolderOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.file_list
    import aws_sdk_codecommit.types.folder_list
    import aws_sdk_codecommit.types.object_id
    import aws_sdk_codecommit.types.path
    import aws_sdk_codecommit.types.sub_module_list
    import aws_sdk_codecommit.types.symbolic_link_list


class GetFolderOutput(TypedDict):
    commit_id: "aws_sdk_codecommit.types.object_id.ObjectId"
    """<p>The full commit ID used as a reference for the returned version of the folder content.</p>"""
    folder_path: "aws_sdk_codecommit.types.path.Path"
    """<p>The fully qualified path of the folder whose contents are returned.</p>"""
    tree_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>The full SHA-1 pointer of the tree information for the commit that contains the folder.</p>"""
    sub_folders: NotRequired["aws_sdk_codecommit.types.folder_list.FolderList"]
    """<p>The list of folders that exist under the specified folder, if any.</p>"""
    files: NotRequired["aws_sdk_codecommit.types.file_list.FileList"]
    """<p>The list of files in the specified folder, if any.</p>"""
    symbolic_links: NotRequired[
        "aws_sdk_codecommit.types.symbolic_link_list.SymbolicLinkList"
    ]
    """<p>The list of symbolic links to other files and folders in the specified folder, if any.</p>"""
    sub_modules: NotRequired["aws_sdk_codecommit.types.sub_module_list.SubModuleList"]
    """<p>The list of submodules in the specified folder, if any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFolderOutput) -> dict:
    out: dict = {}
    out["commitId"] = value["commit_id"]
    out["folderPath"] = value["folder_path"]
    if "tree_id" in value:
        out["treeId"] = value["tree_id"]
    if "sub_folders" in value:
        import aws_sdk_codecommit.types.folder_list

        out["subFolders"] = aws_sdk_codecommit.types.folder_list.serialize_aws_json_1_1(
            value["sub_folders"]
        )
    if "files" in value:
        import aws_sdk_codecommit.types.file_list

        out["files"] = aws_sdk_codecommit.types.file_list.serialize_aws_json_1_1(
            value["files"]
        )
    if "symbolic_links" in value:
        import aws_sdk_codecommit.types.symbolic_link_list

        out["symbolicLinks"] = (
            aws_sdk_codecommit.types.symbolic_link_list.serialize_aws_json_1_1(
                value["symbolic_links"]
            )
        )
    if "sub_modules" in value:
        import aws_sdk_codecommit.types.sub_module_list

        out["subModules"] = (
            aws_sdk_codecommit.types.sub_module_list.serialize_aws_json_1_1(
                value["sub_modules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFolderOutput:
    out: GetFolderOutput = {}  # type: ignore[typeddict-item]
    if "commitId" in data:
        out["commit_id"] = data["commitId"]
    else:
        raise DeserializationError("GetFolderOutput.commit_id required")
    if "folderPath" in data:
        out["folder_path"] = data["folderPath"]
    else:
        raise DeserializationError("GetFolderOutput.folder_path required")
    if "treeId" in data:
        out["tree_id"] = data["treeId"]
    if "subFolders" in data:
        import aws_sdk_codecommit.types.folder_list

        out["sub_folders"] = (
            aws_sdk_codecommit.types.folder_list.deserialize_aws_json_1_1(
                data["subFolders"]
            )
        )
    if "files" in data:
        import aws_sdk_codecommit.types.file_list

        out["files"] = aws_sdk_codecommit.types.file_list.deserialize_aws_json_1_1(
            data["files"]
        )
    if "symbolicLinks" in data:
        import aws_sdk_codecommit.types.symbolic_link_list

        out["symbolic_links"] = (
            aws_sdk_codecommit.types.symbolic_link_list.deserialize_aws_json_1_1(
                data["symbolicLinks"]
            )
        )
    if "subModules" in data:
        import aws_sdk_codecommit.types.sub_module_list

        out["sub_modules"] = (
            aws_sdk_codecommit.types.sub_module_list.deserialize_aws_json_1_1(
                data["subModules"]
            )
        )
    return out
