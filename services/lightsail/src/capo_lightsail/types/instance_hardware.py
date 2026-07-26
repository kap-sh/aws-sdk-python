"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceHardware``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.disk_list
    import capo_lightsail.types.float
    import capo_lightsail.types.integer


class InstanceHardware(TypedDict, closed=True):
    cpu_count: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The number of vCPUs the instance has.</p>"""
    disks: NotRequired["capo_lightsail.types.disk_list.DiskList"]
    """<p>The disks attached to the instance.</p>"""
    ram_size_in_gb: NotRequired["capo_lightsail.types.float.float"]
    """<p>The amount of RAM in GB on the instance (<code>1.0</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceHardware) -> dict:
    out: dict = {}
    if "cpu_count" in value:
        out["cpuCount"] = value["cpu_count"]
    if "disks" in value:
        import capo_lightsail.types.disk_list

        out["disks"] = capo_lightsail.types.disk_list.serialize_aws_json_1_1(
            value["disks"]
        )
    if "ram_size_in_gb" in value:
        out["ramSizeInGb"] = value["ram_size_in_gb"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceHardware:
    out: InstanceHardware = {}  # type: ignore[typeddict-item]
    if "cpuCount" in data:
        out["cpu_count"] = data["cpuCount"]
    if "disks" in data:
        import capo_lightsail.types.disk_list

        out["disks"] = capo_lightsail.types.disk_list.deserialize_aws_json_1_1(
            data["disks"]
        )
    if "ramSizeInGb" in data:
        out["ram_size_in_gb"] = data["ramSizeInGb"]
    return out
