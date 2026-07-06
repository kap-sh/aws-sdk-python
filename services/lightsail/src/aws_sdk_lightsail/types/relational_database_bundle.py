"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabaseBundle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.float
    import aws_sdk_lightsail.types.integer
    import aws_sdk_lightsail.types.string


class RelationalDatabaseBundle(TypedDict, closed=True):
    bundle_id: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The ID for the database bundle.</p>"""
    name: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The name for the database bundle.</p>"""
    price: NotRequired["aws_sdk_lightsail.types.float.float"]
    """<p>The cost of the database bundle in US currency.</p>"""
    ram_size_in_gb: NotRequired["aws_sdk_lightsail.types.float.float"]
    """<p>The amount of RAM in GB (for example, <code>2.0</code>) for the database bundle.</p>"""
    disk_size_in_gb: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The size of the disk for the database bundle.</p>"""
    transfer_per_month_in_gb: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The data transfer rate per month in GB for the database bundle.</p>"""
    cpu_count: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The number of virtual CPUs (vCPUs) for the database bundle.</p>"""
    is_encrypted: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether the database bundle is encrypted.</p>"""
    is_active: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether the database bundle is active.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabaseBundle) -> dict:
    out: dict = {}
    if "bundle_id" in value:
        out["bundleId"] = value["bundle_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "price" in value:
        out["price"] = value["price"]
    if "ram_size_in_gb" in value:
        out["ramSizeInGb"] = value["ram_size_in_gb"]
    if "disk_size_in_gb" in value:
        out["diskSizeInGb"] = value["disk_size_in_gb"]
    if "transfer_per_month_in_gb" in value:
        out["transferPerMonthInGb"] = value["transfer_per_month_in_gb"]
    if "cpu_count" in value:
        out["cpuCount"] = value["cpu_count"]
    if "is_encrypted" in value:
        out["isEncrypted"] = value["is_encrypted"]
    if "is_active" in value:
        out["isActive"] = value["is_active"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RelationalDatabaseBundle:
    out: RelationalDatabaseBundle = {}  # type: ignore[typeddict-item]
    if "bundleId" in data:
        out["bundle_id"] = data["bundleId"]
    if "name" in data:
        out["name"] = data["name"]
    if "price" in data:
        out["price"] = data["price"]
    if "ramSizeInGb" in data:
        out["ram_size_in_gb"] = data["ramSizeInGb"]
    if "diskSizeInGb" in data:
        out["disk_size_in_gb"] = data["diskSizeInGb"]
    if "transferPerMonthInGb" in data:
        out["transfer_per_month_in_gb"] = data["transferPerMonthInGb"]
    if "cpuCount" in data:
        out["cpu_count"] = data["cpuCount"]
    if "isEncrypted" in data:
        out["is_encrypted"] = data["isEncrypted"]
    if "isActive" in data:
        out["is_active"] = data["isActive"]
    return out
