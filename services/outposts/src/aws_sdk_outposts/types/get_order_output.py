"""Generated from Smithy shape ``com.amazonaws.outposts#GetOrderOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.order


class GetOrderOutput(TypedDict):
    order: NotRequired["aws_sdk_outposts.types.order.Order"]


# --- restJson1 ser/de ---
def serialize_json(value: GetOrderOutput) -> dict:
    out: dict = {}
    if "order" in value:
        import aws_sdk_outposts.types.order

        out["Order"] = aws_sdk_outposts.types.order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> GetOrderOutput:
    out: GetOrderOutput = {}  # type: ignore[typeddict-item]
    if "Order" in data:
        import aws_sdk_outposts.types.order

        out["order"] = aws_sdk_outposts.types.order.deserialize_json(data["Order"])
    return out
