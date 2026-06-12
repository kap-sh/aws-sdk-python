"""Generated from Smithy shape ``com.amazonaws.efs#DescribeLifecycleConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_efs.types.file_system_id


class DescribeLifecycleConfigurationRequest(TypedDict):
    file_system_id: "aws_sdk_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the file system whose <code>LifecycleConfiguration</code> object you want to retrieve (String).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeLifecycleConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeLifecycleConfigurationRequest:
    out: DescribeLifecycleConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
