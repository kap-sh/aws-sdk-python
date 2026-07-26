"""Generated from Smithy shape ``com.amazonaws.emrcontainers#InTransitEncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.tls_certificate_configuration


class InTransitEncryptionConfiguration(TypedDict, closed=True):
    tls_certificate_configuration: NotRequired[
        "capo_emr_containers.types.tls_certificate_configuration.TLSCertificateConfiguration"
    ]
    """<p>TLS certificate-related configuration input for the security configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InTransitEncryptionConfiguration) -> dict:
    out: dict = {}
    if "tls_certificate_configuration" in value:
        import capo_emr_containers.types.tls_certificate_configuration

        out["tlsCertificateConfiguration"] = (
            capo_emr_containers.types.tls_certificate_configuration.serialize_json(
                value["tls_certificate_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> InTransitEncryptionConfiguration:
    out: InTransitEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "tlsCertificateConfiguration" in data:
        import capo_emr_containers.types.tls_certificate_configuration

        out["tls_certificate_configuration"] = (
            capo_emr_containers.types.tls_certificate_configuration.deserialize_json(
                data["tlsCertificateConfiguration"]
            )
        )
    return out
