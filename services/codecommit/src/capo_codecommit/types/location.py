"""Generated from Smithy shape ``com.amazonaws.codecommit#Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.path
    import capo_codecommit.types.position
    import capo_codecommit.types.relative_file_version_enum


class Location(TypedDict, closed=True):
    file_path: NotRequired["capo_codecommit.types.path.Path"]
    """<p>The name of the file being compared, including its extension and subdirectory, if any.</p>"""
    file_position: NotRequired["capo_codecommit.types.position.Position"]
    """<p>The position of a change in a compared file, in line number format.</p>"""
    relative_file_version: NotRequired[
        "capo_codecommit.types.relative_file_version_enum.RelativeFileVersionEnum"
    ]
    """<p>In a comparison of commits or a pull request, whether the change is in the before or after of that comparison.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Location) -> dict:
    out: dict = {}
    if "file_path" in value:
        out["filePath"] = value["file_path"]
    if "file_position" in value:
        out["filePosition"] = value["file_position"]
    if "relative_file_version" in value:
        import capo_codecommit.types.relative_file_version_enum

        out["relativeFileVersion"] = (
            capo_codecommit.types.relative_file_version_enum.serialize_aws_json_1_1(
                value["relative_file_version"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Location:
    out: Location = {}  # type: ignore[typeddict-item]
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    if "filePosition" in data:
        out["file_position"] = data["filePosition"]
    if "relativeFileVersion" in data:
        import capo_codecommit.types.relative_file_version_enum

        out["relative_file_version"] = (
            capo_codecommit.types.relative_file_version_enum.deserialize_aws_json_1_1(
                data["relativeFileVersion"]
            )
        )
    return out
