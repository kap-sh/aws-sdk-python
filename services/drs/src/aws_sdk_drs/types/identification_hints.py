"""Generated from Smithy shape ``com.amazonaws.drs#IdentificationHints``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_drs.types.bounded_string
    import aws_sdk_drs.types.ec2_instance_id

class IdentificationHints(TypedDict):
    fqdn: NotRequired["aws_sdk_drs.types.bounded_string.BoundedString"]
    """<p>Fully Qualified Domain Name identification hint.</p>"""
    hostname: NotRequired["aws_sdk_drs.types.bounded_string.BoundedString"]
    """<p>Hostname identification hint.</p>"""
    vm_ware_uuid: NotRequired["aws_sdk_drs.types.bounded_string.BoundedString"]
    """<p>vCenter VM path identification hint.</p>"""
    aws_instance_id: NotRequired["aws_sdk_drs.types.ec2_instance_id.EC2InstanceID"]
    """<p>AWS Instance ID identification hint.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: IdentificationHints) -> dict:
    out: dict = {}
    if "fqdn" in value:
        out["fqdn"] = value["fqdn"]
    if "hostname" in value:
        out["hostname"] = value["hostname"]
    if "vm_ware_uuid" in value:
        out["vmWareUuid"] = value["vm_ware_uuid"]
    if "aws_instance_id" in value:
        out["awsInstanceID"] = value["aws_instance_id"]
    return out


def deserialize_json(data: dict) -> IdentificationHints:
    out: IdentificationHints = {}  # type: ignore[typeddict-item]
    if "fqdn" in data:
        out["fqdn"] = data["fqdn"]
    if "hostname" in data:
        out["hostname"] = data["hostname"]
    if "vmWareUuid" in data:
        out["vm_ware_uuid"] = data["vmWareUuid"]
    if "awsInstanceID" in data:
        out["aws_instance_id"] = data["awsInstanceID"]
    return out