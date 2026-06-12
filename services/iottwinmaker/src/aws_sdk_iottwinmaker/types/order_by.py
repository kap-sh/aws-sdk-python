"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#OrderBy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.order
    import aws_sdk_iottwinmaker.types.string


class OrderBy(TypedDict):
    order: NotRequired["aws_sdk_iottwinmaker.types.order.Order"]
    """<p>The set order that filters results.</p>"""
    property_name: "aws_sdk_iottwinmaker.types.string.String"
    """<p>The property name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrderBy) -> dict:
    out: dict = {}
    if "order" in value:
        out["order"] = value["order"]
    out["propertyName"] = value["property_name"]
    return out


def deserialize_json(data: dict) -> OrderBy:
    out: OrderBy = {}  # type: ignore[typeddict-item]
    if "order" in data:
        out["order"] = data["order"]
    if "propertyName" in data:
        out["property_name"] = data["propertyName"]
    else:
        raise DeserializationError("OrderBy.property_name required")
    return out
