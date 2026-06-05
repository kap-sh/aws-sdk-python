"""Generated from Smithy shape ``com.amazonaws.ec2#HostProperties``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class HostProperties(TypedDict):
    cores: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of cores on the Dedicated Host.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance type supported by the Dedicated Host. For example, <code>m5.large</code>. If the host supports multiple instance types, no <b>instanceType</b> is returned.</p>"""
    instance_family: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance family supported by the Dedicated Host. For example, <code>m5</code>.</p>"""
    sockets: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of sockets on the Dedicated Host.</p>"""
    total_v_cpus: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The total number of vCPUs on the Dedicated Host.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: HostProperties, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cores" in value:
        pairs.append((f"{prefix}.Cores", str(value["cores"])))
    if "instance_type" in value:
        pairs.append((f"{prefix}.InstanceType", str(value["instance_type"])))
    if "instance_family" in value:
        pairs.append((f"{prefix}.InstanceFamily", str(value["instance_family"])))
    if "sockets" in value:
        pairs.append((f"{prefix}.Sockets", str(value["sockets"])))
    if "total_v_cpus" in value:
        pairs.append((f"{prefix}.TotalVCpus", str(value["total_v_cpus"])))


def deserialize_ec2_query(el: Element) -> HostProperties:
    out: HostProperties = {}  # type: ignore[typeddict-item]
    child_cores = el.find("Cores")
    if child_cores is not None:
        out["cores"] = int(child_cores.text or "")
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_instance_family = el.find("InstanceFamily")
    if child_instance_family is not None:
        out["instance_family"] = str(child_instance_family.text or "")
    child_sockets = el.find("Sockets")
    if child_sockets is not None:
        out["sockets"] = int(child_sockets.text or "")
    child_total_v_cpus = el.find("TotalVCpus")
    if child_total_v_cpus is not None:
        out["total_v_cpus"] = int(child_total_v_cpus.text or "")
    return out
