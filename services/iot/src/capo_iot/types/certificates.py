"""Generated from Smithy shape ``com.amazonaws.iot#Certificates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.certificate

Certificates: TypeAlias = list["capo_iot.types.certificate.Certificate"]


# --- restJson1 ser/de ---
def serialize_json(value: Certificates) -> list:
    import capo_iot.types.certificate

    out: list = []
    for item in value:
        out.append(capo_iot.types.certificate.serialize_json(item))
    return out


def deserialize_json(data: list) -> Certificates:
    import capo_iot.types.certificate

    out: Certificates = []
    for item in data:
        out.append(capo_iot.types.certificate.deserialize_json(item))
    return out
