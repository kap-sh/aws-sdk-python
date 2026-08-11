"""Generated from Smithy shape ``com.amazonaws.ec2#InferenceDeviceInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.inference_device_info

InferenceDeviceInfoList: TypeAlias = list[
    "capo_ec2.types.inference_device_info.InferenceDeviceInfo"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InferenceDeviceInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.inference_device_info

        capo_ec2.types.inference_device_info.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> InferenceDeviceInfoList:
    import capo_ec2.types.inference_device_info

    out: InferenceDeviceInfoList = []
    for child in el.findall("member"):
        out.append(capo_ec2.types.inference_device_info.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> InferenceDeviceInfoList:
    import capo_ec2.types.inference_device_info

    out: InferenceDeviceInfoList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.inference_device_info.deserialize_ec2_query(child))
    return out
