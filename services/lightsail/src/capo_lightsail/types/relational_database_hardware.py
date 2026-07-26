"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabaseHardware``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.float
    import capo_lightsail.types.integer


class RelationalDatabaseHardware(TypedDict, closed=True):
    cpu_count: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The number of vCPUs for the database.</p>"""
    disk_size_in_gb: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The size of the disk for the database.</p>"""
    ram_size_in_gb: NotRequired["capo_lightsail.types.float.float"]
    """<p>The amount of RAM in GB for the database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabaseHardware) -> dict:
    out: dict = {}
    if "cpu_count" in value:
        out["cpuCount"] = value["cpu_count"]
    if "disk_size_in_gb" in value:
        out["diskSizeInGb"] = value["disk_size_in_gb"]
    if "ram_size_in_gb" in value:
        out["ramSizeInGb"] = value["ram_size_in_gb"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RelationalDatabaseHardware:
    out: RelationalDatabaseHardware = {}  # type: ignore[typeddict-item]
    if "cpuCount" in data:
        out["cpu_count"] = data["cpuCount"]
    if "diskSizeInGb" in data:
        out["disk_size_in_gb"] = data["diskSizeInGb"]
    if "ramSizeInGb" in data:
        out["ram_size_in_gb"] = data["ramSizeInGb"]
    return out
