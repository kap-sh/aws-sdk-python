"""Generated from Smithy shape ``com.amazonaws.redshift#CertificateAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.certificate_association

CertificateAssociationList: TypeAlias = list[
    "capo_redshift.types.certificate_association.CertificateAssociation"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: CertificateAssociationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.certificate_association

    for n, item in enumerate(value, 1):
        capo_redshift.types.certificate_association.serialize_query(
            item, pairs, f"{prefix}.CertificateAssociation.{n}"
        )


def deserialize_query(el: Element) -> CertificateAssociationList:
    import capo_redshift.types.certificate_association

    out: CertificateAssociationList = []
    for child in el.findall("CertificateAssociation"):
        out.append(capo_redshift.types.certificate_association.deserialize_query(child))
    return out


def serialize_query_flat(
    value: CertificateAssociationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.certificate_association

    for n, item in enumerate(value, 1):
        capo_redshift.types.certificate_association.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> CertificateAssociationList:
    import capo_redshift.types.certificate_association

    out: CertificateAssociationList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.certificate_association.deserialize_query(child))
    return out
