"""Generated from Smithy shape ``com.amazonaws.efs#DescribeFileSystemsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_efs.types.file_system_descriptions
    import aws_sdk_efs.types.marker


class DescribeFileSystemsResponse(TypedDict):
    marker: NotRequired["aws_sdk_efs.types.marker.Marker"]
    """<p>Present if provided by caller in the request (String).</p>"""
    file_systems: NotRequired[
        "aws_sdk_efs.types.file_system_descriptions.FileSystemDescriptions"
    ]
    """<p>An array of file system descriptions.</p>"""
    next_marker: NotRequired["aws_sdk_efs.types.marker.Marker"]
    """<p>Present if there are more file systems than returned in the response (String). You can use the <code>NextMarker</code> in the subsequent request to fetch the descriptions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFileSystemsResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "file_systems" in value:
        import aws_sdk_efs.types.file_system_descriptions

        out["FileSystems"] = aws_sdk_efs.types.file_system_descriptions.serialize_json(
            value["file_systems"]
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> DescribeFileSystemsResponse:
    out: DescribeFileSystemsResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "FileSystems" in data:
        import aws_sdk_efs.types.file_system_descriptions

        out["file_systems"] = (
            aws_sdk_efs.types.file_system_descriptions.deserialize_json(
                data["FileSystems"]
            )
        )
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    return out
