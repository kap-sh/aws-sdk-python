"""Generated from Smithy shape ``com.amazonaws.iot#CACertificates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.ca_certificate

CACertificates: TypeAlias = list["aws_sdk_iot.types.ca_certificate.CACertificate"]


# --- restJson1 ser/de ---
def serialize_json(value: CACertificates) -> list:
    import aws_sdk_iot.types.ca_certificate

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.ca_certificate.serialize_json(item))
    return out


def deserialize_json(data: list) -> CACertificates:
    import aws_sdk_iot.types.ca_certificate

    out: CACertificates = []
    for item in data:
        out.append(aws_sdk_iot.types.ca_certificate.deserialize_json(item))
    return out
