"""Generated from Smithy shape ``com.amazonaws.codecommit#ConflictMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.file_modes
    import capo_codecommit.types.file_sizes
    import capo_codecommit.types.is_binary_file
    import capo_codecommit.types.is_content_conflict
    import capo_codecommit.types.is_file_mode_conflict
    import capo_codecommit.types.is_object_type_conflict
    import capo_codecommit.types.merge_operations
    import capo_codecommit.types.number_of_conflicts
    import capo_codecommit.types.object_types
    import capo_codecommit.types.path


class ConflictMetadata(TypedDict, closed=True):
    file_path: NotRequired["capo_codecommit.types.path.Path"]
    """<p>The path of the file that contains conflicts.</p>"""
    file_sizes: NotRequired["capo_codecommit.types.file_sizes.FileSizes"]
    """<p>The file sizes of the file in the source, destination, and base of the merge.</p>"""
    file_modes: NotRequired["capo_codecommit.types.file_modes.FileModes"]
    """<p>The file modes of the file in the source, destination, and base of the merge.</p>"""
    object_types: NotRequired["capo_codecommit.types.object_types.ObjectTypes"]
    """<p>Information about any object type conflicts in a merge operation.</p>"""
    number_of_conflicts: "capo_codecommit.types.number_of_conflicts.NumberOfConflicts"
    """<p>The number of conflicts, including both hunk conflicts and metadata conflicts.</p>"""
    is_binary_file: NotRequired["capo_codecommit.types.is_binary_file.IsBinaryFile"]
    """<p>A boolean value (true or false) indicating whether the file is binary or textual in the source, destination, and base of the merge.</p>"""
    content_conflict: "capo_codecommit.types.is_content_conflict.IsContentConflict"
    """<p>A boolean value indicating whether there are conflicts in the content of a file.</p>"""
    file_mode_conflict: "capo_codecommit.types.is_file_mode_conflict.IsFileModeConflict"
    """<p>A boolean value indicating whether there are conflicts in the file mode of a file.</p>"""
    object_type_conflict: (
        "capo_codecommit.types.is_object_type_conflict.IsObjectTypeConflict"
    )
    """<p>A boolean value (true or false) indicating whether there are conflicts between the branches in the object type of a file, folder, or submodule.</p>"""
    merge_operations: NotRequired[
        "capo_codecommit.types.merge_operations.MergeOperations"
    ]
    """<p>Whether an add, modify, or delete operation caused the conflict between the source and destination of the merge.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConflictMetadata) -> dict:
    out: dict = {}
    if "file_path" in value:
        out["filePath"] = value["file_path"]
    if "file_sizes" in value:
        import capo_codecommit.types.file_sizes

        out["fileSizes"] = capo_codecommit.types.file_sizes.serialize_aws_json_1_1(
            value["file_sizes"]
        )
    if "file_modes" in value:
        import capo_codecommit.types.file_modes

        out["fileModes"] = capo_codecommit.types.file_modes.serialize_aws_json_1_1(
            value["file_modes"]
        )
    if "object_types" in value:
        import capo_codecommit.types.object_types

        out["objectTypes"] = capo_codecommit.types.object_types.serialize_aws_json_1_1(
            value["object_types"]
        )
    out["numberOfConflicts"] = value.get("number_of_conflicts", 0)
    if "is_binary_file" in value:
        import capo_codecommit.types.is_binary_file

        out["isBinaryFile"] = (
            capo_codecommit.types.is_binary_file.serialize_aws_json_1_1(
                value["is_binary_file"]
            )
        )
    out["contentConflict"] = value.get("content_conflict", False)
    out["fileModeConflict"] = value.get("file_mode_conflict", False)
    out["objectTypeConflict"] = value.get("object_type_conflict", False)
    if "merge_operations" in value:
        import capo_codecommit.types.merge_operations

        out["mergeOperations"] = (
            capo_codecommit.types.merge_operations.serialize_aws_json_1_1(
                value["merge_operations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConflictMetadata:
    out: ConflictMetadata = {}  # type: ignore[typeddict-item]
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    if "fileSizes" in data:
        import capo_codecommit.types.file_sizes

        out["file_sizes"] = capo_codecommit.types.file_sizes.deserialize_aws_json_1_1(
            data["fileSizes"]
        )
    if "fileModes" in data:
        import capo_codecommit.types.file_modes

        out["file_modes"] = capo_codecommit.types.file_modes.deserialize_aws_json_1_1(
            data["fileModes"]
        )
    if "objectTypes" in data:
        import capo_codecommit.types.object_types

        out["object_types"] = (
            capo_codecommit.types.object_types.deserialize_aws_json_1_1(
                data["objectTypes"]
            )
        )
    if "numberOfConflicts" in data:
        out["number_of_conflicts"] = data["numberOfConflicts"]
    else:
        out["number_of_conflicts"] = 0
    if "isBinaryFile" in data:
        import capo_codecommit.types.is_binary_file

        out["is_binary_file"] = (
            capo_codecommit.types.is_binary_file.deserialize_aws_json_1_1(
                data["isBinaryFile"]
            )
        )
    if "contentConflict" in data:
        out["content_conflict"] = data["contentConflict"]
    else:
        out["content_conflict"] = False
    if "fileModeConflict" in data:
        out["file_mode_conflict"] = data["fileModeConflict"]
    else:
        out["file_mode_conflict"] = False
    if "objectTypeConflict" in data:
        out["object_type_conflict"] = data["objectTypeConflict"]
    else:
        out["object_type_conflict"] = False
    if "mergeOperations" in data:
        import capo_codecommit.types.merge_operations

        out["merge_operations"] = (
            capo_codecommit.types.merge_operations.deserialize_aws_json_1_1(
                data["mergeOperations"]
            )
        )
    return out
