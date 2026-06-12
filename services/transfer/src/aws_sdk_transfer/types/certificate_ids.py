"""Generated from Smithy shape ``com.amazonaws.transfer#CertificateIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transfer.types.certificate_id

CertificateIds: TypeAlias = list["aws_sdk_transfer.types.certificate_id.CertificateId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CertificateIds:
    return list(data)
