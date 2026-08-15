"""Generated from Smithy shape ``com.amazonaws.ec2#PayerResponsibilitySet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.payer_responsibility_entry

PayerResponsibilitySet: TypeAlias = list[
    "capo_ec2.types.payer_responsibility_entry.PayerResponsibilityEntry"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PayerResponsibilitySet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.payer_responsibility_entry

        capo_ec2.types.payer_responsibility_entry.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> PayerResponsibilitySet:
    import capo_ec2.types.payer_responsibility_entry

    out: PayerResponsibilitySet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.payer_responsibility_entry.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> PayerResponsibilitySet:
    import capo_ec2.types.payer_responsibility_entry

    out: PayerResponsibilitySet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.payer_responsibility_entry.deserialize_ec2_query(child)
        )
    return out
