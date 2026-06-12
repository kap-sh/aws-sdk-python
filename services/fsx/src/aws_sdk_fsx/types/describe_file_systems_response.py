"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeFileSystemsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.file_systems
    import aws_sdk_fsx.types.next_token


class DescribeFileSystemsResponse(TypedDict):
    file_systems: NotRequired["aws_sdk_fsx.types.file_systems.FileSystems"]
    """<p>An array of file system descriptions.</p>"""
    next_token: NotRequired["aws_sdk_fsx.types.next_token.NextToken"]
    """<p>Present if there are more file systems than returned in the response (String). You can use the <code>NextToken</code> value in the later request to fetch the descriptions. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFileSystemsResponse) -> dict:
    out: dict = {}
    if "file_systems" in value:
        import aws_sdk_fsx.types.file_systems

        out["FileSystems"] = aws_sdk_fsx.types.file_systems.serialize_aws_json_1_1(
            value["file_systems"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFileSystemsResponse:
    out: DescribeFileSystemsResponse = {}  # type: ignore[typeddict-item]
    if "FileSystems" in data:
        import aws_sdk_fsx.types.file_systems

        out["file_systems"] = aws_sdk_fsx.types.file_systems.deserialize_aws_json_1_1(
            data["FileSystems"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
