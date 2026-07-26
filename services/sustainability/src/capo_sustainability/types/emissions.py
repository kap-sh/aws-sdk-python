"""Generated from Smithy shape ``com.amazonaws.sustainability#Emissions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sustainability.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sustainability.types.emissions_unit


class Emissions(TypedDict, closed=True):
    value: "float"
    """<p>The numeric value of the emissions quantity.</p>"""
    unit: "capo_sustainability.types.emissions_unit.EmissionsUnit"
    """<p>The unit of measurement for the emissions value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Emissions) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    import capo_sustainability.types.emissions_unit

    out["Unit"] = capo_sustainability.types.emissions_unit.serialize_json(value["unit"])
    return out


def deserialize_json(data: dict) -> Emissions:
    out: Emissions = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("Emissions.value required")
    if "Unit" in data:
        import capo_sustainability.types.emissions_unit

        out["unit"] = capo_sustainability.types.emissions_unit.deserialize_json(
            data["Unit"]
        )
    else:
        raise DeserializationError("Emissions.unit required")
    return out
