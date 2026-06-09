"""Generated from Smithy shape ``com.amazonaws.ec2#DiskInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disk_info

DiskInfoList: TypeAlias = list["aws_sdk_ec2.types.disk_info.DiskInfo"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DiskInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.disk_info

        aws_sdk_ec2.types.disk_info.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> DiskInfoList:
    import aws_sdk_ec2.types.disk_info

    out: DiskInfoList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.disk_info.deserialize_ec2_query(child))
    return out
