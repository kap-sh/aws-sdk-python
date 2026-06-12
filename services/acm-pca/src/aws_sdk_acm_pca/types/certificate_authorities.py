"""Generated from Smithy shape ``com.amazonaws.acmpca#CertificateAuthorities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.certificate_authority

CertificateAuthorities: TypeAlias = list[
    "aws_sdk_acm_pca.types.certificate_authority.CertificateAuthority"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateAuthorities) -> list:
    import aws_sdk_acm_pca.types.certificate_authority

    out: list = []
    for item in value:
        out.append(
            aws_sdk_acm_pca.types.certificate_authority.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CertificateAuthorities:
    import aws_sdk_acm_pca.types.certificate_authority

    out: CertificateAuthorities = []
    for item in data:
        out.append(
            aws_sdk_acm_pca.types.certificate_authority.deserialize_aws_json_1_1(item)
        )
    return out
