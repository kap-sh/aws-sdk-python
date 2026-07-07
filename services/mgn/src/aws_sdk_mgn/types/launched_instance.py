"""Generated from Smithy shape ``com.amazonaws.mgn#LaunchedInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.ec2_instance_id
    import aws_sdk_mgn.types.first_boot
    import aws_sdk_mgn.types.job_id


class LaunchedInstance(TypedDict, closed=True):
    ec2_instance_id: NotRequired["aws_sdk_mgn.types.ec2_instance_id.EC2InstanceID"]
    """<p>Launched instance EC2 ID.</p>"""
    job_id: NotRequired["aws_sdk_mgn.types.job_id.JobID"]
    """<p>Launched instance Job ID.</p>"""
    first_boot: NotRequired["aws_sdk_mgn.types.first_boot.FirstBoot"]
    """<p>Launched instance first boot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LaunchedInstance) -> dict:
    out: dict = {}
    if "ec2_instance_id" in value:
        out["ec2InstanceID"] = value["ec2_instance_id"]
    if "job_id" in value:
        out["jobID"] = value["job_id"]
    if "first_boot" in value:
        out["firstBoot"] = value["first_boot"]
    return out


def deserialize_json(data: dict) -> LaunchedInstance:
    out: LaunchedInstance = {}  # type: ignore[typeddict-item]
    if "ec2InstanceID" in data:
        out["ec2_instance_id"] = data["ec2InstanceID"]
    if "jobID" in data:
        out["job_id"] = data["jobID"]
    if "firstBoot" in data:
        out["first_boot"] = data["firstBoot"]
    return out
