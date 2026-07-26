"""Generated from Smithy shape ``com.amazonaws.iot#CACertificates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.ca_certificate

CACertificates: TypeAlias = list["capo_iot.types.ca_certificate.CACertificate"]


# --- restJson1 ser/de ---
def serialize_json(value: CACertificates) -> list:
    import capo_iot.types.ca_certificate

    out: list = []
    for item in value:
        out.append(capo_iot.types.ca_certificate.serialize_json(item))
    return out


def deserialize_json(data: list) -> CACertificates:
    import capo_iot.types.ca_certificate

    out: CACertificates = []
    for item in data:
        out.append(capo_iot.types.ca_certificate.deserialize_json(item))
    return out
