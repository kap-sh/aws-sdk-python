"""Generated from Smithy shape ``com.amazonaws.acm#CertificateMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_acm.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_acm.types.acm_certificate_metadata


class _CertificateMetadata_AcmCertificateMetadata(TypedDict, closed=True):
    AcmCertificateMetadata: (
        "aws_sdk_acm.types.acm_certificate_metadata.AcmCertificateMetadata"
    )


CertificateMetadata: TypeAlias = _CertificateMetadata_AcmCertificateMetadata


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateMetadata) -> dict:
    if "AcmCertificateMetadata" in value:
        import aws_sdk_acm.types.acm_certificate_metadata

        return {
            "AcmCertificateMetadata": aws_sdk_acm.types.acm_certificate_metadata.serialize_aws_json_1_1(
                value["AcmCertificateMetadata"]
            )
        }
    else:
        raise SerializationError("CertificateMetadata: no variant present")


def deserialize_aws_json_1_1(data: dict) -> CertificateMetadata:
    if "AcmCertificateMetadata" in data:
        import aws_sdk_acm.types.acm_certificate_metadata

        return {
            "AcmCertificateMetadata": aws_sdk_acm.types.acm_certificate_metadata.deserialize_aws_json_1_1(
                data["AcmCertificateMetadata"]
            )
        }
    else:
        raise DeserializationError("CertificateMetadata: no recognized variant key")
