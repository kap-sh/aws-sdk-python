"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectorySizeUpdateSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_size


class DirectorySizeUpdateSettings(TypedDict):
    directory_size: NotRequired[
        "aws_sdk_directory_service.types.directory_size.DirectorySize"
    ]
    """<p>The target directory size for the update operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectorySizeUpdateSettings) -> dict:
    out: dict = {}
    if "directory_size" in value:
        import aws_sdk_directory_service.types.directory_size

        out["DirectorySize"] = (
            aws_sdk_directory_service.types.directory_size.serialize_aws_json_1_1(
                value["directory_size"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectorySizeUpdateSettings:
    out: DirectorySizeUpdateSettings = {}  # type: ignore[typeddict-item]
    if "DirectorySize" in data:
        import aws_sdk_directory_service.types.directory_size

        out["directory_size"] = (
            aws_sdk_directory_service.types.directory_size.deserialize_aws_json_1_1(
                data["DirectorySize"]
            )
        )
    return out
