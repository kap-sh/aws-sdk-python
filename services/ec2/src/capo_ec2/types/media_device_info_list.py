"""Generated from Smithy shape ``com.amazonaws.ec2#MediaDeviceInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.media_device_info

MediaDeviceInfoList: TypeAlias = list[
    "capo_ec2.types.media_device_info.MediaDeviceInfo"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MediaDeviceInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.media_device_info

        capo_ec2.types.media_device_info.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> MediaDeviceInfoList:
    import capo_ec2.types.media_device_info

    out: MediaDeviceInfoList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.media_device_info.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> MediaDeviceInfoList:
    import capo_ec2.types.media_device_info

    out: MediaDeviceInfoList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.media_device_info.deserialize_ec2_query(child))
    return out
