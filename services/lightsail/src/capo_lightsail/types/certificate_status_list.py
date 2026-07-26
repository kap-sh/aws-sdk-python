"""Generated from Smithy shape ``com.amazonaws.lightsail#CertificateStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.certificate_status

CertificateStatusList: TypeAlias = list[
    "capo_lightsail.types.certificate_status.CertificateStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateStatusList) -> list:
    import capo_lightsail.types.certificate_status

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.certificate_status.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CertificateStatusList:
    import capo_lightsail.types.certificate_status

    out: CertificateStatusList = []
    for item in data:
        out.append(
            capo_lightsail.types.certificate_status.deserialize_aws_json_1_1(item)
        )
    return out
