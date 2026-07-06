"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#Selector``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.bounded_string
    import aws_sdk_marketplace_discovery.types.selector_type


class Selector(TypedDict, closed=True):
    type: "aws_sdk_marketplace_discovery.types.selector_type.SelectorType"
    """<p>The category of the selector, such as <code>Duration</code>.</p>"""
    value: "aws_sdk_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The value of the selector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Selector) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_discovery.types.selector_type

    out["type"] = aws_sdk_marketplace_discovery.types.selector_type.serialize_json(
        value["type"]
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Selector:
    out: Selector = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_marketplace_discovery.types.selector_type

        out["type"] = (
            aws_sdk_marketplace_discovery.types.selector_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("Selector.type required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Selector.value required")
    return out
