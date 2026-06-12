"""Generated from Smithy shape ``com.amazonaws.drs#LaunchIntoInstanceProperties``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_drs.types.ec2_instance_id

class LaunchIntoInstanceProperties(TypedDict):
    launch_into_ec2_instance_id: NotRequired["aws_sdk_drs.types.ec2_instance_id.EC2InstanceID"]
    """<p>Optionally holds EC2 instance ID of an instance to launch into, instead of launching a new instance during drill, recovery or failback.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: LaunchIntoInstanceProperties) -> dict:
    out: dict = {}
    if "launch_into_ec2_instance_id" in value:
        out["launchIntoEC2InstanceID"] = value["launch_into_ec2_instance_id"]
    return out


def deserialize_json(data: dict) -> LaunchIntoInstanceProperties:
    out: LaunchIntoInstanceProperties = {}  # type: ignore[typeddict-item]
    if "launchIntoEC2InstanceID" in data:
        out["launch_into_ec2_instance_id"] = data["launchIntoEC2InstanceID"]
    return out