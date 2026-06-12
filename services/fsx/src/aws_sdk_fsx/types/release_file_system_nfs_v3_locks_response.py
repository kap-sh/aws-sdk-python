"""Generated from Smithy shape ``com.amazonaws.fsx#ReleaseFileSystemNfsV3LocksResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.file_system


class ReleaseFileSystemNfsV3LocksResponse(TypedDict):
    file_system: NotRequired["aws_sdk_fsx.types.file_system.FileSystem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReleaseFileSystemNfsV3LocksResponse) -> dict:
    out: dict = {}
    if "file_system" in value:
        import aws_sdk_fsx.types.file_system

        out["FileSystem"] = aws_sdk_fsx.types.file_system.serialize_aws_json_1_1(
            value["file_system"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReleaseFileSystemNfsV3LocksResponse:
    out: ReleaseFileSystemNfsV3LocksResponse = {}  # type: ignore[typeddict-item]
    if "FileSystem" in data:
        import aws_sdk_fsx.types.file_system

        out["file_system"] = aws_sdk_fsx.types.file_system.deserialize_aws_json_1_1(
            data["FileSystem"]
        )
    return out
