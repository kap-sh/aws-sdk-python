"""Generated from Smithy shape ``com.amazonaws.redshift#HsmClientCertificateList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.hsm_client_certificate

HsmClientCertificateList: TypeAlias = list[
    "capo_redshift.types.hsm_client_certificate.HsmClientCertificate"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: HsmClientCertificateList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.hsm_client_certificate

    for n, item in enumerate(value, 1):
        capo_redshift.types.hsm_client_certificate.serialize_query(
            item, pairs, f"{prefix}.HsmClientCertificate.{n}"
        )


def deserialize_query(el: Element) -> HsmClientCertificateList:
    import capo_redshift.types.hsm_client_certificate

    out: HsmClientCertificateList = []
    for child in el.findall("HsmClientCertificate"):
        out.append(capo_redshift.types.hsm_client_certificate.deserialize_query(child))
    return out


def serialize_query_flat(
    value: HsmClientCertificateList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.hsm_client_certificate

    for n, item in enumerate(value, 1):
        capo_redshift.types.hsm_client_certificate.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> HsmClientCertificateList:
    import capo_redshift.types.hsm_client_certificate

    out: HsmClientCertificateList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.hsm_client_certificate.deserialize_query(child))
    return out
