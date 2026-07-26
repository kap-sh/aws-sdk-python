"""Generated from Smithy shape ``com.amazonaws.ec2#ProductCode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.product_code_values
    import capo_ec2.types.string


class ProductCode(TypedDict, closed=True):
    product_code_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The product code.</p>"""
    product_code_type: NotRequired[
        "capo_ec2.types.product_code_values.ProductCodeValues"
    ]
    """<p>The type of product code.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ProductCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "product_code_id" in value:
        pairs.append((f"{prefix}.ProductCode", str(value["product_code_id"])))
    if "product_code_type" in value:
        import capo_ec2.types.product_code_values

        capo_ec2.types.product_code_values.serialize_ec2_query(
            value["product_code_type"], pairs, f"{prefix}.Type"
        )


def deserialize_ec2_query(el: Element) -> ProductCode:
    out: ProductCode = {}  # type: ignore[typeddict-item]
    child_product_code_id = el.find("ProductCode")
    if child_product_code_id is not None:
        out["product_code_id"] = str(child_product_code_id.text or "")
    child_product_code_type = el.find("Type")
    if child_product_code_type is not None:
        import capo_ec2.types.product_code_values

        out["product_code_type"] = (
            capo_ec2.types.product_code_values.deserialize_ec2_query(
                child_product_code_type
            )
        )
    return out
