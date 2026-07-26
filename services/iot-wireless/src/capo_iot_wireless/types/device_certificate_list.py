"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeviceCertificateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.certificate_list

DeviceCertificateList: TypeAlias = list[
    "capo_iot_wireless.types.certificate_list.CertificateList"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceCertificateList) -> list:
    import capo_iot_wireless.types.certificate_list

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.certificate_list.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeviceCertificateList:
    import capo_iot_wireless.types.certificate_list

    out: DeviceCertificateList = []
    for item in data:
        out.append(capo_iot_wireless.types.certificate_list.deserialize_json(item))
    return out
