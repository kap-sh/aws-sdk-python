"""Generated from Smithy shape ``com.amazonaws.ec2#GpuDeviceInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.gpu_device_info

GpuDeviceInfoList: TypeAlias = list["aws_sdk_ec2.types.gpu_device_info.GpuDeviceInfo"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GpuDeviceInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.gpu_device_info

        aws_sdk_ec2.types.gpu_device_info.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> GpuDeviceInfoList:
    import aws_sdk_ec2.types.gpu_device_info

    out: GpuDeviceInfoList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.gpu_device_info.deserialize_ec2_query(child))
    return out
