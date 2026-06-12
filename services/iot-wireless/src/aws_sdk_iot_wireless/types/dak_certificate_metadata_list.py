"""Generated from Smithy shape ``com.amazonaws.iotwireless#DakCertificateMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.dak_certificate_metadata

DakCertificateMetadataList: TypeAlias = list[
    "aws_sdk_iot_wireless.types.dak_certificate_metadata.DakCertificateMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: DakCertificateMetadataList) -> list:
    import aws_sdk_iot_wireless.types.dak_certificate_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_wireless.types.dak_certificate_metadata.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DakCertificateMetadataList:
    import aws_sdk_iot_wireless.types.dak_certificate_metadata

    out: DakCertificateMetadataList = []
    for item in data:
        out.append(
            aws_sdk_iot_wireless.types.dak_certificate_metadata.deserialize_json(item)
        )
    return out
