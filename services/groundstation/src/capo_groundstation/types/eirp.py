"""Generated from Smithy shape ``com.amazonaws.groundstation#Eirp``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.eirp_units


class Eirp(TypedDict, closed=True):
    value: "float"
    """<p>Value of an EIRP. Valid values are between 20.0 to 50.0 dBW.</p>"""
    units: "capo_groundstation.types.eirp_units.EirpUnits"
    """<p>Units of an EIRP.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Eirp) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    import capo_groundstation.types.eirp_units

    out["units"] = capo_groundstation.types.eirp_units.serialize_json(value["units"])
    return out


def deserialize_json(data: dict) -> Eirp:
    out: Eirp = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Eirp.value required")
    if "units" in data:
        import capo_groundstation.types.eirp_units

        out["units"] = capo_groundstation.types.eirp_units.deserialize_json(
            data["units"]
        )
    else:
        raise DeserializationError("Eirp.units required")
    return out
