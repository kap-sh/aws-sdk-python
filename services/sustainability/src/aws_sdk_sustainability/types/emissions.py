"""Generated from Smithy shape ``com.amazonaws.sustainability#Emissions``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sustainability.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sustainability.types.emissions_unit


class Emissions(TypedDict):
    value: "float"
    """<p>The numeric value of the emissions quantity.</p>"""
    unit: "aws_sdk_sustainability.types.emissions_unit.EmissionsUnit"
    """<p>The unit of measurement for the emissions value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Emissions) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    import aws_sdk_sustainability.types.emissions_unit

    out["Unit"] = aws_sdk_sustainability.types.emissions_unit.serialize_json(
        value["unit"]
    )
    return out


def deserialize_json(data: dict) -> Emissions:
    out: Emissions = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("Emissions.value required")
    if "Unit" in data:
        import aws_sdk_sustainability.types.emissions_unit

        out["unit"] = aws_sdk_sustainability.types.emissions_unit.deserialize_json(
            data["Unit"]
        )
    else:
        raise DeserializationError("Emissions.unit required")
    return out
