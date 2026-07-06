"""Generated from Smithy shape ``com.amazonaws.outposts#CreateOrderOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.order


class CreateOrderOutput(TypedDict, closed=True):
    order: NotRequired["aws_sdk_outposts.types.order.Order"]
    """<p>Information about this order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOrderOutput) -> dict:
    out: dict = {}
    if "order" in value:
        import aws_sdk_outposts.types.order

        out["Order"] = aws_sdk_outposts.types.order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> CreateOrderOutput:
    out: CreateOrderOutput = {}  # type: ignore[typeddict-item]
    if "Order" in data:
        import aws_sdk_outposts.types.order

        out["order"] = aws_sdk_outposts.types.order.deserialize_json(data["Order"])
    return out
