"""Generated from Smithy shape ``com.amazonaws.deadline#ManifestProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.file_system_location_name
    import aws_sdk_deadline.types.output_relative_directories_list
    import aws_sdk_deadline.types.path_format
    import aws_sdk_deadline.types.string


class ManifestProperties(TypedDict):
    file_system_location_name: NotRequired[
        "aws_sdk_deadline.types.file_system_location_name.FileSystemLocationName"
    ]
    """<p>The file system location name.</p>"""
    root_path: "aws_sdk_deadline.types.string.String"
    """<p>The file's root path.</p>"""
    root_path_format: "aws_sdk_deadline.types.path_format.PathFormat"
    """<p>The format of the root path.</p>"""
    output_relative_directories: NotRequired[
        "aws_sdk_deadline.types.output_relative_directories_list.OutputRelativeDirectoriesList"
    ]
    """<p>The file path relative to the directory.</p>"""
    input_manifest_path: NotRequired["aws_sdk_deadline.types.string.String"]
    """<p>The file path.</p>"""
    input_manifest_hash: NotRequired["aws_sdk_deadline.types.string.String"]
    """<p>The hash value of the file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManifestProperties) -> dict:
    out: dict = {}
    if "file_system_location_name" in value:
        out["fileSystemLocationName"] = value["file_system_location_name"]
    out["rootPath"] = value["root_path"]
    import aws_sdk_deadline.types.path_format

    out["rootPathFormat"] = aws_sdk_deadline.types.path_format.serialize_json(
        value["root_path_format"]
    )
    if "output_relative_directories" in value:
        import aws_sdk_deadline.types.output_relative_directories_list

        out["outputRelativeDirectories"] = (
            aws_sdk_deadline.types.output_relative_directories_list.serialize_json(
                value["output_relative_directories"]
            )
        )
    if "input_manifest_path" in value:
        out["inputManifestPath"] = value["input_manifest_path"]
    if "input_manifest_hash" in value:
        out["inputManifestHash"] = value["input_manifest_hash"]
    return out


def deserialize_json(data: dict) -> ManifestProperties:
    out: ManifestProperties = {}  # type: ignore[typeddict-item]
    if "fileSystemLocationName" in data:
        out["file_system_location_name"] = data["fileSystemLocationName"]
    if "rootPath" in data:
        out["root_path"] = data["rootPath"]
    else:
        raise DeserializationError("ManifestProperties.root_path required")
    if "rootPathFormat" in data:
        import aws_sdk_deadline.types.path_format

        out["root_path_format"] = aws_sdk_deadline.types.path_format.deserialize_json(
            data["rootPathFormat"]
        )
    else:
        raise DeserializationError("ManifestProperties.root_path_format required")
    if "outputRelativeDirectories" in data:
        import aws_sdk_deadline.types.output_relative_directories_list

        out["output_relative_directories"] = (
            aws_sdk_deadline.types.output_relative_directories_list.deserialize_json(
                data["outputRelativeDirectories"]
            )
        )
    if "inputManifestPath" in data:
        out["input_manifest_path"] = data["inputManifestPath"]
    if "inputManifestHash" in data:
        out["input_manifest_hash"] = data["inputManifestHash"]
    return out
