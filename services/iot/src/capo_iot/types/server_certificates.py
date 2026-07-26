"""Generated from Smithy shape ``com.amazonaws.iot#ServerCertificates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.server_certificate_summary

ServerCertificates: TypeAlias = list[
    "capo_iot.types.server_certificate_summary.ServerCertificateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServerCertificates) -> list:
    import capo_iot.types.server_certificate_summary

    out: list = []
    for item in value:
        out.append(capo_iot.types.server_certificate_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServerCertificates:
    import capo_iot.types.server_certificate_summary

    out: ServerCertificates = []
    for item in data:
        out.append(capo_iot.types.server_certificate_summary.deserialize_json(item))
    return out
