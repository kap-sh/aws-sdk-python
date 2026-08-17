"""Generated from Smithy shape ``com.amazonaws.ec2#PricingDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.pricing_detail

PricingDetailsList: TypeAlias = list["capo_ec2.types.pricing_detail.PricingDetail"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PricingDetailsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.pricing_detail

        capo_ec2.types.pricing_detail.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> PricingDetailsList:
    import capo_ec2.types.pricing_detail

    out: PricingDetailsList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.pricing_detail.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> PricingDetailsList:
    import capo_ec2.types.pricing_detail

    out: PricingDetailsList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.pricing_detail.deserialize_ec2_query(child))
    return out
