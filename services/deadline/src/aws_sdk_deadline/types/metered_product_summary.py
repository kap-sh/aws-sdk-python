"""Generated from Smithy shape ``com.amazonaws.deadline#MeteredProductSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.bounded_string
    import aws_sdk_deadline.types.metered_product_id
    import aws_sdk_deadline.types.port_number


class MeteredProductSummary(TypedDict):
    product_id: "aws_sdk_deadline.types.metered_product_id.MeteredProductId"
    """<p>The product ID.</p>"""
    family: "aws_sdk_deadline.types.bounded_string.BoundedString"
    """<p>The family to which the metered product belongs.</p>"""
    vendor: "aws_sdk_deadline.types.bounded_string.BoundedString"
    """<p>The vendor.</p>"""
    port: "aws_sdk_deadline.types.port_number.PortNumber"
    """<p>The port on which the metered product should run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MeteredProductSummary) -> dict:
    out: dict = {}
    out["productId"] = value["product_id"]
    out["family"] = value["family"]
    out["vendor"] = value["vendor"]
    out["port"] = value["port"]
    return out


def deserialize_json(data: dict) -> MeteredProductSummary:
    out: MeteredProductSummary = {}  # type: ignore[typeddict-item]
    if "productId" in data:
        out["product_id"] = data["productId"]
    else:
        raise DeserializationError("MeteredProductSummary.product_id required")
    if "family" in data:
        out["family"] = data["family"]
    else:
        raise DeserializationError("MeteredProductSummary.family required")
    if "vendor" in data:
        out["vendor"] = data["vendor"]
    else:
        raise DeserializationError("MeteredProductSummary.vendor required")
    if "port" in data:
        out["port"] = data["port"]
    else:
        raise DeserializationError("MeteredProductSummary.port required")
    return out
