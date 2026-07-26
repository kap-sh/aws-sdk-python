"""Generated from Smithy shape ``com.amazonaws.iotwireless#PrivateKeysList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.certificate_list

PrivateKeysList: TypeAlias = list[
    "capo_iot_wireless.types.certificate_list.CertificateList"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivateKeysList) -> list:
    import capo_iot_wireless.types.certificate_list

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.certificate_list.serialize_json(item))
    return out


def deserialize_json(data: list) -> PrivateKeysList:
    import capo_iot_wireless.types.certificate_list

    out: PrivateKeysList = []
    for item in data:
        out.append(capo_iot_wireless.types.certificate_list.deserialize_json(item))
    return out
