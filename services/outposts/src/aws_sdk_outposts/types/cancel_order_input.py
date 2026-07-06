"""Generated from Smithy shape ``com.amazonaws.outposts#CancelOrderInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.order_id


class CancelOrderInput(TypedDict, closed=True):
    order_id: "aws_sdk_outposts.types.order_id.OrderId"
    """<p> The ID of the order. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelOrderInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelOrderInput:
    out: CancelOrderInput = {}  # type: ignore[typeddict-item]
    return out
