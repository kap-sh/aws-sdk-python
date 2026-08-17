"""Generated from Smithy shape ``com.amazonaws.ec2#ProductCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.product_code

ProductCodeList: TypeAlias = list["capo_ec2.types.product_code.ProductCode"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ProductCodeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.product_code

        capo_ec2.types.product_code.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> ProductCodeList:
    import capo_ec2.types.product_code

    out: ProductCodeList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.product_code.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ProductCodeList:
    import capo_ec2.types.product_code

    out: ProductCodeList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.product_code.deserialize_ec2_query(child))
    return out
