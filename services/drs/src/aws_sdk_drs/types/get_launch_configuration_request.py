"""Generated from Smithy shape ``com.amazonaws.drs#GetLaunchConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_drs.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_drs.types.source_server_id

class GetLaunchConfigurationRequest(TypedDict):
    source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID"
    """<p>The ID of the Source Server that we want to retrieve a Launch Configuration for.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetLaunchConfigurationRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    return out


def deserialize_json(data: dict) -> GetLaunchConfigurationRequest:
    out: GetLaunchConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    else:
        raise DeserializationError("GetLaunchConfigurationRequest.source_server_id required")
    return out