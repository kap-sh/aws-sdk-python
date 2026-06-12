"""Generated from Smithy shape ``com.amazonaws.redshift#CertificateAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.certificate_association

CertificateAssociationList: TypeAlias = list[
    "aws_sdk_redshift.types.certificate_association.CertificateAssociation"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: CertificateAssociationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.certificate_association

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.certificate_association.serialize_query(
            item, pairs, f"{prefix}.CertificateAssociation.{n}"
        )


def deserialize_query(el: Element) -> CertificateAssociationList:
    import aws_sdk_redshift.types.certificate_association

    out: CertificateAssociationList = []
    for child in el.findall("CertificateAssociation"):
        out.append(
            aws_sdk_redshift.types.certificate_association.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: CertificateAssociationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.certificate_association

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.certificate_association.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> CertificateAssociationList:
    import aws_sdk_redshift.types.certificate_association

    out: CertificateAssociationList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_redshift.types.certificate_association.deserialize_query(child)
        )
    return out
