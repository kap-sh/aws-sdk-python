"""Generated from Smithy shape ``com.amazonaws.acm#CertificateStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm.types.certificate_status

CertificateStatuses: TypeAlias = list[
    "capo_acm.types.certificate_status.CertificateStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateStatuses) -> list:
    import capo_acm.types.certificate_status

    out: list = []
    for item in value:
        out.append(capo_acm.types.certificate_status.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CertificateStatuses:
    import capo_acm.types.certificate_status

    out: CertificateStatuses = []
    for item in data:
        out.append(capo_acm.types.certificate_status.deserialize_aws_json_1_1(item))
    return out
