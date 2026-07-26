"""Generated from Smithy shape ``com.amazonaws.quicksight#DecimalPlacesConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.decimal_places


class DecimalPlacesConfiguration(TypedDict, closed=True):
    decimal_places: "capo_quicksight.types.decimal_places.DecimalPlaces"
    """<p>The values of the decimal places.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DecimalPlacesConfiguration) -> dict:
    out: dict = {}
    out["DecimalPlaces"] = value["decimal_places"]
    return out


def deserialize_json(data: dict) -> DecimalPlacesConfiguration:
    out: DecimalPlacesConfiguration = {}  # type: ignore[typeddict-item]
    if "DecimalPlaces" in data:
        out["decimal_places"] = data["DecimalPlaces"]
    else:
        raise DeserializationError("DecimalPlacesConfiguration.decimal_places required")
    return out
