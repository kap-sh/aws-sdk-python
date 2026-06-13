"""Generated from Smithy shape ``com.amazonaws.groundstation#Elevation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.angle_units


class Elevation(TypedDict):
    value: "float"
    """<p>Elevation angle value.</p>"""
    unit: "aws_sdk_groundstation.types.angle_units.AngleUnits"
    """<p>Elevation angle units.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Elevation) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    import aws_sdk_groundstation.types.angle_units

    out["unit"] = aws_sdk_groundstation.types.angle_units.serialize_json(value["unit"])
    return out


def deserialize_json(data: dict) -> Elevation:
    out: Elevation = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Elevation.value required")
    if "unit" in data:
        import aws_sdk_groundstation.types.angle_units

        out["unit"] = aws_sdk_groundstation.types.angle_units.deserialize_json(
            data["unit"]
        )
    else:
        raise DeserializationError("Elevation.unit required")
    return out
