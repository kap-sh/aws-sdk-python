"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseRequestSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.purchase_request

PurchaseRequestSet: TypeAlias = list["capo_ec2.types.purchase_request.PurchaseRequest"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PurchaseRequestSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.purchase_request

        capo_ec2.types.purchase_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> PurchaseRequestSet:
    import capo_ec2.types.purchase_request

    out: PurchaseRequestSet = []
    for child in el.findall("PurchaseRequest"):
        out.append(capo_ec2.types.purchase_request.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> PurchaseRequestSet:
    import capo_ec2.types.purchase_request

    out: PurchaseRequestSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.purchase_request.deserialize_ec2_query(child))
    return out
