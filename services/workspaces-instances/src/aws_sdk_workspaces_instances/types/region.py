"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#Region``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.region_name

class Region(TypedDict):
    region_name: NotRequired["aws_sdk_workspaces_instances.types.region_name.RegionName"]
    """<p>Name of the AWS region.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Region) -> dict:
    out: dict = {}
    if "region_name" in value:
        out["RegionName"] = value["region_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Region:
    out: Region = {}  # type: ignore[typeddict-item]
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    return out