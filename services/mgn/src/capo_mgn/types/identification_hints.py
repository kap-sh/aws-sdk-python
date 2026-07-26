"""Generated from Smithy shape ``com.amazonaws.mgn#IdentificationHints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.bounded_string
    import capo_mgn.types.ec2_instance_id


class IdentificationHints(TypedDict, closed=True):
    fqdn: NotRequired["capo_mgn.types.bounded_string.BoundedString"]
    """<p>FQDN address identification hint.</p>"""
    hostname: NotRequired["capo_mgn.types.bounded_string.BoundedString"]
    """<p>Hostname identification hint.</p>"""
    vm_ware_uuid: NotRequired["capo_mgn.types.bounded_string.BoundedString"]
    """<p>vmWare UUID identification hint.</p>"""
    aws_instance_id: NotRequired["capo_mgn.types.ec2_instance_id.EC2InstanceID"]
    """<p>AWS Instance ID identification hint.</p>"""
    vm_path: NotRequired["capo_mgn.types.bounded_string.BoundedString"]
    """<p>vCenter VM path identification hint.</p>"""


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
    if "vm_path" in value:
        out["vmPath"] = value["vm_path"]
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
    if "vmPath" in data:
        out["vm_path"] = data["vmPath"]
    return out
