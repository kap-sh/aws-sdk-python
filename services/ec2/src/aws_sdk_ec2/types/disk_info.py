"""Generated from Smithy shape ``com.amazonaws.ec2#DiskInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disk_count
    import aws_sdk_ec2.types.disk_size
    import aws_sdk_ec2.types.disk_type


class DiskInfo(TypedDict):
    size_in_gb: NotRequired["aws_sdk_ec2.types.disk_size.DiskSize"]
    """<p>The size of the disk in GB.</p>"""
    count: NotRequired["aws_sdk_ec2.types.disk_count.DiskCount"]
    """<p>The number of disks with this configuration.</p>"""
    type: NotRequired["aws_sdk_ec2.types.disk_type.DiskType"]
    """<p>The type of disk.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DiskInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "size_in_gb" in value:
        pairs.append((f"{prefix}.SizeInGB", str(value["size_in_gb"])))
    if "count" in value:
        pairs.append((f"{prefix}.Count", str(value["count"])))
    if "type" in value:
        import aws_sdk_ec2.types.disk_type

        aws_sdk_ec2.types.disk_type.serialize_ec2_query(
            value["type"], pairs, f"{prefix}.Type"
        )


def deserialize_ec2_query(el: Element) -> DiskInfo:
    out: DiskInfo = {}  # type: ignore[typeddict-item]
    child_size_in_gb = el.find("SizeInGB")
    if child_size_in_gb is not None:
        out["size_in_gb"] = int(child_size_in_gb.text or "")
    child_count = el.find("Count")
    if child_count is not None:
        out["count"] = int(child_count.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_ec2.types.disk_type

        out["type"] = aws_sdk_ec2.types.disk_type.deserialize_ec2_query(child_type)
    return out
