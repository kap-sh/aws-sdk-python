"""Generated from Smithy shape ``com.amazonaws.codecommit#GetFileOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.file_content
    import capo_codecommit.types.file_mode_type_enum
    import capo_codecommit.types.object_id
    import capo_codecommit.types.object_size
    import capo_codecommit.types.path


class GetFileOutput(TypedDict, closed=True):
    commit_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The full commit ID of the commit that contains the content returned by GetFile.</p>"""
    blob_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The blob ID of the object that represents the file content.</p>"""
    file_path: "capo_codecommit.types.path.Path"
    """<p>The fully qualified path to the specified file. Returns the name and extension of the file.</p>"""
    file_mode: "capo_codecommit.types.file_mode_type_enum.FileModeTypeEnum"
    """<p>The extrapolated file mode permissions of the blob. Valid values include strings such as EXECUTABLE and not numeric values.</p> <note> <p>The file mode permissions returned by this API are not the standard file mode permission values, such as 100644, but rather extrapolated values. See the supported return values.</p> </note>"""
    file_size: "capo_codecommit.types.object_size.ObjectSize"
    """<p>The size of the contents of the file, in bytes.</p>"""
    file_content: "capo_codecommit.types.file_content.FileContent"
    """<p>The base-64 encoded binary data object that represents the content of the file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFileOutput) -> dict:
    out: dict = {}
    out["commitId"] = value["commit_id"]
    out["blobId"] = value["blob_id"]
    out["filePath"] = value["file_path"]
    import capo_codecommit.types.file_mode_type_enum

    out["fileMode"] = capo_codecommit.types.file_mode_type_enum.serialize_aws_json_1_1(
        value["file_mode"]
    )
    out["fileSize"] = value.get("file_size", 0)
    import capo_codecommit.types.file_content

    out["fileContent"] = capo_codecommit.types.file_content.serialize_aws_json_1_1(
        value["file_content"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFileOutput:
    out: GetFileOutput = {}  # type: ignore[typeddict-item]
    if "commitId" in data:
        out["commit_id"] = data["commitId"]
    else:
        raise DeserializationError("GetFileOutput.commit_id required")
    if "blobId" in data:
        out["blob_id"] = data["blobId"]
    else:
        raise DeserializationError("GetFileOutput.blob_id required")
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    else:
        raise DeserializationError("GetFileOutput.file_path required")
    if "fileMode" in data:
        import capo_codecommit.types.file_mode_type_enum

        out["file_mode"] = (
            capo_codecommit.types.file_mode_type_enum.deserialize_aws_json_1_1(
                data["fileMode"]
            )
        )
    else:
        raise DeserializationError("GetFileOutput.file_mode required")
    if "fileSize" in data:
        out["file_size"] = data["fileSize"]
    else:
        out["file_size"] = 0
    if "fileContent" in data:
        import capo_codecommit.types.file_content

        out["file_content"] = (
            capo_codecommit.types.file_content.deserialize_aws_json_1_1(
                data["fileContent"]
            )
        )
    else:
        raise DeserializationError("GetFileOutput.file_content required")
    return out
