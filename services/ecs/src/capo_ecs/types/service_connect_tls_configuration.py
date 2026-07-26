"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectTlsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.service_connect_tls_certificate_authority
    import capo_ecs.types.string


class ServiceConnectTlsConfiguration(TypedDict, closed=True):
    issuer_certificate_authority: "capo_ecs.types.service_connect_tls_certificate_authority.ServiceConnectTlsCertificateAuthority"
    """<p>The signer certificate authority.</p>"""
    kms_key: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Web Services Key Management Service key.</p>"""
    role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that's associated with the Service Connect TLS.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceConnectTlsConfiguration) -> dict:
    out: dict = {}
    import capo_ecs.types.service_connect_tls_certificate_authority

    out["issuerCertificateAuthority"] = (
        capo_ecs.types.service_connect_tls_certificate_authority.serialize_aws_json_1_1(
            value["issuer_certificate_authority"]
        )
    )
    if "kms_key" in value:
        out["kmsKey"] = value["kms_key"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceConnectTlsConfiguration:
    out: ServiceConnectTlsConfiguration = {}  # type: ignore[typeddict-item]
    if "issuerCertificateAuthority" in data:
        import capo_ecs.types.service_connect_tls_certificate_authority

        out["issuer_certificate_authority"] = (
            capo_ecs.types.service_connect_tls_certificate_authority.deserialize_aws_json_1_1(
                data["issuerCertificateAuthority"]
            )
        )
    else:
        raise DeserializationError(
            "ServiceConnectTlsConfiguration.issuer_certificate_authority required"
        )
    if "kmsKey" in data:
        out["kms_key"] = data["kmsKey"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    return out
