"""Generated from Smithy shape ``com.amazonaws.iam#certificateListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.signing_certificate

certificateListType: TypeAlias = list[
    "capo_iam.types.signing_certificate.SigningCertificate"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: certificateListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.signing_certificate

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.signing_certificate.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> certificateListType:
    import capo_iam.types.signing_certificate

    out: certificateListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.signing_certificate.deserialize_query(child))
    return out


def serialize_query_flat(
    value: certificateListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.signing_certificate

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.signing_certificate.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> certificateListType:
    import capo_iam.types.signing_certificate

    out: certificateListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.signing_certificate.deserialize_query(child))
    return out
