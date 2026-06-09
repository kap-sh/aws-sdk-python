"""Generated from Smithy shape ``com.amazonaws.iam#serverCertificateMetadataListType``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.server_certificate_metadata

serverCertificateMetadataListType: TypeAlias = list[
    "aws_sdk_iam.types.server_certificate_metadata.ServerCertificateMetadata"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: serverCertificateMetadataListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.server_certificate_metadata

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.server_certificate_metadata.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> serverCertificateMetadataListType:
    import aws_sdk_iam.types.server_certificate_metadata

    out: serverCertificateMetadataListType = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_iam.types.server_certificate_metadata.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: serverCertificateMetadataListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.server_certificate_metadata

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.server_certificate_metadata.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> serverCertificateMetadataListType:
    import aws_sdk_iam.types.server_certificate_metadata

    out: serverCertificateMetadataListType = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_iam.types.server_certificate_metadata.deserialize_query(child)
        )
    return out
