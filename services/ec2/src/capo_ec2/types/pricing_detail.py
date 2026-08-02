"""Generated from Smithy shape ``com.amazonaws.ec2#PricingDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.double
    import capo_ec2.types.integer


class PricingDetail(TypedDict, closed=True):
    count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of reservations available for the price.</p>"""
    price: NotRequired["capo_ec2.types.double.Double"]
    """<p>The price per instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PricingDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "count" in value:
        pairs.append((f"{key_prefix}Count", str(value["count"])))
    if "price" in value:
        pairs.append((f"{key_prefix}Price", str(value["price"])))


def deserialize_ec2_query(el: Element) -> PricingDetail:
    out: PricingDetail = {}  # type: ignore[typeddict-item]
    child_count = el.find("Count")
    if child_count is not None:
        out["count"] = int(child_count.text or "")
    child_price = el.find("Price")
    if child_price is not None:
        out["price"] = float(child_price.text or "")
    return out
