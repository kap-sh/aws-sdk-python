"""Generated from Smithy shape ``com.amazonaws.rtbfabric#TrustStoreConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.certificate_authority_certificates


class TrustStoreConfiguration(TypedDict, closed=True):
    certificate_authority_certificates: "capo_rtbfabric.types.certificate_authority_certificates.CertificateAuthorityCertificates"
    """<p>The certificate authority certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrustStoreConfiguration) -> dict:
    out: dict = {}
    import capo_rtbfabric.types.certificate_authority_certificates

    out["certificateAuthorityCertificates"] = (
        capo_rtbfabric.types.certificate_authority_certificates.serialize_json(
            value["certificate_authority_certificates"]
        )
    )
    return out


def deserialize_json(data: dict) -> TrustStoreConfiguration:
    out: TrustStoreConfiguration = {}  # type: ignore[typeddict-item]
    if "certificateAuthorityCertificates" in data:
        import capo_rtbfabric.types.certificate_authority_certificates

        out["certificate_authority_certificates"] = (
            capo_rtbfabric.types.certificate_authority_certificates.deserialize_json(
                data["certificateAuthorityCertificates"]
            )
        )
    else:
        raise DeserializationError(
            "TrustStoreConfiguration.certificate_authority_certificates required"
        )
    return out
