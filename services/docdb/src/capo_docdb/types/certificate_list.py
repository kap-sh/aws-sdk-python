"""Generated from Smithy shape ``com.amazonaws.docdb#CertificateList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.certificate

CertificateList: TypeAlias = list["capo_docdb.types.certificate.Certificate"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CertificateList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_docdb.types.certificate

    for n, item in enumerate(value, 1):
        capo_docdb.types.certificate.serialize_query(
            item, pairs, f"{prefix}.Certificate.{n}"
        )


def deserialize_query(el: Element) -> CertificateList:
    import capo_docdb.types.certificate

    out: CertificateList = []
    for child in el.findall("Certificate"):
        out.append(capo_docdb.types.certificate.deserialize_query(child))
    return out


def serialize_query_flat(
    value: CertificateList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_docdb.types.certificate

    for n, item in enumerate(value, 1):
        capo_docdb.types.certificate.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> CertificateList:
    import capo_docdb.types.certificate

    out: CertificateList = []
    for child in parent.findall(tag):
        out.append(capo_docdb.types.certificate.deserialize_query(child))
    return out
