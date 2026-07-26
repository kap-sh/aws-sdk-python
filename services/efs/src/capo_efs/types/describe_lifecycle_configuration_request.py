"""Generated from Smithy shape ``com.amazonaws.efs#DescribeLifecycleConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_efs.types.file_system_id


class DescribeLifecycleConfigurationRequest(TypedDict, closed=True):
    file_system_id: "capo_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the file system whose <code>LifecycleConfiguration</code> object you want to retrieve (String).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeLifecycleConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeLifecycleConfigurationRequest:
    out: DescribeLifecycleConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
