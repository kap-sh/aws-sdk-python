"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RevocationContents``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.revocation_content

RevocationContents: TypeAlias = list[
    "capo_elastic_load_balancing_v2.types.revocation_content.RevocationContent"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: RevocationContents, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.revocation_content

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.revocation_content.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> RevocationContents:
    import capo_elastic_load_balancing_v2.types.revocation_content

    out: RevocationContents = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing_v2.types.revocation_content.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: RevocationContents, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.revocation_content

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.revocation_content.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> RevocationContents:
    import capo_elastic_load_balancing_v2.types.revocation_content

    out: RevocationContents = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing_v2.types.revocation_content.deserialize_query(
                child
            )
        )
    return out
