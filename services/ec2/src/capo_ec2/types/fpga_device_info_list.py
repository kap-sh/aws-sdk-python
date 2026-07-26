"""Generated from Smithy shape ``com.amazonaws.ec2#FpgaDeviceInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fpga_device_info

FpgaDeviceInfoList: TypeAlias = list["capo_ec2.types.fpga_device_info.FpgaDeviceInfo"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FpgaDeviceInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.fpga_device_info

        capo_ec2.types.fpga_device_info.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> FpgaDeviceInfoList:
    import capo_ec2.types.fpga_device_info

    out: FpgaDeviceInfoList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.fpga_device_info.deserialize_ec2_query(child))
    return out
