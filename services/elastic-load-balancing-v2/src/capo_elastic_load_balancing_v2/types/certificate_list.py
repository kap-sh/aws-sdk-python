"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#CertificateList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.certificate

CertificateList: TypeAlias = list[
    "capo_elastic_load_balancing_v2.types.certificate.Certificate"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: CertificateList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.certificate

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.certificate.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> CertificateList:
    import capo_elastic_load_balancing_v2.types.certificate

    out: CertificateList = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing_v2.types.certificate.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: CertificateList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.certificate

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.certificate.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> CertificateList:
    import capo_elastic_load_balancing_v2.types.certificate

    out: CertificateList = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing_v2.types.certificate.deserialize_query(child)
        )
    return out
