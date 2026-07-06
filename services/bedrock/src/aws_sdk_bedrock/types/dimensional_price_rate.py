"""Generated from Smithy shape ``com.amazonaws.bedrock#DimensionalPriceRate``."""

from typing_extensions import NotRequired, TypedDict


class DimensionalPriceRate(TypedDict, closed=True):
    dimension: NotRequired["str"]
    """<p>Dimension for the price rate.</p>"""
    price: NotRequired["str"]
    """<p>Single-dimensional rate information.</p>"""
    description: NotRequired["str"]
    """<p>Description of the price rate.</p>"""
    unit: NotRequired["str"]
    """<p>Unit associated with the price.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DimensionalPriceRate) -> dict:
    out: dict = {}
    if "dimension" in value:
        out["dimension"] = value["dimension"]
    if "price" in value:
        out["price"] = value["price"]
    if "description" in value:
        out["description"] = value["description"]
    if "unit" in value:
        out["unit"] = value["unit"]
    return out


def deserialize_json(data: dict) -> DimensionalPriceRate:
    out: DimensionalPriceRate = {}  # type: ignore[typeddict-item]
    if "dimension" in data:
        out["dimension"] = data["dimension"]
    if "price" in data:
        out["price"] = data["price"]
    if "description" in data:
        out["description"] = data["description"]
    if "unit" in data:
        out["unit"] = data["unit"]
    return out
