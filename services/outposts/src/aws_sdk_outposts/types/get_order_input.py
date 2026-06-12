"""Generated from Smithy shape ``com.amazonaws.outposts#GetOrderInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.order_id


class GetOrderInput(TypedDict):
    order_id: "aws_sdk_outposts.types.order_id.OrderId"
    """<p>The ID of the order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOrderInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetOrderInput:
    out: GetOrderInput = {}  # type: ignore[typeddict-item]
    return out
