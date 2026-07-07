"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class PurchaseRequest(TypedDict, closed=True):
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances.</p>"""
    purchase_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The purchase token.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PurchaseRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_count" in value:
        pairs.append((f"{prefix}.InstanceCount", str(value["instance_count"])))
    if "purchase_token" in value:
        pairs.append((f"{prefix}.PurchaseToken", str(value["purchase_token"])))


def deserialize_ec2_query(el: Element) -> PurchaseRequest:
    out: PurchaseRequest = {}  # type: ignore[typeddict-item]
    child_instance_count = el.find("InstanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    child_purchase_token = el.find("PurchaseToken")
    if child_purchase_token is not None:
        out["purchase_token"] = str(child_purchase_token.text or "")
    return out
