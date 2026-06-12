"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollPriceValueRange``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.sensitive_double


class RouteTollPriceValueRange(TypedDict):
    min: "aws_sdk_geo_routes.types.sensitive_double.SensitiveDouble"
    """<p>Minimum price.</p>"""
    max: "aws_sdk_geo_routes.types.sensitive_double.SensitiveDouble"
    """<p>Maximum price.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollPriceValueRange) -> dict:
    out: dict = {}
    out["Min"] = value["min"]
    out["Max"] = value["max"]
    return out


def deserialize_json(data: dict) -> RouteTollPriceValueRange:
    out: RouteTollPriceValueRange = {}  # type: ignore[typeddict-item]
    if "Min" in data:
        out["min"] = data["Min"]
    else:
        raise DeserializationError("RouteTollPriceValueRange.min required")
    if "Max" in data:
        out["max"] = data["Max"]
    else:
        raise DeserializationError("RouteTollPriceValueRange.max required")
    return out
