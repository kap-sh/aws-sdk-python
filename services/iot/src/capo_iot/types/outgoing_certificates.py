"""Generated from Smithy shape ``com.amazonaws.iot#OutgoingCertificates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.outgoing_certificate

OutgoingCertificates: TypeAlias = list[
    "capo_iot.types.outgoing_certificate.OutgoingCertificate"
]


# --- restJson1 ser/de ---
def serialize_json(value: OutgoingCertificates) -> list:
    import capo_iot.types.outgoing_certificate

    out: list = []
    for item in value:
        out.append(capo_iot.types.outgoing_certificate.serialize_json(item))
    return out


def deserialize_json(data: list) -> OutgoingCertificates:
    import capo_iot.types.outgoing_certificate

    out: OutgoingCertificates = []
    for item in data:
        out.append(capo_iot.types.outgoing_certificate.deserialize_json(item))
    return out
