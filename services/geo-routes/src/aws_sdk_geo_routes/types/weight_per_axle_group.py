"""Generated from Smithy shape ``com.amazonaws.georoutes#WeightPerAxleGroup``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.weight_kilograms


class WeightPerAxleGroup(TypedDict):
    single: "aws_sdk_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>Total weight in kilograms for single axle configurations.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    tandem: "aws_sdk_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>Total weight in kilograms for tandem (two adjacent) axle configurations.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    triple: "aws_sdk_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>Total weight in kilograms for triple (three adjacent) axle configurations.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    quad: "aws_sdk_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>Total weight in kilograms for quad (four adjacent) axle configurations.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""
    quint: "aws_sdk_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>Total weight in kilograms for quint (five adjacent) axle configurations.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WeightPerAxleGroup) -> dict:
    out: dict = {}
    out["Single"] = value.get("single", 0)
    out["Tandem"] = value.get("tandem", 0)
    out["Triple"] = value.get("triple", 0)
    out["Quad"] = value.get("quad", 0)
    out["Quint"] = value.get("quint", 0)
    return out


def deserialize_json(data: dict) -> WeightPerAxleGroup:
    out: WeightPerAxleGroup = {}  # type: ignore[typeddict-item]
    if "Single" in data:
        out["single"] = data["Single"]
    else:
        out["single"] = 0
    if "Tandem" in data:
        out["tandem"] = data["Tandem"]
    else:
        out["tandem"] = 0
    if "Triple" in data:
        out["triple"] = data["Triple"]
    else:
        out["triple"] = 0
    if "Quad" in data:
        out["quad"] = data["Quad"]
    else:
        out["quad"] = 0
    if "Quint" in data:
        out["quint"] = data["Quint"]
    else:
        out["quint"] = 0
    return out
