"""Generated from Smithy shape ``com.amazonaws.outposts#EC2Capacity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.family
    import aws_sdk_outposts.types.max_size
    import aws_sdk_outposts.types.quantity


class EC2Capacity(TypedDict):
    family: NotRequired["aws_sdk_outposts.types.family.Family"]
    """<p> The family of the EC2 capacity. </p>"""
    max_size: NotRequired["aws_sdk_outposts.types.max_size.MaxSize"]
    """<p> The maximum size of the EC2 capacity. </p>"""
    quantity: NotRequired["aws_sdk_outposts.types.quantity.Quantity"]
    """<p> The quantity of the EC2 capacity. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EC2Capacity) -> dict:
    out: dict = {}
    if "family" in value:
        out["Family"] = value["family"]
    if "max_size" in value:
        out["MaxSize"] = value["max_size"]
    if "quantity" in value:
        out["Quantity"] = value["quantity"]
    return out


def deserialize_json(data: dict) -> EC2Capacity:
    out: EC2Capacity = {}  # type: ignore[typeddict-item]
    if "Family" in data:
        out["family"] = data["Family"]
    if "MaxSize" in data:
        out["max_size"] = data["MaxSize"]
    if "Quantity" in data:
        out["quantity"] = data["Quantity"]
    return out
