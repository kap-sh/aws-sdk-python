"""Generated from Smithy shape ``com.amazonaws.ec2#CancellationTermsSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.cancellation_terms

CancellationTermsSet: TypeAlias = list[
    "capo_ec2.types.cancellation_terms.CancellationTerms"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancellationTermsSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.cancellation_terms

        capo_ec2.types.cancellation_terms.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> CancellationTermsSet:
    import capo_ec2.types.cancellation_terms

    out: CancellationTermsSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.cancellation_terms.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> CancellationTermsSet:
    import capo_ec2.types.cancellation_terms

    out: CancellationTermsSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.cancellation_terms.deserialize_ec2_query(child))
    return out
