"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanEc2InstanceWithFindings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.boolean


class ScanEc2InstanceWithFindings(TypedDict, closed=True):
    ebs_volumes: NotRequired["aws_sdk_guardduty.types.boolean.Boolean"]
    """<p>Describes the configuration for scanning EBS volumes as data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanEc2InstanceWithFindings) -> dict:
    out: dict = {}
    if "ebs_volumes" in value:
        out["ebsVolumes"] = value["ebs_volumes"]
    return out


def deserialize_json(data: dict) -> ScanEc2InstanceWithFindings:
    out: ScanEc2InstanceWithFindings = {}  # type: ignore[typeddict-item]
    if "ebsVolumes" in data:
        out["ebs_volumes"] = data["ebsVolumes"]
    return out
