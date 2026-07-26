"""Generated from Smithy shape ``com.amazonaws.groundstation#Elevation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.angle_units


class Elevation(TypedDict, closed=True):
    value: "float"
    """<p>Elevation angle value.</p>"""
    unit: "capo_groundstation.types.angle_units.AngleUnits"
    """<p>Elevation angle units.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Elevation) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    import capo_groundstation.types.angle_units

    out["unit"] = capo_groundstation.types.angle_units.serialize_json(value["unit"])
    return out


def deserialize_json(data: dict) -> Elevation:
    out: Elevation = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Elevation.value required")
    if "unit" in data:
        import capo_groundstation.types.angle_units

        out["unit"] = capo_groundstation.types.angle_units.deserialize_json(
            data["unit"]
        )
    else:
        raise DeserializationError("Elevation.unit required")
    return out
