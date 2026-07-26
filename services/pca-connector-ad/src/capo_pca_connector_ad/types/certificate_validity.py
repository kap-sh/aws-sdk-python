"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#CertificateValidity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pca_connector_ad.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.validity_period


class CertificateValidity(TypedDict, closed=True):
    validity_period: "capo_pca_connector_ad.types.validity_period.ValidityPeriod"
    """<p>Information describing the end of the validity period of the certificate. This parameter sets the “Not After” date for the certificate. Certificate validity is the period of time during which a certificate is valid. Validity can be expressed as an explicit date and time when the certificate expires, or as a span of time after issuance, stated in days, months, or years. For more information, see Validity in RFC 5280. This value is unaffected when ValidityNotBefore is also specified. For example, if Validity is set to 20 days in the future, the certificate will expire 20 days from issuance time regardless of the ValidityNotBefore value.</p>"""
    renewal_period: "capo_pca_connector_ad.types.validity_period.ValidityPeriod"
    """<p>Renewal period is the period of time before certificate expiration when a new certificate will be requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CertificateValidity) -> dict:
    out: dict = {}
    import capo_pca_connector_ad.types.validity_period

    out["ValidityPeriod"] = capo_pca_connector_ad.types.validity_period.serialize_json(
        value["validity_period"]
    )
    import capo_pca_connector_ad.types.validity_period

    out["RenewalPeriod"] = capo_pca_connector_ad.types.validity_period.serialize_json(
        value["renewal_period"]
    )
    return out


def deserialize_json(data: dict) -> CertificateValidity:
    out: CertificateValidity = {}  # type: ignore[typeddict-item]
    if "ValidityPeriod" in data:
        import capo_pca_connector_ad.types.validity_period

        out["validity_period"] = (
            capo_pca_connector_ad.types.validity_period.deserialize_json(
                data["ValidityPeriod"]
            )
        )
    else:
        raise DeserializationError("CertificateValidity.validity_period required")
    if "RenewalPeriod" in data:
        import capo_pca_connector_ad.types.validity_period

        out["renewal_period"] = (
            capo_pca_connector_ad.types.validity_period.deserialize_json(
                data["RenewalPeriod"]
            )
        )
    else:
        raise DeserializationError("CertificateValidity.renewal_period required")
    return out
