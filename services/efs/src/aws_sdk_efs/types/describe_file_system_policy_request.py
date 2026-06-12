"""Generated from Smithy shape ``com.amazonaws.efs#DescribeFileSystemPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_efs.types.file_system_id


class DescribeFileSystemPolicyRequest(TypedDict):
    file_system_id: "aws_sdk_efs.types.file_system_id.FileSystemId"
    """<p>Specifies which EFS file system to retrieve the <code>FileSystemPolicy</code> for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFileSystemPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeFileSystemPolicyRequest:
    out: DescribeFileSystemPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
