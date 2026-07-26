"""Generated from Smithy shape ``com.amazonaws.redshift#CreateHsmClientCertificateResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.hsm_client_certificate


class CreateHsmClientCertificateResult(TypedDict, closed=True):
    hsm_client_certificate: NotRequired[
        "capo_redshift.types.hsm_client_certificate.HsmClientCertificate"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateHsmClientCertificateResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "hsm_client_certificate" in value:
        import capo_redshift.types.hsm_client_certificate

        capo_redshift.types.hsm_client_certificate.serialize_query(
            value["hsm_client_certificate"], pairs, f"{prefix}.HsmClientCertificate"
        )


def deserialize_query(el: Element) -> CreateHsmClientCertificateResult:
    out: CreateHsmClientCertificateResult = {}  # type: ignore[typeddict-item]
    child_hsm_client_certificate = el.find("HsmClientCertificate")
    if child_hsm_client_certificate is not None:
        import capo_redshift.types.hsm_client_certificate

        out["hsm_client_certificate"] = (
            capo_redshift.types.hsm_client_certificate.deserialize_query(
                child_hsm_client_certificate
            )
        )
    return out
